import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


from src.preprocessing.text_cleaner import preprocess_dataset

preprocess_dataset(input_path=Path("data/raw/20"))
