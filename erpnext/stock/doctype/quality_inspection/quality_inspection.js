cur_frm.cscript.refresh = cur_frm.cscript.inspection_type;

frappe.ui.form.on("Quality Inspection", {
refresh: function(frm) {
	if (frm.doc.docstatus===0) {
			frm.add_custom_button(__('Purchase Receipt'), function() {
				erpnext.utils.map_current_doc({
					method: "erpnext.stock.doctype.purchase_receipt.purchase_receipt.make_quality",
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

frappe.ui.form.on("Quality Inspection Item", {
	acc_qty: function(frm,cdt, cdn){
		calculate_total(frm, cdt, cdn);
	},
	rate: function(frm, cdt, cdn){
		calculate_total(frm, cdt, cdn);
	},
	ins_status: function(frm, cdt, cdn){
		calculate_total(frm, cdt, cdn);
	}
});
var calculate_total = function(frm, cdt, cdn) {
	var child = locals[cdt][cdn];
	frappe.model.set_value(cdt, cdn, "amount", child.acc_qty * child.rate);

	var i,sum=0,sum_amount=0,sub=0,sub_amount=0,val,val2,r;
	var temp = frm.doc.items;

	for(i=0;i<temp.length;i++)
	{
		if(temp[i].ins_status=="Accepted")
		{
		sum+=temp[i].acc_qty;
		sum_amount+=temp[i].amount;
		}
	}
	if(child.ins_status=="Accepted")
	{
	frm.set_value("total_qty",sum);
	frm.set_value("total",sum_amount);
	}
	else if(child.ins_status=="Rejected")
	{
	frappe.model.set_value(cdt, cdn, "acc_qty",0.00);
	frm.set_value("total_qty",sum);
	frm.set_value("total",sum_amount);
	}
	//if(arr.every((val, i, arr)=>val===2))
/*
	for(i=0;i<temp.length;i++)
	{
		if(temp.every((val2,r,temp=>val2==="Rejected")))	
		{
			val=0.00
		}
		else if(temp[i].ins_status=="Accepted")
		{
		sum+=temp[i].qty;
		sum_amount+=temp[i].amount;
		}
		else if(temp[i].ins_status=="Rejected")
		{
		sub=frm.doc.total_qty-temp[i].qty;
		sub_amount=frm.doc.total-temp[i].amount;	
		}
	}
	if(temp.every((val2,r,temp=>val2==="Rejected")))
	{
		frm.set_value("total_qty",val);
		frm.set_value("total",val);
	}
	else if(child.ins_status=="Accepted")
	{
	frm.set_value("total_qty",sum);
	frm.set_value("total",sum_amount);
	}
	else if(child.ins_status=="Rejected")
	{
	frm.set_value("total_qty",sub);
	frm.set_value("total",sub_amount);
	}
*/
}