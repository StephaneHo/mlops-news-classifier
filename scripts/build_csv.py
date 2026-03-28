import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


from src.data_processing.convert import convert_to_csv

convert_to_csv(raw_dir=Path("data/raw"), output_dir=Path("data/processed"))
