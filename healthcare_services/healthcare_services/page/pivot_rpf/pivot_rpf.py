# Copyright (c) 2022, ayman and contributors
# For license information, please see license.txt

# import frappe
from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt,getdate
from frappe.model.mapper import get_mapped_doc
import frappe.model.rename_doc as rd
from datetime import timedelta, date,datetime
from frappe.utils import add_to_date

class pivot_rpf(Document):
	pass


@frappe.whitelist()
def pivot_rpf_q(date ,date2):
	data = []
	data_rpf = frappe.db.sql(""" select a.date as 'Date' , a.facility_name as 'Facility Name', b.ser_name as 'Service Name', a.ind_price_id as 'Indicator Price'
	   , b.ser_no as 'Service Nubmer'  , QUARTER(a.date) as 'Quarter'
	  ,(b.ser_price * b.ser_no) as cost,(a.quality_bounce *(b.ser_price * b.ser_no))+(b.ser_price * b.ser_no) as 'net with quality',(a.quality_bounce *(b.ser_price * b.ser_no))+(b.ser_price * b.ser_no) as 'net after deduction'
	  ,((a.quality_bounce *(b.ser_price * b.ser_no))+(b.ser_price * b.ser_no)/100) * a.medical_supply as 'Medical Supply'
	  ,((a.quality_bounce *(b.ser_price * b.ser_no))+(b.ser_price * b.ser_no)/100) * a.incentive as 'incentive' 
	   from `tabRBF Data` a , `tabService Detail` b where a.name= b.parent 
	  and Date(a.date) between %s and %s """,(date,date2),as_dict=True)







	ret = {
		'data_rpf': data_rpf

	}

	return ret

