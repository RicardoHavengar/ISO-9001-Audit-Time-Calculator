import pandas as pd

file_path = r"C:\Users\ricar\OneDrive\Desktop\Development Projects\ISO 9001 Audit Time Calculator"
df = pd.read_excel('iaf_code_list.xlsx')

iaf_codes = df.set_index('No').to_dict(orient= 'index')


iaf_codes_table = [(key,  value["Description"], value ["Risk Level"]) for key, value in iaf_codes.items()]
headers = ["No", "Description", "Risk Level"]