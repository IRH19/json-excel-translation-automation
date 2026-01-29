import pandas as pd
import json
import os

# --- CONFIGURATION ---
# We now point to the FILLED file, not the empty one
excel_file = "Translation_Master_Filled.xlsx"
output_folder = "output_json_malay"

print(f"Reading {excel_file}...")

# 1. Load the Excel file
try:
    # fillna("") ensures empty cells are empty strings, not 'NaN' errors
    df = pd.read_excel(excel_file).fillna("")
except FileNotFoundError:
    print(f"CRITICAL ERROR: I cannot find '{excel_file}'.")
    print("Did you run the 'auto_translate.py' script first?")
    exit()

# 2. Group data by Filename (process form.json, button.json separately)
grouped = df.groupby("Filename")

# --- HELPER FUNCTION ---
# Turns "admin.label.email" back into {"admin": {"label": {"email": "..."}}}
def unflatten(dictionary, key_path, value):
    keys = key_path.split('.')
    current_level = dictionary
    
    for i, key in enumerate(keys[:-1]):
        # Create nested dictionary if it doesn't exist
        if key not in current_level:
            current_level[key] = {}
        
        # Check if we are trying to add a child to something that isn't a dict
        if not isinstance(current_level[key], dict):
            # This happens if a key is used as both a text AND a folder (rare, but possible)
            print(f"Warning: Key collision at '{key}' in path '{key_path}'. Skipping.")
            return

        current_level = current_level[key]
        
    # Set the value at the final spot
    current_level[keys[-1]] = value

# 3. Create the output folder
os.makedirs(output_folder, exist_ok=True)

# 4. Loop through each file group and reconstruct JSON
print("Reconstructing JSON files...")

for filename, group in grouped:
    json_structure = {}
    
    for index, row in group.iterrows():
        key_path = row['Key_Path']
        
        # LOGIC: Use Malay column. If empty, fallback to English.
        malay_text = str(row['Bahasa_Melayu']).strip()
        english_text = str(row['English_Source']).strip()
        
        # If Malay translation exists, use it. Otherwise, use English.
        final_value = malay_text if malay_text != "" else english_text
            
        unflatten(json_structure, key_path, final_value)

    # 5. Save the new JSON file
    output_path = os.path.join(output_folder, filename)
    with open(output_path, 'w', encoding='utf-8') as f:
        # ensure_ascii=False ensures Malay characters display correctly
        json.dump(json_structure, f, indent=2, ensure_ascii=False)
    
    print(f" -> Generated: {output_path}")

print(f"\nSUCCESS! All new files are inside the '{output_folder}' folder.")