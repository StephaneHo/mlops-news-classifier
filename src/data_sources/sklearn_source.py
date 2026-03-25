import logging

import pandas as pd
from sklearn.datasets import fetch_20newsgroups

from src.data_sources.base import DataSource

logger = logging.getLogger(__name__)


class SklearnDataSource(DataSource):
    def download(self, output_dir):
        logger.info("Téléchargement via sklearn ...")
        output_dir.mkdir(parents=True, exist_ok=True)

        for split in ["train", "test"]:
            data = fetch_20newsgroups(
                subset=split,
                remove=(),
                shuffle=False,
            )

            df = pd.DataFrame(
                {
                    "text": data.data,
                    "label": [data.target_names[t] for t in data.target],
                }
            )

            out_path = output_dir / f"{split}_raw.csv"
            df.to_csv(out_path, index=False)

            logger.info(
                f"imported via sklearn {split}: {len(df)} documents -> {out_path}"
            )

        return output_dir
