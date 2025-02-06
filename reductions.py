import pandas as pd

file_path = r"C:\Users\ricar\OneDrive\Desktop\Development Projects\ISO 9001 Audit Time Calculator"
df = pd.read_excel('reductions.xlsx')

reductions = df.set_index('No').to_dict(orient= 'index')

