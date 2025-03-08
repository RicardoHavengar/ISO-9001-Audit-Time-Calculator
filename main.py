# from iaf_codes import iaf_codes
# from reductions import reductions
# from enhancements import enhancements
# from audit_days import audit_days_table, find_range_for_employee_count


from HQ_audit_time_calculator import calculate_hq, hq_audit_time

calculate_hq()
check_additional_site = input("Are there additional sites? Type Y or N.\n")
if check_additional_site =="Y":
    from site_audit_time_calculator import calculate_multisite
    calculate_multisite()
else:
    from audit_duration import create_audit_duration
    create_audit_duration(hq_audit_time)
