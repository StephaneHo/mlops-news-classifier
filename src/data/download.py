from kaggle.api.kaggle_api_extended import KaggleApi


def download_kaggle_dataset(dataset, output_dir):
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset, path=output_dir, unzip=True)
    print(f"Dataset téléchargé dans {output_dir}")
