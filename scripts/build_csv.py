import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

raw_dir = Path("data/raw")

records = []

"""
Parcours récursif de tous les fichiers et sous dossiers de data/raw
"""
for split_dir in raw_dir.rglob("*"):
    if split_dir.is_file():
        # on ne veut que les fichiers textes, pas les dossiers
        category = split_dir.parent.name
        try:
            text = split_dir.read_text(encoding="latin-1")
            records.append({"text": text, "label": category})
        except Exception as e:
            print(f"Erreur sur {split_dir} : {e}")

df = pd.DataFrame(records)
df.to_csv("data/raw/20newsgroup.csv", index=False)
print(f"{len(df)} articles sauvegardés dans data/raw/20newsgroup.csv")
