import pandas as pd
import glob
import os
from ftfy import fix_text

# -------------------------
# Debug: show working dir
# -------------------------
print("CURRENT WORKING DIRECTORY:", os.getcwd())

TEXT_COLUMNS = [
    "message", "text", "content", "body", "msg", "message_text"
]

# Absolute project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "*.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "merged.csv")

all_files = glob.glob(RAW_DATA_PATH)
dfs = []

for file in all_files:
    print(f"Processing: {file}")

    df = pd.read_csv(file, encoding="utf-8")

    # normalize column names
    df.columns = [c.strip().lower() for c in df.columns]

    # find message column
    message_col = None
    for col in TEXT_COLUMNS:
        if col in df.columns:
            message_col = col
            break

    if message_col is None:
        print(f"Skipping (no text column): {file}")
        continue

    # rename to standard name
    df = df.rename(columns={message_col: "message"})

    # keep only existing required columns
    required = ["id", "category", "language", "message", "label", "split"]
    df = df[[c for c in required if c in df.columns]]

    # fix unicode text
    df["message"] = df["message"].astype(str).apply(fix_text)

    dfs.append(df)

# -------------------------
# Merge & save
# -------------------------
merged = pd.concat(dfs, ignore_index=True)
merged.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")

print("✅ MERGED FILE SAVED AT:", OUTPUT_PATH)
print("📊 Total rows:", len(merged))
