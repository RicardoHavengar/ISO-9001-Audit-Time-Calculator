from tabulate import tabulate
from iaf_codes import iaf_codes_table, headers, iaf_codes


def iaf_code_selection():
    print("SELECT THE IAF CODE:")
    input("Please select the IAF code associated to the scope of certification. Press" " ENTER " "to view the table:" )
    print(tabulate(iaf_codes_table,headers= headers, tablefmt="grid"))
    selected_iaf_code = int(input("Please type the Number associated to the IAF code related to the scope of "
                                  "certification:\n"))
    selected_iaf_code_risk = (iaf_codes[selected_iaf_code]["Risk Level"])

    print (f"The Risk Level for the selected code is: {selected_iaf_code_risk}")
    iaf_code_risk = 0
    if selected_iaf_code_risk == "High":
        iaf_code_risk +=10
    else:
        iaf_code_risk = iaf_code_risk

    return iaf_code_risk

