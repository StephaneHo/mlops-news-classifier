from sklearn.model_selection import train_test_split
import pandas as pd

# On charge
df = pd.read_csv("data/processed/all_clean.csv").dropna()

# On splite
train_df, test_df = train_test_split(
    df, test_size=0.2, random_state=42, stratify=df["label"]
)

# On sauvegarde les splits
train_df.to_csv("data/processed/train_clean.csv", index=False)
test_df.to_csv("data/processed/test_clean.csv", index=False)

print(f"Train: {len(train_df)} lignes")
print(f"Test: {len(test_df)} lignes")
