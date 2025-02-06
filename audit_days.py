def create_number_range(start, end, starting_point, increase_rate):
    number_range = {}
    for i in range(start, end + 1):
        value = starting_point + (i - start) * increase_rate
        number_range[i] = value
    return number_range

def find_range_for_number(ranges, selected_number):
    for range_key, range_info in ranges.items():
        start, end, starting_point, increase_rate = range_info
        if start <= selected_number <= end:
            number_range = create_number_range(start, end, starting_point, increase_rate)
            return number_range.get(selected_number, "Number out of range")
    return "Number out of any range"

range1 = create_number_range(1,5,1.5,0.10)
range2 = create_number_range(6,10,2.0,0.10)
range3 = create_number_range(11,15,2.5,0.10)
range4 = create_number_range(16,25,3.0,0.10)
range5 = create_number_range(26,45,4.0,0.05)
range6 = create_number_range(46,65,5.0,0.05)
range7 = create_number_range(66,85,6.0,0.05)
range8 = create_number_range(86,125,8.0,0.02)
range9 = create_number_range(126,175,8.0,0.02)
range10 =create_number_range(176,275,9.0,0.01)
range11 = create_number_range(276,425,10.0,0.006)
range12 = create_number_range(426,625,11.0,0.005)
range13 = create_number_range(626,875,12.0,0.004)
range14 = create_number_range(876,1175,13.0,0.003)
range15 = create_number_range(1176,1550,14.0,0.002)
range16 = create_number_range(1551,2025,15.0,0.002)
range17 = create_number_range(2026,2675,16.0,0.0015)
range18 = create_number_range(2676,3450,17.0,0.0012)
range19 = create_number_range(3451,4350,18.0,0.001)
range20 = create_number_range(4351,5450,19.0,0.0009)
range21 = create_number_range(5451,6800,20.0,0.0007)
range22 = create_number_range(6801,8500,21.0,0.0005)
range23 = create_number_range(8501,10700,22.0,0.0004)
range24 = create_number_range(10701,100000,23.0,0.0004)

ranges = {
    "range1": create_number_range(1, 5, 1.5, 0.10),
    "range2": create_number_range(6, 10, 2.0, 0.10),
    "range3": create_number_range(11, 15, 2.5, 0.10),
    "range4": create_number_range(16, 25, 3.0, 0.10),
    "range5": create_number_range(26, 45, 4.0, 0.05),
    "range6": create_number_range(46, 65, 5.0, 0.05),
    "range7": create_number_range(66, 85, 6.0, 0.05),
    "range8": create_number_range(86, 125, 8.0, 0.02),
    "range9": create_number_range(126, 175, 8.0, 0.02),
    "range10": create_number_range(176, 275, 9.0, 0.01),
    "range11": create_number_range(276, 425, 10.0, 0.006),
    "range12": create_number_range(426, 625, 11.0, 0.005),
    "range13": create_number_range(626, 875, 12.0, 0.004),
    "range14": create_number_range(876, 1175, 13.0, 0.003),
    "range15": create_number_range(1176, 1550, 14.0, 0.002),
    "range16": create_number_range(1551, 2025, 15.0, 0.002),
    "range17": create_number_range(2026, 2675, 16.0, 0.0015),
    "range18": create_number_range(2676, 3450, 17.0, 0.0012),
    "range19": create_number_range(3451, 4350, 18.0, 0.001),
    "range20": create_number_range(4351, 5450, 19.0, 0.0009),
    "range21": create_number_range(5451, 6800, 20.0, 0.0007),
    "range22": create_number_range(6801, 8500, 21.0, 0.0005),
    "range23": create_number_range(8501, 10700, 22.0, 0.0004),
    "range24": create_number_range(10701, 100000, 23.0, 0.0004),
}
