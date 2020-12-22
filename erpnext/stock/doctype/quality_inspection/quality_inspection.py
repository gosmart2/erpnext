# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from erpnext.stock.doctype.quality_inspection_template.quality_inspection_template \
	import get_template_details
from frappe.model.mapper import get_mapped_doc

class QualityInspection(Document):
	def validate(self):
		if not self.readings and self.item_code:
			self.get_item_specification_details()

	def get_item_specification_details(self):
		if not self.quality_inspection_template:
			self.quality_inspection_template = frappe.db.get_value('Item',
				self.item_code, 'quality_inspection_template')

		if not self.quality_inspection_template: return

		self.set('readings', [])
		parameters = get_template_details(self.quality_inspection_template)
		for d in parameters:
			child = self.append('readings', {})
			child.specification = d.specification
			child.value = d.value
			child.status = "Accepted"

	def get_quality_inspection_template(self):
		template = ''
		if self.bom_no:
			template = frappe.db.get_value('BOM', self.bom_no, 'quality_inspection_template')

		if not template:
			template = frappe.db.get_value('BOM', self.item_code, 'quality_inspection_template')

		self.quality_inspection_template = template
		self.get_item_specification_details()

	def on_submit(self):
		frappe.db.sql("UPDATE `tabPurchase Receipt` SET `total_qty`='"+str(self.total_qty)+"',`total`='"+str(self.total)+"',`base_total`='"+str(self.total)+"',`net_total`='"+str(self.total)+"' WHERE `name`='" +self.receipt_series+"'")
		val=frappe.db.sql("SELECT rate FROM `tabPurchase Taxes and Charges` WHERE parent='"+self.receipt_series+"'")
		for x in val:
			amt=self.total*(x[0]/100)
			tot=amt+self.total
			frappe.db.sql("UPDATE `tabPurchase Taxes and Charges` SET `tax_amount`='"+str(amt)+"',`total`='"+str(tot)+"',`tax_amount_after_discount_amount`='"+str(amt)+"',`base_tax_amount`='"+str(amt)+"',`base_total`='"+str(tot)+"',`base_tax_amount_after_discount_amount`='"+str(amt)+"' WHERE `parent`='" +self.receipt_series+"'")
			frappe.db.sql("UPDATE `tabPurchase Receipt` SET `grand_total`='"+str(tot)+"',`taxes_and_charges_added`='"+str(amt)+"',`total_taxes_and_charges`='"+str(amt)+"',`rounded_total`='"+str(tot)+"',`base_rounded_total`='"+str(tot)+"',`base_grand_total`='"+str(tot)+"',`base_total_taxes_and_charges`='"+str(amt)+"',`base_taxes_and_charges_added`='"+str(amt)+"' WHERE `name`='" +self.receipt_series+"'")
		for item in self.get("items"):
			if(item.ins_status == "Accepted"):
				frappe.db.sql("UPDATE `tabPurchase Receipt Item` SET `accepted_qty`='"+str(item.qty)+"',`rejected_qty`='"+str(0.00)+"',`quality_status`='Accepted',`amount`='"+str(item.amount)+"' WHERE `parent`='" +self.receipt_series+"' AND `item_code`='" +item.item_code+"'")
			else:
				frappe.db.sql("UPDATE `tabPurchase Receipt Item` SET `accepted_qty`='"+str(0.00)+"',`rejected_qty`='"+str(item.qty)+"',`quality_status`='Rejected',`amount`='"+str(item.amount)+"' WHERE `parent`='" +self.receipt_series+"' AND `item_code`='" +item.item_code+"'")
		self.update_qc_reference()

	def on_cancel(self):
		self.update_qc_reference()

	def update_qc_reference(self):
		quality_inspection = self.name if self.docstatus == 1 else ""
		doctype = self.reference_type + ' Item'
		if self.reference_type == 'Stock Entry':
			doctype = 'Stock Entry Detail'

		if self.reference_type and self.reference_name:
			frappe.db.sql("""update `tab{child_doc}` t1, `tab{parent_doc}` t2
				set t1.quality_inspection = %s, t2.modified = %s
				where t1.parent = %s and t1.item_code = %s and t1.parent = t2.name"""
				.format(parent_doc=self.reference_type, child_doc=doctype),
				(quality_inspection, self.modified, self.reference_name, self.item_code))

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def item_query(doctype, txt, searchfield, start, page_len, filters):
	if filters.get("from"):
		from frappe.desk.reportview import get_match_cond
		mcond = get_match_cond(filters["from"])
		cond, qi_condition = "", "and (quality_inspection is null or quality_inspection = '')"

		if filters.get('from') in ['Purchase Invoice Item', 'Purchase Receipt Item']\
				and filters.get("inspection_type") != "In Process":
			cond = """and item_code in (select name from `tabItem` where
				inspection_required_before_purchase = 1)"""
		elif filters.get('from') in ['Sales Invoice Item', 'Delivery Note Item']\
				and filters.get("inspection_type") != "In Process":
			cond = """and item_code in (select name from `tabItem` where
				inspection_required_before_delivery = 1)"""
		elif filters.get('from') == 'Stock Entry Detail':
			cond = """and s_warehouse is null"""

		if filters.get('from') in ['Supplier Quotation Item']:
			qi_condition = ""

		return frappe.db.sql(""" select item_code from `tab{doc}`
			where parent=%(parent)s and docstatus < 2 and item_code like %(txt)s
			{qi_condition} {cond} {mcond}
			order by item_code limit {start}, {page_len}""".format(doc=filters.get('from'),
			parent=filters.get('parent'), cond = cond, mcond = mcond, start = start,
			page_len = page_len, qi_condition = qi_condition),
			{'parent': filters.get('parent'), 'txt': "%%%s%%" % txt})

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def quality_inspection_query(doctype, txt, searchfield, start, page_len, filters):
	return frappe.get_all('Quality Inspection',
		limit_start=start,
		limit_page_length=page_len,
		filters = {
			'docstatus': 1,
			'name': ('like', '%%%s%%' % txt),
			'item_code': filters.get("item_code"),
			'reference_name': ('in', [filters.get("reference_name", ''), ''])
		}, as_list=1)

