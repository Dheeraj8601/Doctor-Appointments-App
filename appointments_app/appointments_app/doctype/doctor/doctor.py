# Copyright (c) 2024, dheeraj and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document

class Doctor(Document):
    def validate(self):
        self.full_name = f"{self.first_name} {self.last_name or ''}"

        # Print full name for validation
        frappe.msgprint(f"{self.full_name}")
