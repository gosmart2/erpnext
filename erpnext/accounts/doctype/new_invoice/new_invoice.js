frappe.ui.form.on("New Invoice", {
refresh: function(frm) {
	if (frm.doc.docstatus===0) {
			frm.add_custom_button(__('Purchase Receipt'), function() {
				erpnext.utils.map_current_doc({
					method: "erpnext.stock.doctype.purchase_receipt.purchase_receipt.make_pur_invoice",
					source_doctype: "Purchase Receipt",
					target: frm,
					date_field: "posting_date",
					setters: {
						supplier: frm.doc.supplier || undefined,
					},
					get_query_filters: {
						docstatus: 1
					}
				})
			}, __("Get items from"));
}
}
});