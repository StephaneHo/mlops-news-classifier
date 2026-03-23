### Suivre les modèles et les expériences avec MLFlow
import mlflow
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split
import pandas as pd

mlflow.set_experiment("text_classification")


def train_and_log():
    with mlflow.start_run():
        df = pd.read_csv("data/processed/20_newsgroups_processed.csv")
        X_train, X_test, y_train, y_test = train_test_split(
            df["text"], df["target"], text_size=0.2, random_state=42
        )

        pipeline = Pipeline(
            [
                ("tfidf", TfidfVectorizer(max_features=10000)),
                ("clf", LogisticRegression()),
            ]
        )

        pipeline.fit(X_train, y_train)

        accuracy = pipeline.score(X_test, y_test)
        mlflow.log_metric("accuracy", accuracy)

        mlflow.sklearn.log_model(pipeline, "model")
