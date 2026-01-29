import json
import pandas as pd
import os
import glob

# 1. Setup lists to hold our data
data_rows = []

# 2. Get all .json files in the current directory
json_files = glob.glob("*.json")

def flatten_json(y):
    out = {}
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '.')
        else:
            out[name[:-1]] = x
    flatten(y)
    return out

# 3. Loop through files and extract data
for file_name in json_files:
    with open(file_name, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            # Flatten the nested structure
            flat_data = flatten_json(data)
            
            for key, value in flat_data.items():
                data_rows.append({
                    "Filename": file_name,
                    "Key_Path": key,
                    "English_Source": value,
                    "Bahasa_Melayu": "" # Blank column for them
                })
        except Exception as e:
            print(f"Error reading {file_name}: {e}")

# 4. Save to Excel
df = pd.DataFrame(data_rows)
df.to_excel("Translation_Master_Sheet.xlsx", index=False)
print("Done! Created 'Translation_Master_Sheet.xlsx'") 