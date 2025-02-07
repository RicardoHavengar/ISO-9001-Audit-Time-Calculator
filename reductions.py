import pandas as pd
from tabulate import tabulate

file_path = r"C:\Users\ricar\OneDrive\Desktop\Development Projects\ISO 9001 Audit Time Calculator"
df = pd.read_excel('reductions.xlsx')

reductions = df.set_index('No').to_dict(orient= 'index')

reduction_table = [(key,  value["Reduction Description"], value ["Percentage"]) for key, value in reductions.items()]
headers = ["No", "Reduction Description", "Percentage"]
