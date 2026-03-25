from pathlib import Path


class DataSource:
    """
    C'est l'interface pour la source de données
    """

    def download(self, output_dir: Path) -> Path:
        raise NotImplementedError
