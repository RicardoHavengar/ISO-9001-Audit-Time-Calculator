from reductions import reduction_table, headers
from enhancements import enhancement_table, headers
from tabulate import tabulate
print("Welcome to the ISO 9001 Audit Time Calculator")

organization_name = input("Please type the name of the organization to be certified:\n")
scope_of_certification = input("Please type the desired scope of certification:\n")

print("We will start the calculation of audit days at the organization's Headquarters.")
hq_employee_count = int(input("Please type the number of employees of the organization's Headquarters:\n"))
no_employee_similar_activities = int(input("Please type the number of employees performing similar activities:\n"))

print("The next 4 questions will help us on defining the Complexity Level of the organization's QMS.")
processes_complexity_score = input("How would you score the complexity of the organization's processes? Type 1:LOW, "
                                   "2:MEDIUM, 3:HIGH:\n")
volume_of_processes = input("How would you score the volume of processes? Type 1:LOW, 2:MEDIUM, 3:HIGH:\n")
volume_of_sites = input("How would you score the volume of sites? Type 1:SMALL, 2:MEDIUM, 3:LARGE:\n")
scope_complexity = input("How would you score the complexity of the scope of certification? Type 1:LOW, 2:MEDIUM, "
                         "3:HIGH:\n ")

print("The next 4 questions will help us on defining the Maturity Level of the organization's QMS.")
internal_audit_maturity = input("How would you score the maturity of the Internal Audit Program? Type 1:LOW, 2:MEDIUM, "
                           "3:HIGH:\n")
delivery_performance = input("How would you score the on-time delivery performance? Type 1:LOW, 2:MEDIUM, 3:HIGH:\n")
product_conformity = input("How would you score the conformity of the delivered products? Type 1:LOW, 2:MEDIUM, "
                           "3:HIGH:\n")
customer_satisfaction = input("How would you score the Customer Satisfaction? Type 1:LOW, 2:MEDIUM, 3:HIGH:\n")

print("Based on the information provided above,the final scores are:")
print (" Complexity of the Quality Management System: {complexity_score}")
print (" Maturity of the Quality Management System: {maturity_score}")
print(" The percentage of reduction applied to the calculation is {% of reduction}")
print(" The percentage of enhancement applied to the calculation is {% of enhancement}\n")

input(f"The table below provides a list of reductions and their respective percentages.\n"
      f"{(tabulate(reduction_table, headers=headers, tablefmt="grid"))} \n"
      "If you wish to apply further reductions to this calculation, please type below the related number.\n"
      "IMPORTANT: The maximum amount of reduction allowed for the calculation is 30%.\n")

input(f"The table below provides a list of enhancements and their respective percentages.\n"
      f"{(tabulate(enhancement_table, headers=headers, tablefmt="grid"))} \n"
      "If you wish to apply further enhancements to this calculation, please type below the related number.\n")