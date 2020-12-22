// Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('valve item', {
	body: function(frm,cdt, cdn){
		go(frm, cdt, cdn);
	}
});

var go = function(frm, cdt, cdn) {
	if(frm.doc.item_description=='Butterfly Valve')
	{
		frm.toggle_display("body",true);
		frm.toggle_display("disc",true);
		frm.toggle_display("seal",true);
		frm.toggle_display("bonnet",false);
		frm.toggle_display("float",false);
		frm.toggle_display("seat",false);
		frm.toggle_display("ball",false);
		frm.toggle_display("spring",false);
		frm.toggle_display("wedge",false);
		frm.toggle_display("strainer",false);
		frm.toggle_display("diaphragm",false);	
	}
	else if(frm.doc.body=='Epoxy Coated Ductile Iron'&&frm.doc.item_description=='Check Valve')
	{
		frm.toggle_display("body",true);
		frm.toggle_display("disc",false);
		frm.toggle_display("seal",false);
		frm.toggle_display("bonnet",true);
		frm.toggle_display("float",false);
		frm.toggle_display("seat",false);
		frm.toggle_display("ball",true);
		frm.toggle_display("spring",false);
		frm.toggle_display("wedge",false);
		frm.toggle_display("strainer",false);
		frm.toggle_display("diaphragm",false);
	}
	else if(frm.doc.body=='SS304'&&frm.doc.item_description=='Check Valve')
	{
		frm.toggle_display("body",true);
		frm.toggle_display("disc",true);
		frm.toggle_display("seal",false);
		frm.toggle_display("bonnet",false);
		frm.toggle_display("float",false);
		frm.toggle_display("seat",false);
		frm.toggle_display("ball",false);
		frm.toggle_display("spring",true);
		frm.toggle_display("wedge",false);
		frm.toggle_display("strainer",false);
		frm.toggle_display("diaphragm",false);
	}
	else if(frm.doc.body=='PVC-U'||frm.doc.body=='C-PVC'&&frm.doc.item_description=='Check Valve')
	{
		frm.toggle_display("body",true);
		frm.toggle_display("disc",true);
		frm.toggle_display("seal",false);
		frm.toggle_display("bonnet",false);
		frm.toggle_display("float",false);
		frm.toggle_display("seat",true);
		frm.toggle_display("ball",false);
		frm.toggle_display("spring",false);
		frm.toggle_display("wedge",false);
		frm.toggle_display("strainer",false);
		frm.toggle_display("diaphragm",false);
	}
	else if(frm.doc.body=='SS316/SS304'&&frm.doc.item_description=='Ball Valve')
	{
		frm.toggle_display("body",true);
		frm.toggle_display("disc",false);
		frm.toggle_display("seal",true);
		frm.toggle_display("bonnet",false);
		frm.toggle_display("float",false);
		frm.toggle_display("seat",false);
		frm.toggle_display("ball",true);
		frm.toggle_display("spring",false);
		frm.toggle_display("wedge",false);
		frm.toggle_display("strainer",false);
		frm.toggle_display("diaphragm",false);
	}
	else if(frm.doc.body=='PVC-U'&&frm.doc.item_description=='Ball Valve')
	{
		frm.toggle_display("body",true);
		frm.toggle_display("disc",false);
		frm.toggle_display("seal",false);
		frm.toggle_display("bonnet",false);
		frm.toggle_display("float",false);
		frm.toggle_display("seat",true);
		frm.toggle_display("ball",false);
		frm.toggle_display("spring",false);
		frm.toggle_display("wedge",false);
		frm.toggle_display("strainer",false);
		frm.toggle_display("diaphragm",false);
	}
	else if(frm.doc.item_description=='Gate Valve')
	{
		frm.toggle_display("body",true);
		frm.toggle_display("disc",false);
		frm.toggle_display("seal",false);
		frm.toggle_display("bonnet",true);
		frm.toggle_display("float",false);
		frm.toggle_display("seat",false);
		frm.toggle_display("ball",false);
		frm.toggle_display("spring",false);
		frm.toggle_display("wedge",true);
		frm.toggle_display("strainer",false);
		frm.toggle_display("diaphragm",false);
	}
	else if(frm.doc.item_description=='Electro Valve')
	{
		frm.toggle_display("body",true);
		frm.toggle_display("disc",false);
		frm.toggle_display("seal",false);
		frm.toggle_display("bonnet",true);
		frm.toggle_display("float",false);
		frm.toggle_display("seat",false);
		frm.toggle_display("ball",false);
		frm.toggle_display("spring",false);
		frm.toggle_display("wedge",false);
		frm.toggle_display("strainer",false);
		frm.toggle_display("diaphragm",true);
	}
	else if(frm.doc.item_description=='Air vent Valve')
	{
		frm.toggle_display("body",true);
		frm.toggle_display("disc",false);
		frm.toggle_display("seal",false);
		frm.toggle_display("bonnet",false);
		frm.toggle_display("float",true);
		frm.toggle_display("seat",true);
		frm.toggle_display("ball",false);
		frm.toggle_display("spring",false);
		frm.toggle_display("wedge",false);
		frm.toggle_display("strainer",false);
		frm.toggle_display("diaphragm",false);
	}
	else if(frm.doc.item_description=='Y-Strainer')
	{
		frm.toggle_display("body",true);
		frm.toggle_display("disc",false);
		frm.toggle_display("seal",true);
		frm.toggle_display("bonnet",false);
		frm.toggle_display("float",false);
		frm.toggle_display("seat",false);
		frm.toggle_display("ball",false);
		frm.toggle_display("spring",false);
		frm.toggle_display("wedge",false);
		frm.toggle_display("strainer",true);
		frm.toggle_display("diaphragm",false);
	}
	else
	{

	}
}