import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
import nltk
import logging

nltk.download("stopwords")
# nécessaire pour que le lemmatizer puisse fonctionner
nltk.download("wordnet")

STOPWORDS = set(stopwords.words("english"))
LEMMATIZER = WordNetLemmatizer()

logger = logging.getLogger(__name__)


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    words = text.split()

    words = [w for w in words if w not in STOPWORDS]
    words = [LEMMATIZER.lemmatize(w) for w in words]

    return " ".join(words)


def preprocess_dataset(input_path, output_path):
    try:
        df = pd.read_csv(input_path)
    except Exception as e:
        logger.error(f"Erreur lecture fichier {e}")
        raise
    df["text"] = df["text"].apply(clean_text)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Datset prétraité sauvegardé dans {output_path}")
