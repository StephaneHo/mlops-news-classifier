Utilise https://www.kaggle.com/datasets/au1206/20-newsgroup-original/data

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


# initailiser avec uv
    uv init
    uv venv
    source .venv\Scripts\activate
    uv add scikit-learn mlflow fastapi uvicorn pandas numpy
    normalement on devrait installer à part dans un autre venv apache-airflow
    mais là je l'installe avec les autres
    uv add apache-airflow



# lancer le projet
uv run uvicorn src.api.main:app --reload

# training
uv run python src/model/train.py