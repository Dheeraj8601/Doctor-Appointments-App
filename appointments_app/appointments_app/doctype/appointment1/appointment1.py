# Copyright (c) 2024, dheeraj and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
#from my_cache_module import cache

class Appointment1(Document):
    def after_insert(self):
        self.queue_number = self.add_to_appointment_queue()
        #frappe.cache.set_value(f"{frappe.session.sid}:queue_number",self.queue_number)
        frappe.cache().set_value(f"{frappe.session.sid}:queue_number", self.queue_number)
        frappe.msgprint("Queue Number is : " + str(self.queue_number))    
        self.save()

    def add_to_appointment_queue(self):
        filters = {
            "date": self.date,
            "shift": self.shift,
            "clinic": self.clinic,
        }

        appointment_queue_exists = frappe.db.exists("Appointment Queue", filters)

        if appointment_queue_exists:
            q = frappe.get_doc("Appointment Queue", filters)
            print("exists : "+str(q))
        else:
            q = frappe.new_doc("Appointment Queue")
            print("not exists : "+str(q))
            q.update(filters)
            print("not exists after update: "+str(q))
            q.save()

        print("1. "+str(q))
        print(frappe.as_json(q))
        q.append("queue", {"appointment": self.name, "status": "Pending"})
        print("Appointment Name:", self.name)
        print("2. "+str(q))
        q.save(ignore_permissions=True)
        return len(q.queue)
