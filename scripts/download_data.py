""" 
Télécharge le dataset Newsgroups depuis Kaggle et le convertit au bon format
"""

import pandas as pd
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

KAGGLE_DATASET = "au1206/20-newsgroup-original"
DEFAULT_KAGGLE = Path("/data")

def download_from_kaggle(output_dir: Path) -> Path:
    """
    Télécharge le dataset depuis Kaggle via l'API officielle
    On a besoin de configurer le kaggle.json 
    """
    
    try:
        import kaggle.api
    
    
    
