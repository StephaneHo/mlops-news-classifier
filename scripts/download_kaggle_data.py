from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


from src.data_sources.kaggle_source import KaggleDataSource


source = KaggleDataSource()
source.download(output_dir=Path("data/raw"))
