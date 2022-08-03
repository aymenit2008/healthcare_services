from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Document"),
			"items": [
				{
					"type": "doctype",
					"name": "RBF Data",
					"onboard": 1,
				}
			]
			
		},
		{
			"label": _("Setup"),
			"items": [
				{
					"type": "doctype",
					"name": "Facility",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Item",
					"onboard": 1,
				},				
				{
					"type": "doctype",
					"name": "Service Department",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Indicator Price",
					"onboard": 1,
				},
			]
			
		},
		{
			"label": _("Report"),
			"items": [
				{
					"type": "page",
					"name": "pivot_rpf",
					"label": _("Pivot Report"),
					"onboard": 1,
				}
			]

		}
	]
