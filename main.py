from iaf_codes import iaf_codes
from reductions import reductions
from enhancements import enhancements
from audit_days import audit_days_table, find_range_for_employee_count

audit_time = find_range_for_employee_count(audit_days_table,2)

print(audit_time)
