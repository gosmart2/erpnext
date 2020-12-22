# -*- coding: utf-8 -*-
# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class valveitem(Document):
	def before_save(self):
		val=f'{self.body}{self.disc}{self.seal}{self.dn}'
		go=val.replace(" ","")
		self.item_code = go
