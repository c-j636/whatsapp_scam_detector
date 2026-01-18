import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "cleaned.csv")

df = pd.read_csv(DATA_PATH)

dup_count = df.duplicated(subset=["message"]).sum()

print("Total rows:", len(df))
print("Duplicate messages:", dup_count)
print("Duplicate percentage:", round(dup_count / len(df) * 100, 2), "%")
