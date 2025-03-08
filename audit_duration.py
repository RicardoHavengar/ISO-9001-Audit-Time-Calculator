from HQ_audit_time_calculator import hq_audit_time
from tabulate import tabulate
from site_audit_time_calculator import calculate_multisite

def round_to_half(x):
    return round(x * 2)/2

def create_audit_duration(duration):
    total_audit_duration = {}
    initial_certification = round(duration,2)
    initial_on_site_min = round (((initial_certification * 80)/100),2)
    initial_total_on_site = round_to_half(initial_on_site_min)

    surveillance_1 = round(duration/3,2)
    surveillance_1_on_site_min = round((initial_on_site_min/3),2)
    surveillance_1_total_on_site = round_to_half(surveillance_1_on_site_min)

    surveillance_2 = round(duration/3,2)
    surveillance_2_on_site_min = round((initial_on_site_min / 3),2)
    surveillance_2_total_on_site = round_to_half(surveillance_2_on_site_min)

    recertification = round((duration/3)*2,2)
    recertification_on_site_min = round(((initial_on_site_min/3) * 2),2)
    recertification_total_on_site = round_to_half(recertification_on_site_min)

    total_audit_duration["Initial Certification"] = (initial_certification, initial_on_site_min, initial_total_on_site)
    total_audit_duration["Surveillance 1"] = (surveillance_1, surveillance_1_on_site_min, surveillance_1_total_on_site)
    total_audit_duration["Surveillance 2"] = (surveillance_2, surveillance_2_on_site_min, surveillance_2_total_on_site)
    total_audit_duration["Recertification"] = (recertification, recertification_on_site_min, recertification_total_on_site)

    total_audit_duration_table = [(key, value[0], value[1], value[2]) for key, value in total_audit_duration.items()]
    audit_duration_headers = ["Audit Type", "Total Number of Days", "80% On-Site", "Total On-Site"]
    print(f"{(tabulate(total_audit_duration_table, headers=audit_duration_headers, tablefmt="grid"))} \n")


# create_audit_duration(hq_audit_time)
calculate_multisite()