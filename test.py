import sys
from pathlib import Path

root = (
    Path(__file__).resolve().parent
)  # pas parents[1], juste parent car fichier à la racine
sys.path.insert(0, str(root))

print("Racine :", root)
print("src existe ?", (root / "src").exists())

print("Import OK !")
