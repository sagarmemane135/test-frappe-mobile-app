// Copyright (c) 2026, Your Name and contributors
// For license information, please see license.txt

frappe.ui.form.on('Customer', {
	refresh: function(frm) {
		// Add custom buttons or functionality
		if (!frm.is_new()) {
			frm.add_custom_button(__('View Projects'), function() {
				frappe.set_route('List', 'Project', {'customer': frm.doc.name});
			});
			
			frm.add_custom_button(__('Create Project'), function() {
				frappe.new_doc('Project', {
					customer: frm.doc.name
				});
			});
		}
	}
});
