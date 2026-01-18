import pandas as pd
import os
from sklearn.model_selection import train_test_split

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "cleaned_dedup.csv")

df = pd.read_csv(DATA_PATH)

# Sanity check
df["message"] = df["message"].astype(str)

# Stratified split (keeps spam / not_spam ratio)
train_df, val_df = train_test_split(
    df,
    test_size=0.2,
    random_state=42,
    stratify=df["label"]
)

train_path = os.path.join(BASE_DIR, "data", "train.csv")
val_path = os.path.join(BASE_DIR, "data", "val.csv")

train_df.to_csv(train_path, index=False)
val_df.to_csv(val_path, index=False)

print("Total unique rows:", len(df))
print("Train size:", len(train_df))
print("Validation size:", len(val_df))
print("Train saved to:", train_path)
print("Val saved to:", val_path)
