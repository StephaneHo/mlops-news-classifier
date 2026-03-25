Utilise https://www.kaggle.com/datasets/au1206/20-newsgroup-original/data


kaggle datasets download -d au1206/20-newsgroup-original --unzip

=> Kaggle extrait un dossier avec une arborescence déjà définie par le dataset.

Exemple :

20news-bydate-train/
    alt.atheism/
    comp.graphics/
    ...
20news-bydate-test/
    alt.atheism/
    comp.graphics/
    ...

download_data.py
        ↓
choisit une source
        ↓
data_sources/*.py
        ↓
load_data()
        ↓
données brutes
        ↓
convert.py
        ↓
données propres

.
├── data/
│   ├── raw/               # Fichiers bruts (CSV, JSON, etc.)
│   ├── processed/         # Textes prétraités (tokenisés, vectorisés, etc.)
│   └── kaggle.json        # Clé API Kaggle
├── models/
│   ├── model.pkl          # Modèle sauvegardé (Scikit-learn ou PyTorch)
│   └── model_metadata.json
├── notebooks/
│   └── exploration.ipynb  # Exploration et analyse du dataset
├── src/
│   ├── data/
│   │   ├── download.py    # Téléchargement des données
│   │   └── preprocess.py  # Prétraitement du texte
│   ├── train/
│   │   └── train.py       # Entraînement du modèle
│   ├── registry/
│   │   └── save_to_s3.py  # Sauvegarde du modèle dans S3
│   ├── api/
│   │   ├── main.py        # API FastAPI pour la prédiction
│   │   └── requirements.txt
│   ├── dags/
│   │   └── retrain_pipeline.py  # Pipeline Airflow
│   └── mlflow/
│       └── tracking.py    # Suivi MLFlow
├── airflow/
│   └── Dockerfile         # Pour exécuter Airflow dans Docker
├── docker-compose.yml     # Pour orchestrer tous les services
├── .env                   # Variables d'environnement
└── README.md

scripts/
    download_data.py

src/
    data_sources/
        base.py
        kaggle_source.py
        sklearn_source.py
    data_processing/
        convert.py


# initailiser avec uv
    uv init
    uv venv
    source .venv\Scripts\activate
    uv add scikit-learn mlflow fastapi uvicorn pandas numpy
    normalement on devrait installer à part dans un autre venv apache-airflow
    mais là je l'installe avec les autres
    uv add apache-airflow

    installer kaggle en tant que dépendance optionnelle:
    uv add kaggle --optional kaggle



# lancer le projet
uv run uvicorn src.api.main:app --reload

# training
uv run python src/model/train.py