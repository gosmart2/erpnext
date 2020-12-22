from __future__ import unicode_literals
import frappe,json

@frappe.whitelist()
def create_data(doc):
	list=[]
	for item in frappe.db.sql("SELECT * FROM `tabSupplier Quotation` WHERE material_series='MAT-MR-2020-00079'", as_dict=1):
		for val in frappe.db.sql("SELECT * FROM `tabSupplier Quotation Item` WHERE parent='"+item.name+"'", as_dict=1):
			list.append({
			"Supplier":item.supplier,
           	"Item_code":val.item_code,
            "Qty":val.qty,
            "Rate":val.rate,
            "Amount":val.amount
           	})
	return list