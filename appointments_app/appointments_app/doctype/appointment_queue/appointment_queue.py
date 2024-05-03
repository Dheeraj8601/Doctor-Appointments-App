# Copyright (c) 2024, dheeraj and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AppointmentQueue(Document):
	pass


def create_queues_for_today():
	clinics = frappe.get_doc("Clinic",filters = {"is_published":True}, pluck = "name")

	for clinic in clinics:
		# shifts = frappe.get_all("Schedule Shift",filters = {"clinic":clinic},pluck="name")
		# for shift in shifts:
		# 	frappe.get_doc(
		# 		{
		# 			"doctype":"Appointment Queue",
		# 			"clinic" :clinic,
		# 			"date"   :frappe.utils.today(),
		# 			"shift"  : shift,
		# 		}
		# 	).insert(ignore_if_duplicate = True)
		frappe.get_doc(
			{
				"doctype":"Appointment Queue",
				"clinic" : clinic,
				"date"   : frappe.utils.today(),
			}
		).insert(ignore_if_duplicate = True)