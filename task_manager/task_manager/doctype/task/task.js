// Copyright (c) 2026, Your Name and contributors
// For license information, please see license.txt

frappe.ui.form.on('Task', {
	refresh: function(frm) {
		// Mobile-friendly quick actions
		if (frm.doc.status === 'Open') {
			frm.add_custom_button(__('Start Working'), function() {
				frm.set_value('status', 'Working');
				if (!frm.doc.act_start_date) {
					frm.set_value('act_start_date', frappe.datetime.get_today());
				}
				frm.save();
			}).addClass('btn-primary');
		}
		
		if (frm.doc.status === 'Working') {
			frm.add_custom_button(__('Mark Complete'), function() {
				frm.set_value('status', 'Completed');
				frm.set_value('progress', 100);
				if (!frm.doc.act_end_date) {
					frm.set_value('act_end_date', frappe.datetime.get_today());
				}
				frm.save();
			}).addClass('btn-success');
		}
		
		// Add comment button
		if (!frm.is_new()) {
			frm.add_custom_button(__('Add Comment'), function() {
				let d = new frappe.ui.Dialog({
					title: 'Add Comment',
					fields: [
						{
							label: 'Comment',
							fieldname: 'comment',
							fieldtype: 'Text Editor',
							reqd: 1
						}
					],
					primary_action_label: 'Add',
					primary_action(values) {
						let row = frm.add_child('comments');
						row.comment = values.comment;
						row.commented_by = frappe.session.user;
						row.comment_time = frappe.datetime.now_datetime();
						frm.refresh_field('comments');
						frm.save();
						d.hide();
					}
				});
				d.show();
			}).addClass('btn-default');
		}
		
		// Show progress indicator
		if (frm.doc.progress) {
			frm.dashboard.add_indicator(__('Progress: {0}%', [frm.doc.progress]), 
				frm.doc.progress < 30 ? 'red' : 
				frm.doc.progress < 70 ? 'orange' : 'green');
		}
	},
	
	project: function(frm) {
		// Auto-fetch customer from project
		if (frm.doc.project) {
			frappe.db.get_value('Project', frm.doc.project, 'customer', (r) => {
				if (r && r.customer) {
					frm.set_value('customer', r.customer);
				}
			});
		}
	},
	
	status: function(frm) {
		// Auto-set dates based on status
		if (frm.doc.status === 'Working' && !frm.doc.act_start_date) {
			frm.set_value('act_start_date', frappe.datetime.get_today());
		}
		
		if (frm.doc.status === 'Completed') {
			if (!frm.doc.act_end_date) {
				frm.set_value('act_end_date', frappe.datetime.get_today());
			}
			if (frm.doc.progress < 100) {
				frm.set_value('progress', 100);
			}
		}
	}
});

// List view customization for mobile
frappe.listview_settings['Task'] = {
	add_fields: ["status", "priority", "progress"],
	get_indicator: function(doc) {
		if (doc.status === "Completed") {
			return [__("Completed"), "green", "status,=,Completed"];
		} else if (doc.status === "Working") {
			return [__("Working"), "orange", "status,=,Working"];
		} else if (doc.status === "Cancelled") {
			return [__("Cancelled"), "red", "status,=,Cancelled"];
		} else {
			return [__("Open"), "blue", "status,=,Open"];
		}
	},
	onload: function(listview) {
		// Add custom filters for mobile
		listview.page.add_inner_button(__('My Tasks'), function() {
			listview.filter_area.add([[listview.doctype, "assigned_to", "=", frappe.session.user]]);
		});
		
		listview.page.add_inner_button(__('High Priority'), function() {
			listview.filter_area.add([[listview.doctype, "priority", "in", ["High", "Urgent"]]]);
		});
	}
};