@frappe.whitelist()
def make_quality_inspection(source_name, target_doc=None):
	def postprocess(source, doc):
		doc.inspected_by = frappe.session.user
		doc.get_quality_inspection_template()

	doc = get_mapped_doc("BOM", source_name, {
		'BOM': {
			"doctype": "Quality Inspection",
			"validation": {
				"docstatus": ["=", 1]
			},
			"field_map": {
				"name": "bom_no",
				"item": "item_code",
				"stock_uom": "uom",
				"stock_qty": "qty"
			},
		}
	}, target_doc, postprocess)
	return doc

@frappe.whitelist()
def make_quality(source_name, target_doc=None):
	doc = get_mapped_doc("Quality Inspection", source_name, {
		"Quality Inspection": {
			"doctype": "Stock Entry",
			"validation": {
				"docstatus": ["=", 1]
			}
		},
		"Quality Inspection Item": {
			"doctype": "Stock Entry Detail",
			"field_map": {
				"stock_qty": "transfer_qty",
				"batch_no": "batch_no",
				"rate":"basic_rate"
			},
			"condition": lambda doc: doc.ins_status=="Accepted"
		}
	}, target_doc)
	return doc
'''
	for d in doc.get("items"):
		if d.ins_status == "Accepted":
			doc.append('items', {
				"item_code": d.item_code,
				"ins_status":d.ins_status,
				"qty": d.qty,
				"uom":d.uom,
				"conversion_factor":d.conversion_factor,
				"stock_uom":d.stock_uom,
				"stock_qty":d.stock_qty
				})
'''