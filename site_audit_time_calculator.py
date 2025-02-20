from audit_days import find_range_for_employee_count, audit_days_table

site_number = 0
number_of_sites = int(input("Please provide the number of additional sites:\n"))
site_number = number_of_sites
site_number_list = []
site_id_number = 1
site_duration_table = {}
while site_number >0:
    site_employee_count = int(input(f"Please provide the employee count to site #{(len(site_number_list)+1)}:\n"))

    site_audit_days = find_range_for_employee_count(audit_days_table, site_employee_count)
    print(f"The number of days for initial audit according to IAF MD 5 is: {round(site_audit_days,2)}")

    employee_similar_activities = int(input("Please provide the number of employees performing similar tasks:\n"))

    effective_number_of_employees = site_employee_count - round(employee_similar_activities/2)
    print (f"The effective number of employees is: {effective_number_of_employees}")

    number_of_days_effective_employees = find_range_for_employee_count(audit_days_table,effective_number_of_employees)
    print (f"The number of days according to the effective number of employees is: "
           f"{round(number_of_days_effective_employees)}\n")
    site_number -=1
    site_number_list.append(site_id_number)
    site_id_number +=1
    site_duration_table["Site Number"] = len(site_number_list)
    site_duration_table["Initial Certification"] = number_of_days_effective_employees
    site_duration_table["Surveillance 1"] = round(number_of_days_effective_employees/3,2)
    site_duration_table["Surveillance 2"] = round(number_of_days_effective_employees/3,2)
    site_duration_table["Recertification"] = round ((number_of_days_effective_employees/3)*2,2)


    print(site_duration_table)
    # print (site_number)
    # print (site_number_list)
    # print (len(site_number_list))