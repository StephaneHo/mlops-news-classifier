import logging
from pathlib import Path
import pandas as pd

logger = logging.getLogger(__name__)
"""
Attention, risque d'overfit si on ne retire pas les harders
From: stephane@alt.atheism.edu        ← contient le label !
Newsgroups: alt.atheism               ← contient le label !
"""


def remove_headers(text: str) -> str:
    """
    On va supprimer les headers jusqu' à la première ligne vide
    """
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line.strip() == "":
            return "\n".join(lines[i + 1 :])
    return text


def convert_to_csv(raw_dir: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    # cas 1: strcture train/test séparés (c'est le cas du dataset sklearn)
    has_split = (raw_dir / "20news-bydate-train").exists()

    if has_split:
        splits = {
            "train": raw_dir / "20news-bydate-train",
            "test": raw_dir / "20news-bydate-test",
        }
    else:
        # cas 2: tout est mélangé (c'est le cas du dataset Kaggle)
        subdirs = [d for d in raw_dir.iterdir() if d.is_dir()]
        root = subdirs[0] if len(subdirs) == 1 else raw_dir
        splits = {"all": root}

    for split_name, split_dir in splits.items():
        rows = []
        print(f"Dossier analysé : {split_dir}")
        print(f"Contenu : {list(split_dir.iterdir())}")

        for category_dir in sorted(split_dir.iterdir()):
            # si ce n'est pas un fichier, on passe
            if not category_dir.is_dir():
                continue
            print(f"Catégorie trouvée : {category_dir.name}")

            category = category_dir.name

            for text_file in category_dir.glob("*"):
                if text_file.is_file():
                    try:
                        try:
                            text = text_file.read_text(encoding="utf-8")
                        except UnicodeDecodeError:
                            text = text_file.read_text(
                                encoding="latin-1", errors="replace"
                            )
                        text = remove_headers(text)
                        rows.append({"text": text, "label": category})
                    except Exception as e:
                        logger.debug(f"Erreur {text_file}/ {e}")

    df = pd.DataFrame(rows)
    out_path = output_dir / f"{split_name}_raw.csv"
    df.to_csv(out_path, index=False)

    logger.info(
        f"conversion to csv of {split_name} / {len(df)} documents -> {out_path}"
    )
