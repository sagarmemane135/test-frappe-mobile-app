// Copyright (c) 2026, Your Name and contributors
// For license information, please see license.txt

frappe.ui.form.on('Project', {
	refresh: function(frm) {
		if (!frm.is_new()) {
			// Add custom button to view tasks
			frm.add_custom_button(__('View Tasks'), function() {
				frappe.set_route('List', 'Task', {'project': frm.doc.name});
			});
			
			// Add custom button to create task
			frm.add_custom_button(__('Create Task'), function() {
				frappe.new_doc('Task', {
					project: frm.doc.name,
					customer: frm.doc.customer
				});
			});
			
			// Add progress indicator
			frm.dashboard.add_indicator(__('Progress: {0}%', [frm.doc.percent_complete]), 
				frm.doc.percent_complete < 30 ? 'red' : 
				frm.doc.percent_complete < 70 ? 'orange' : 'green');
		}
	},
	
	status: function(frm) {
		// Auto-set actual end date when completed
		if (frm.doc.status === 'Completed' && !frm.doc.actual_end_date) {
			frm.set_value('actual_end_date', frappe.datetime.get_today());
			frm.set_value('percent_complete', 100);
		}
	}
});
