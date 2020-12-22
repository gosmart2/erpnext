// Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Valve Bom', {
	valve_name: function(frm,cdt, cdn){
		go(frm, cdt, cdn);
	},
	refresh: function(frm) {
		frm.add_fetch("valve_name", "body","body");
		frm.add_fetch("valve_name", "disc","disc");
		frm.add_fetch("valve_name", "contact_seal","contact_seal");
	}
});

var go = function(frm, cdt, cdn) {
	var i;
	if(frm.doc.valve_name=='Butterfly Valve')
	{
		//cur_frm.fields_dict.items.grid.toggle_enable("body",false);
	//	cur_frm.fields_dict.items.grid.toggle_display("body",false);
	//cur_frm.fields_dict.items.grid.fields_map.body.hidden = 1;
	}
}