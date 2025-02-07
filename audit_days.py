"""The Function below creates the different employee count ranges found in the document IAF MD:5 2023 and generates the
respective number of audit days for each employee count within the different ranges"""

def create_employee_count_range(start, end, starting_point, increase_rate):
    employee_count_range = {}
    for i in range(start, end + 1):
        # "i" is the employee count for which the respective number of audit days is being calculated.
        audit_days = starting_point + (i - start) * increase_rate
        # The line above calculates the respective number of audit days for a given employee count.
        employee_count_range[i] = audit_days
    return employee_count_range

"""The Function below loops through each one of the ranges of the provided ranges dictionary (audit_days_table) and 
look for the selected_number (employee count provided by the user) and once it is found, returns the respective number
of days"""

def find_range_for_employee_count(ranges, selected_number):
    for range_key, employee_count in ranges.items():
        #The dictionary obtained through "ranges" is converted into a list, so specific positions can be accessed.
        start = list(employee_count.keys())[0]
        end = list(employee_count.keys())[-1]
        starting_point = list(employee_count.values())[0]
        increase_rate = (list(employee_count.values())[1] - list(employee_count.values())[
            0])
        if start <= selected_number <= end:
            return employee_count.get(selected_number, "Number out of range")
    return "Number out of any range"

"""The dictionary below reflects the Table QMS 1 - Quality Management Systems, found in the ANNEX A of de document
IAF MD:5 """

audit_days_table = {
    "range1": create_employee_count_range(1, 5, 1.5, 0.10),
    "range2": create_employee_count_range(6, 10, 2.0, 0.10),
    "range3": create_employee_count_range(11, 15, 2.5, 0.10),
    "range4": create_employee_count_range(16, 25, 3.0, 0.10),
    "range5": create_employee_count_range(26, 45, 4.0, 0.05),
    "range6": create_employee_count_range(46, 65, 5.0, 0.05),
    "range7": create_employee_count_range(66, 85, 6.0, 0.05),
    "range8": create_employee_count_range(86, 125, 8.0, 0.02),
    "range9": create_employee_count_range(126, 175, 8.0, 0.02),
    "range10": create_employee_count_range(176, 275, 9.0, 0.01),
    "range11": create_employee_count_range(276, 425, 10.0, 0.006),
    "range12": create_employee_count_range(426, 625, 11.0, 0.005),
    "range13": create_employee_count_range(626, 875, 12.0, 0.004),
    "range14": create_employee_count_range(876, 1175, 13.0, 0.003),
    "range15": create_employee_count_range(1176, 1550, 14.0, 0.002),
    "range16": create_employee_count_range(1551, 2025, 15.0, 0.002),
    "range17": create_employee_count_range(2026, 2675, 16.0, 0.0015),
    "range18": create_employee_count_range(2676, 3450, 17.0, 0.0012),
    "range19": create_employee_count_range(3451, 4350, 18.0, 0.001),
    "range20": create_employee_count_range(4351, 5450, 19.0, 0.0009),
    "range21": create_employee_count_range(5451, 6800, 20.0, 0.0007),
    "range22": create_employee_count_range(6801, 8500, 21.0, 0.0005),
    "range23": create_employee_count_range(8501, 10700, 22.0, 0.0004),
    "range24": create_employee_count_range(10701, 100000, 23.0, 0.0004)
}
