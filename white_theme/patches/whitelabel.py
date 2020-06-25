from __future__ import unicode_literals
import frappe

def execute():
    # frappe.db.sql("""update help set intro='',content=''""")
    frappe.db.sql("""delete from tabPage where name='welcome-to-erpnext'""")
