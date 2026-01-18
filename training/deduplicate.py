import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_PATH = os.path.join(BASE_DIR, "data", "cleaned.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "cleaned_dedup.csv")

df = pd.read_csv(INPUT_PATH)

df = df.drop_duplicates(subset=["message"])

df.to_csv(OUTPUT_PATH, index=False)

print("Before:", len(pd.read_csv(INPUT_PATH)))
print("After:", len(df))
print("Saved to:", OUTPUT_PATH)
