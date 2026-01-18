import pandas as pd
import re
import os

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INPUT_PATH = os.path.join(BASE_DIR, "data", "merged.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "cleaned.csv")

print("Reading from:", INPUT_PATH)

# Load merged dataset
df = pd.read_csv(INPUT_PATH)

# Basic safe cleaning (English-only dataset)
def clean_message(text):
    text = str(text)
    text = re.sub(r"http\S+", " URL ", text)      # replace links
    text = re.sub(r"\b\d{6}\b", " OTP ", text)   # replace OTPs
    text = re.sub(r"\s+", " ", text)             # normalize spaces
    return text.strip()

df["message"] = df["message"].apply(clean_message)

# Save cleaned dataset
df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")

print("CLEANED CSV CREATED AT:", OUTPUT_PATH)
print("TOTAL ROWS:", len(df))
