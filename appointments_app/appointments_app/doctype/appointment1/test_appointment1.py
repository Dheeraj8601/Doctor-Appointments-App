# Copyright (c) 2024, dheeraj and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase
from appointments_app.appointments_app.appointments_app.doctype.appointment1 import add_to_appointment_queue

class TestAppointment1(FrappeTestCase):
    def test_add_to_appointment_queue(self):
        doctor = frappe.get_doc({"doctype":"Doctor","name":"Test Doctor"}).insert()
        clinic = frappe.get_doc({"doctype":"Clinic","name":"Test Clinic","doctor":doctor.name,"contact_number":"+6565675455"}).insert()
        shift = frappe.get_doc({"doctype":"Schedule Shift","start_time":"9:00:00","end_time":"15:00:00","clinic":clinic.name}).insert()
        day = '2024-04-12'
        appointment = frappe.get({
            "doctype":"Appointment",
            "clinic": clinic.name,
            "shift": shift.name,
            "date":day,
            "patient_name":"Test Patient"
        }).insert()

        self.assertEqual(appointment.queue_number, 1)

    def tearDown(self):
        frappe.db.rollback()
