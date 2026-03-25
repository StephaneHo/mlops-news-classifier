import logging
from pathlib import Path
import pandas as pd

logger = logging.getLogger(__name__)


def convert_to_csv(raw_dir: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for split in ["train", "test"]:
        split_dir = raw_dir / f"20news-bydate-{split}"
        if not split_dir.exists():
            candidates = list(raw_dir.glob("*split"))
            if candidates:
                split_dir = candidates[0]
            else:
                logger.warning(f"{split} introuvable")
                continue
        rows = []
        for category_dir in sorted(split_dir.iterdir()):
            # si ce n'est pas un fichier, on passe
            if not category_dir.is_dir():
                continue

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
                        rows.append({"text": text, "'label": category})
                    except Exception as e:
                        logger.debug(f"Erreur {text_file}/ {e}")

            df = pd.DataFrame(rows)
            out_path = output_dir / f"{split}_raw.csv"
            df.to_csv(out_path, index=False)

            logger.info(
                f"conversion to csv of {split} / {len(df)} documents -> {out_path}"
            )
