"""
C'est l'API Rest avec les endpoints
"""

import logging
from typing import List


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ModelService:
    def __init__(self):
        self.model = None
        self.target_names: List[str] = []
        self.model_info: dict = {}

    def load(self):
        try:
            self.model = load_lastest_production_model()
            self.target_names = load_target_names()
            self.model_info = {"status": "loaded", "categories": self.target_names}
            logger.info("Modèle chargé !")
        except Exception as e:
            logger.error("Erreur chargement du modèle : ", {e})
