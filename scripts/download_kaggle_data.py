from pathlib import Path

from scripts.kaggle_source import KaggleDataSource


source = KaggleDataSource()
source.download(output_dir=Path("data/raw"))
