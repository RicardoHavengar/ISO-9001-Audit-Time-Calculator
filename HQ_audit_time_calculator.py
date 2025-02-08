from reductions import reduction_table, reduction_headers
from enhancements import enhancement_table, headers
from tabulate import tabulate
from audit_days import find_range_for_employee_count
from audit_days import audit_days_table, find_range_for_employee_count
from iaf_codes import iaf_codes, iaf_codes_table, headers

hq_audit_time = 0
total_reduction_percentage = 0
total_enhancement_percentage = 0

print("Welcome to the ISO 9001 Audit Time Calculator")

organization_name = input("Please type the name of the organization to be certified:\n")
scope_of_certification = input("Please type the desired scope of certification:\n")

print("EMPLOYEES COUNT")
print("We will start the calculation of audit days for the organization's Headquarters.")
hq_employee_count = int(input("Please type the number of employees of the organization's Headquarters:\n"))
hq_audit_time = find_range_for_employee_count(audit_days_table,hq_employee_count)
print(f"The audit time according to the IAF MD 5 table for initial certification is: {hq_audit_time}\n")


print ("NUMBER OF EMPLOYEE PERFORMING SIMILAR ACTIVITIES")
no_employee_similar_activities = int(input("Please type the number of employees performing similar activities:\n"))
effective_no_employee = hq_employee_count - (no_employee_similar_activities/2)
print(f"The effective number of employee is: {effective_no_employee}")
hq_audit_time = find_range_for_employee_count(audit_days_table,effective_no_employee)
print(f"Based on the effective number of employees, the audit time is {hq_audit_time}")



print("SELECT THE IAF CODE:")
input("Please select the IAF code associated to the scope of certification. Press" " ENTER " "to view the table:" )
print(tabulate(iaf_codes_table,headers= headers, tablefmt="grid"))
selected_iaf_code = int(input("Please type the Number associated to the IAF code related to the scope of "
                              "certification:\n"))
selected_iaf_code_risk = (iaf_codes[selected_iaf_code]["Risk Level"])
print (f"The Risk Level for the selected code is: {selected_iaf_code_risk}")
if selected_iaf_code_risk == "High":
    hq_audit_time = hq_audit_time +((hq_audit_time*10)/100)
    total_enhancement_percentage +=10
else:
    hq_audit_time = hq_audit_time
print(total_enhancement_percentage)
print(f"The audit time has been adjusted to: {hq_audit_time}\n")


print("DETERMINE THE COMPLEXITY OF THE QMS")
print("The next 4 questions will help us on defining the Complexity Level of the organization's QMS.")
processes_complexity_score = int(input("How would you score the complexity of the organization's processes? "
                                       "Type 1:LOW, 2:MEDIUM, 3:HIGH:\n"))
volume_of_processes = int(input("How would you score the volume of processes? Type 1:LOW, 2:MEDIUM, 3:HIGH:\n"))
volume_of_sites = int(input("How would you score the volume of sites? Type 1:SMALL, 2:MEDIUM, 3:LARGE:\n"))
scope_complexity = int(input("How would you score the complexity of the scope of certification? Type 1:LOW, 2:MEDIUM, "
                         "3:HIGH:\n"))

qms_complexity_score = processes_complexity_score +volume_of_processes +volume_of_sites + scope_complexity
if qms_complexity_score >= 10:
    qms_complexity = "High"
    total_enhancement_percentage += 10
elif 10 > qms_complexity_score > 6:
    qms_complexity = "Medium"
else:
    qms_complexity = "Low"
    total_reduction_percentage +=10
print(f"The complexity of the Quality Management System has been determined as: {qms_complexity}\n")

if qms_complexity == "High":
    hq_audit_time = hq_audit_time +((hq_audit_time*10)/100)
elif qms_complexity == "Low":
    hq_audit_time = hq_audit_time - ((hq_audit_time * 10) / 100)
else:
    hq_audit_time = hq_audit_time
print(f"The audit time has been adjusted to: {hq_audit_time}\n")
print(total_enhancement_percentage)
print(total_reduction_percentage)


print("DETERMINE THE MATURITY OF THE QUALITY MANAGEMENT SYSTEM")
print("The next 4 questions will help us on defining the Maturity Level of the organization's QMS.")
internal_audit_maturity = int(input("How would you score the maturity of the Internal Audit Program? Type 1:LOW, "
                                    "2:MEDIUM, "
                           "3:HIGH:\n"))
delivery_performance = int(input("How would you score the on-time delivery performance? Type 1:LOW, 2:MEDIUM, "
                                 "3:HIGH:\n"))
product_conformity = int(input("How would you score the conformity of the delivered products? Type 1:LOW, 2:MEDIUM, "
                           "3:HIGH:\n"))
customer_satisfaction = int(input("How would you score the Customer Satisfaction? Type 1:LOW, 2:MEDIUM, 3:HIGH:\n"))


qms_maturity_score = internal_audit_maturity + delivery_performance + product_conformity + customer_satisfaction
if qms_maturity_score >= 10:
    qms_maturity = "High"
elif 10 > qms_maturity_score > 6:
    qms_maturity = "Medium"
else:
    qms_maturity = "Low"

print(f"The maturity of the Quality Management System has been determined as: {qms_maturity}\n")
if qms_maturity == "High":
    hq_audit_time = hq_audit_time -((hq_audit_time*10)/100)
    total_reduction_percentage =+10
elif qms_maturity == "Low":
    hq_audit_time = hq_audit_time + ((hq_audit_time * 10) / 100)
    total_enhancement_percentage =+10
else:
    hq_audit_time = hq_audit_time

print(f"The audit time has been adjusted to: {hq_audit_time}\n")
print(total_enhancement_percentage)
print(total_reduction_percentage)

print("OTHER REDUCTIONS")

print("Next, a list of other reason for audit time reduction will be provided. Press" " Enter " "to see the list:")

print(f"{(tabulate(reduction_table, headers=reduction_headers, tablefmt="grid"))} \n")
other_reduction_selection = int(input ("If you wish to apply further reductions to this calculation, please type below the "
                         "related number.\n"
      "IMPORTANT: The maximum amount of reduction allowed for the calculation is 30%.\n"))

percentage_other_reduction = (reduction_table[other_reduction_selection][2])
print(f"The audit time has been reduced in {percentage_other_reduction}%")




print("OTHER ENHANCEMENTS")

input(f"The table below provides a list of enhancements and their respective percentages.\n"
      f"{(tabulate(enhancement_table, headers=headers, tablefmt="grid"))} \n"
      "If you wish to apply further enhancements to this calculation, please type below the related number.\n")