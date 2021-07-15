import frappe
from frappe.model.document import Document
from frappe import _
import json
from datetime import date
import time
from frappe.model.mapper import get_mapped_doc

def validate(doc, method=None):
	make_project_warehouse(doc)

@frappe.whitelist()
def make_project_warehouse(doc):
		existing_wh = frappe.db.get_all("Warehouse", {"warehouse_name": doc.name})     
		if len(existing_wh) == 0:
			wh_doc = frappe.new_doc("Warehouse")
			wh_doc.parent_warehouse = "Project Warehouse - C"
			wh_doc.warehouse_name = doc.project_name
			wh_doc.save()
			doc.warehouse= wh_doc.name
		else:
			doc.warehouse= existing_wh[0].name
