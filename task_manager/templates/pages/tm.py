# Copyright (c) 2026, Your Name and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import now_datetime, get_fullname

no_cache = 1

def get_context(context):
    context.no_cache = 1
    context.show_sidebar = False
    
    # Check if user is logged in
    if frappe.session.user == "Guest":
        context.is_guest = True
        context.title = "Task Manager"
        return context
    
    # User is logged in, show the mobile app
    context.is_guest = False
    context.title = "Task Manager"
    context.user = frappe.session.user
    context.user_fullname = get_fullname(frappe.session.user)
    
    # Get user's tasks summary
    context.my_tasks = get_my_tasks()
    context.recent_tasks = get_recent_tasks()
    context.task_stats = get_task_stats()
    context.projects = get_user_projects()
    
    return context

def get_my_tasks():
    """Get tasks assigned to current user"""
    return frappe.get_all(
        "Task",
        filters={"assigned_to": frappe.session.user},
        fields=["name", "subject", "status", "priority", "project", "exp_end_date", "progress"],
        order_by="modified desc",
        limit=20
    )

def get_recent_tasks():
    """Get recently updated tasks"""
    return frappe.get_all(
        "Task",
        fields=["name", "subject", "status", "priority", "assigned_to", "modified"],
        order_by="modified desc",
        limit=10
    )

def get_task_stats():
    """Get task statistics for current user"""
    user = frappe.session.user
    
    total = frappe.db.count("Task", {"assigned_to": user})
    open_tasks = frappe.db.count("Task", {"assigned_to": user, "status": "Open"})
    working = frappe.db.count("Task", {"assigned_to": user, "status": "Working"})
    completed = frappe.db.count("Task", {"assigned_to": user, "status": "Completed"})
    
    return {
        "total": total,
        "open": open_tasks,
        "working": working,
        "completed": completed
    }

def get_user_projects():
    """Get projects for current user"""
    # Get projects where user has tasks
    projects = frappe.db.sql("""
        SELECT DISTINCT p.name, p.project_name, p.status, p.percent_complete
        FROM `tabProject` p
        INNER JOIN `tabTask` t ON t.project = p.name
        WHERE t.assigned_to = %s
        ORDER BY p.modified DESC
        LIMIT 10
    """, frappe.session.user, as_dict=True)
    
    return projects
