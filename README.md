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
# 1. Télécharger
python scripts/download_kaggle_data.py

# 2. Convertir en CSV
python scripts/build_csv.py

# 3. Prétraiter
python scripts/preprocess_data.py

# 4 Split data
        ↓
# 5. Entrainement du modèle
Utilisation d'Autolog : mlflow.sklearn.autolog() capture automatiquement les paramètres du TF-IDF, de la Logistic Regression.
Signature du modèle : L'ajout de la signature permet à MLflow de connaître le format attendu des données (colonnes, types), facilitant le déploiement en API.
Gestion des erreurs (Try/Except) : Le bloc with mlflow.start_run() est sécurisé pour garantir que la session se ferme proprement même en cas de crash.
Modularité : Extraction des hyperparamètres dans un dictionnaire pour plus de lisibilité.

# 6 Visualisation
Lancer l'interface dans un 2ème terminal
mlflow ui
Ouvrir **http://localhost:5000** 

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