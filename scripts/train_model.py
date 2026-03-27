import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.model.train import train

train(
    train_path=Path("data/processed/train_clean.csv"),
    test_path=Path("data/processed/test_clean.csv"),
    model_output=Path("models/news_classifier.pkl"),
)
