# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "healthcare_services"
app_title = "Healthcare Services"
app_publisher = "Yamaan org"
app_description = "Healthcare Services"
app_icon = "fa fa-heartbeat"
app_color = "'green'"
app_email = "aymen.alsurabi@yamaan.org"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/css/healthcare_services.css"
app_include_js = ["/assets/js/healthcare_services.min.js"]

#"/assets/healthcare_services/js/pivotjs/jquery-ui.min.js",

# include js, css files in header of web template
# web_include_css = "/assets/healthcare_services/css/healthcare_services.css"
# web_include_js = "/assets/healthcare_services/js/healthcare_services.js"

# include js in page
# page_js = {"pivot_rpf": "public/js/pivotjs/jquery-ui.min.js"}

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

# Website user home page (by function)
# get_website_user_home_page = "healthcare_services.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "healthcare_services.install.before_install"
# after_install = "healthcare_services.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "healthcare_services.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"healthcare_services.tasks.all"
# 	],
# 	"daily": [
# 		"healthcare_services.tasks.daily"
# 	],
# 	"hourly": [
# 		"healthcare_services.tasks.hourly"
# 	],
# 	"weekly": [
# 		"healthcare_services.tasks.weekly"
# 	]
# 	"monthly": [
# 		"healthcare_services.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "healthcare_services.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "healthcare_services.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "healthcare_services.task.get_dashboard_data"
# }

