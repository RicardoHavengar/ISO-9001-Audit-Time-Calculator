from audit_days import find_range_for_employee_count, audit_days_table
from tabulate import tabulate
from HQ_audit_time_calculator import total_enhancement_percentage, total_reduction_percentage, total_time_adjustment

site_number = 0
number_of_sites = int(input("Please provide the number of additional sites:\n"))
site_number = number_of_sites
site_number_list = []
site_id_number = 1
multisite_duration_table = {}
site_duration_table = {}
total_enhancement_percentage = total_enhancement_percentage
total_reduction_percentage = total_reduction_percentage

def round_to_half(x):
    return round(x * 2)/2

def calculate_multisite():
    global total_reduction_percentage
    global total_enhancement_percentage
    global site_number
    global site_id_number
    while site_number >0:
        site_employee_count = int(input(f"Please provide the employee count to site #{(len(site_number_list)+1)}:\n"))

        site_audit_days = find_range_for_employee_count(audit_days_table, site_employee_count)
        print(f"The number of days for initial audit according to IAF MD 5 is: {round(site_audit_days,2)}")

        employee_similar_activities = int(input("Please provide the number of employees performing similar tasks:\n"))

        effective_number_of_employees = site_employee_count - round(employee_similar_activities/2)
        print (f"The effective number of employees is: {effective_number_of_employees}")


        number_of_days_effective_employees = find_range_for_employee_count(audit_days_table,effective_number_of_employees)
        days_effective_employees_adjusted = (number_of_days_effective_employees +
                                             ((number_of_days_effective_employees * total_time_adjustment)/100))
        print (f"Considering the effective number of employees and the enhancements and reductions resulting "
               f"from IAF code risk, QMS Complexity and QMS Maturity,the number of audit days for this site is: "
                     f"{round(days_effective_employees_adjusted, 2)}")


        print (f"The current percentage of reduction is:{total_reduction_percentage}")
        print (f"The total number of enhancements is: {total_enhancement_percentage}")
        print (f"Total Adjustment is {total_time_adjustment}")

        additional_reduction = int(input("If applicable, apply further reduction by typing either 10 or 20."
                                         "If no further enhancement is required, please type 0 (zero)\n"))
        reduction_number_of_days_effective_employees = round_to_half (days_effective_employees_adjusted - ((
                site_audit_days * additional_reduction)/100))

        print (round(reduction_number_of_days_effective_employees,2))
        total_reduction_percentage = + additional_reduction
        print (f"The total reduction applied to this site is: {total_reduction_percentage}%\n")

        additional_enhancement = int(input("If applicable, apply further enhancement by typing either  10 or 20."
                                           "If no further enhancement is required, please type 0 (zero)\n"))
        enhancement_number_of_days_effective_employees = round_to_half(reduction_number_of_days_effective_employees + ((
                    site_audit_days * additional_enhancement) / 100))

        total_enhancement_percentage = total_enhancement_percentage + additional_enhancement

        print (f"The total enhancement applied to this site is: {total_enhancement_percentage}%\n")

        print (enhancement_number_of_days_effective_employees)

        print (f"The number of days according to the effective number of employees is: "
               f"{enhancement_number_of_days_effective_employees}\n")
        site_number -=1
        site_number_list.append(site_id_number)
        site_id_number +=1


        site_id = len(site_number_list)
        site_initial_certification = round(enhancement_number_of_days_effective_employees,2)
        site_surveillance_1 = round(enhancement_number_of_days_effective_employees/3,2)
        site_surveillance_2 = round(enhancement_number_of_days_effective_employees/3,2)
        site_recertification = round ((enhancement_number_of_days_effective_employees/3)*2,2)

        cycle_table = [round_to_half(site_initial_certification * 80/100), round_to_half(site_surveillance_1 * 80/100),
                       round_to_half(site_surveillance_2 * 80/100), round_to_half(site_recertification * 80/100)]
        multisite_duration_table[site_id] = cycle_table

    total_multisite_audit_duration_table  = [(key , value[0], value[1], value[2], value[3]) for key, value in multisite_duration_table.items()]
    multisite_table_headers = ["Site Number", "Initial Certification (80% rounded)", "Surveillance 1 (80% rounded)",
                               "Surveillance 2 (80% rounded)", "Recertification (80% rounded)"]

    print (f"{(tabulate(total_multisite_audit_duration_table, headers = multisite_table_headers, tablefmt = "grid"))}")
        # print(multisite_duration_table)

