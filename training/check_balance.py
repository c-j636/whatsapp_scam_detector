import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "cleaned.csv")

df = pd.read_csv(DATA_PATH)

print("Total rows:", len(df))
print("\nLabel counts:")
print(df["label"].value_counts())

print("\nLabel percentage:")
print(df["label"].value_counts(normalize=True) * 100)
