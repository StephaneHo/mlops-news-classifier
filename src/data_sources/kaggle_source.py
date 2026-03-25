import logging
from pathlib import Path

from src.data_sources.base import DataSource


logger = logging.getLogger(__name__)


class KaggleDataSource(DataSource):
    def download(self, output_dir: Path) -> Path:
        try:
            from kaggle.api.kaggle_api_extended import KaggleApi
        except ImportError:
            raise ImportError(
                "Installer kaggle en tant que dépendance optionnelle (voir le README)"
            )

        api = KaggleApi()
        api.authenticate()

        # parents=True => créer les dossiers parents si nécessaire
        # exist_ok=True ne lève pas d'erreur si le dossier existe déjà
        output_dir.mkdir(parents=True, exist_ok=True)

        logger.info("Téléchargement depuis Kaggle")

        api.dataset_download_files(
            "au1206/20-newsgroup-original", path=output_dir, unzip=True
        )

        logger.info("Téléchargement terminé")
        return output_dir
