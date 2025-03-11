# from iaf_codes import iaf_codes
# from reductions import reductions
# from enhancements import enhancements
# from audit_days import audit_days_table, find_range_for_employee_count


from HQ_audit_time_calculator import calculate_hq, other_reductions, other_enhancements, hq_audit_time

calculate_hq()
other_reductions(hq_audit_time)
hq_audit_time = other_enhancements(hq_audit_time)

# print (hq_audit_time)
calculation = True

while calculation:
    check_additional_site = input("Are there additional sites? Type Y or N.\n").lower().strip()
    
    if check_additional_site =="y":
        print("CALCULATION OF AUDIT TIME - ADDITIONAL SITES")
        from site_audit_time_calculator import (calculate_multisite, multisite_table,
                                                total_multisite_audit_duration_table)
        calculate_multisite()
        from audit_duration import create_audit_duration
        create_audit_duration(hq_audit_time)
        multisite_final_table = multisite_table(total_multisite_audit_duration_table)
        calculation = False
    elif check_additional_site =="n":
        from audit_duration import create_audit_duration
        create_audit_duration(hq_audit_time)
        calculation = False
    else:
        print("Invalid option, please type either y or n.\n")
