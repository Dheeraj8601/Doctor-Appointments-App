// Copyright (c) 2024, dheeraj and contributors
// For license information, please see license.txt

frappe.ui.form.on('Appointment1', {
	refresh: function(frm) {
                   frm.set_query('shift',(doc) => {
					return {
						filters : {
							"clinic" : doc.clinic
						}
					}
				   })
	}
});
