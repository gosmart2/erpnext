from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def create_data(name,company,tome,depart,purpose,intime,totime,date):
	data = frappe.new_doc("Visitor")
	data.name1 = name
	data.company_name= company
	data.to_meet_whom= tome
	data.department= depart
	data.purpose= purpose
	data.in_time=intime
	data.out_time=totime
	data.date=date
	frappe.msgprint("Visitor Form Submitted Successfully")
	data.save()
	frappe.db.commit()
