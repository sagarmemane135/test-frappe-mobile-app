# Copyright (c) 2026, Your Name and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Task(Document):
	def validate(self):
		# Validate dates
		if self.exp_start_date and self.exp_end_date:
			if self.exp_start_date > self.exp_end_date:
				frappe.throw("Expected Start Date cannot be after Expected End Date")
		
		if self.act_start_date and self.act_end_date:
			if self.act_start_date > self.act_end_date:
				frappe.throw("Actual Start Date cannot be after Actual End Date")
	
	def on_update(self):
		# Update project progress if linked
		if self.project:
			self.update_project_progress()
	
	def update_project_progress(self):
		"""Update project progress based on tasks"""
		project = frappe.get_doc("Project", self.project)
		
		# Get all tasks for this project
		tasks = frappe.get_all("Task", 
			filters={"project": self.project},
			fields=["progress", "status"])
		
		if tasks:
			# Calculate average progress
			total_progress = sum(task.progress or 0 for task in tasks)
			avg_progress = total_progress / len(tasks)
			
			# Update project
			project.percent_complete = avg_progress
			
			# Check if all tasks are completed
			all_completed = all(task.status == "Completed" for task in tasks)
			if all_completed and project.status != "Completed":
				project.status = "Completed"
				project.actual_end_date = frappe.utils.today()
			
			project.save()
