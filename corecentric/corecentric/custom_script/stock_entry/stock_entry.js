frappe.ui.form.on('Stock Entry', {
    project : function(frm) {
    	if(frm.doc.project){
    		frappe.db.get_value('Project', {'name': frm.doc.project}, 'warehouse', (r) => {
				if (r && r.warehouse) {
					frm.set_value('from_warehouse', r.warehouse);
				}
			});
    	}
    }
});