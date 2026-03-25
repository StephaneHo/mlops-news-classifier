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