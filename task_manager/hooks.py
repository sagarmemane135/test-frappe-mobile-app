from . import __version__ as app_version

app_name = "task_manager"
app_title = "Task Manager"
app_publisher = "Your Name"
app_description = "A mobile-friendly PWA task management app"
app_email = "your.email@example.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/task_manager/css/task_manager.css"
app_include_js = "/assets/task_manager/js/task_manager.js"

# include js, css files in header of web template
web_include_css = "/assets/task_manager/css/task_manager.css"
web_include_js = "/assets/task_manager/js/task_manager.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "task_manager/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "task_manager.utils.jinja_methods",
#	"filters": "task_manager.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "task_manager.install.before_install"
# after_install = "task_manager.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "task_manager.uninstall.before_uninstall"
# after_uninstall = "task_manager.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "task_manager.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"task_manager.tasks.all"
#	],
#	"daily": [
#		"task_manager.tasks.daily"
#	],
#	"hourly": [
#		"task_manager.tasks.hourly"
#	],
#	"weekly": [
#		"task_manager.tasks.weekly"
#	],
#	"monthly": [
#		"task_manager.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "task_manager.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "task_manager.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "task_manager.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"task_manager.auth.validate"
# ]

# PWA Configuration
# -----------------
# Enable PWA support
pwa_enabled = True

# Service worker configuration
service_worker_path = "/assets/task_manager/js/service-worker.js"

# App manifest
pwa_manifest = {
    "name": "Task Manager",
    "short_name": "TaskMgr",
    "description": "Mobile-friendly task management app",
    "theme_color": "#2490ef",
    "background_color": "#ffffff",
    "display": "standalone",
    "scope": "/",
    "start_url": "/app",
    "orientation": "any",
    "icons": [
        {
            "src": "/assets/task_manager/images/icon-192x192.png",
            "sizes": "192x192",
            "type": "image/png"
        },
        {
            "src": "/assets/task_manager/images/icon-512x512.png",
            "sizes": "512x512",
            "type": "image/png"
        }
    ]
}
