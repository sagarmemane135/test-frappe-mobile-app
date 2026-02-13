# Copyright (c) 2026, Your Name and contributors
# For license information, please see license.txt

import frappe

no_cache = 1

def get_context(context):
    # Redirect to app if already logged in
    if frappe.session.user != "Guest":
        frappe.local.flags.redirect_location = "/app"
        raise frappe.Redirect
    
    context.no_cache = 1
    context.show_sidebar = False
    
    # Get app info from hooks
    app_name = frappe.get_hooks("app_title")[0] if frappe.get_hooks("app_title") else "Task Manager"
    app_description = frappe.get_hooks("app_description")[0] if frappe.get_hooks("app_description") else "Mobile-friendly task management"
    
    context.title = app_name
    context.app_name = app_name
    context.app_description = app_description
    
    return context
