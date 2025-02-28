import os
import pandas as pd

file_path = os.path.abspath("food_database.xlsx")
print(f"📂 Looking for: {file_path}")

if not os.path.exists(file_path):
    print("❌ File not found!")

try:
    df = pd.read_excel(file_path, engine="openpyxl")
    print("✅ File loaded successfully!")
    print("📝 Columns:", df.columns)
except Exception as e:
    print(f"⚠ Error reading file: {e}")
