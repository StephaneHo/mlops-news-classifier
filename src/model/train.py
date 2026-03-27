import logging
import mlflow
import mlflow.sklearn
import pandas as pd
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline
import joblib

logger = logging.getLogger(__name__)


def train(train_path: Path, test_path: Path, model_output: Path) -> None:
    # Chargement et nettoyage robsute

    train_df = pd.read_csv(train_path).dropna(subset=["text", "label"])
    test_df = pd.read_csv(test_path).dropna(subset=["text", "label"])

    X_train, y_train = train_df["text"], train_df["label"]
    X_test, y_test = test_df["text"], test_df["label"]

    # On devrait avoir un rapport 80 / 20
    logger.info(f"Train : {len(X_train)} | Test : {len(X_test)}")

    # Définition des hyperparamètres
    params = {
        "tfidf__max_features": 50000,
        "tfidf__ngram_range": (1, 2),
        "clf__C": 1.0,
        "clf__max_iter": 1000,
        "clf__solver": "lbfgs",
    }
    pipeline = Pipeline([("tfidf", TfidfVectorizer()), ("clf", LogisticRegression())])
    pipeline.set_params(**params)

    # 3 entrainement avec ML Flow
    mlflow.set_experiment("news-classifier")

    # active l'autologging (capture auto des paramètres de la pipeline)
    mlflow.sklearn.autolog(log_models=False)

    with mlflow.start_run(run_name="text_classification_run"):
        logger.info("Début de l'entrainement ...")
        pipeline.fit(X_train, y_train)

        # 4 Evaluation
        y_pred = pipeline.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

        # Métriques
        mlflow.log_metric("accuracy", acc)
        logger.info(f"Accuracy : {acc:.4f}")
        print(classification_report(y_test, y_pred))

        # Créer le dossier
        model_output.parent.mkdir(parents=True, exist_ok=True)

        # Sauvegarder la modèle en local pour accès rapide et débug et développement
        # Sert aussi de backup quand ML flow est down
        joblib.dump(pipeline, model_output)

        # Enregistre le modèle dans MLflow
        mlflow.sklearn.log_model(pipeline, "model")

        logger.info(f"Modèle sauvegardé : {model_output}")
