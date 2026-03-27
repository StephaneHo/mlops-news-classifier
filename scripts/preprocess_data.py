import sys
from pathlib import Path

"""
ATTENTION: sys.path.insert toujours avant tout import src.
"""

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.data_processing.preprocessing.text_cleaner import preprocess_dataset

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root))


print("Racine ajoutée :", root)  # ← doit afficher mlops-news-classifier
print("src existe ?", (root / "src").exists())  #

preprocess_dataset(
    input_path=Path("data/raw/20newsgroup.csv"),
    output_path=Path("data/processed/20newsgroup_clean.csv"),
)
