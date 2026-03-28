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

    # si certaines cellules de text sont vides => NaN => pandas les lit comme float
    if not isinstance(text, str):
        return ""

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

    # On supprime les lignes vides avec text vide après nettoyage
    df = df[df["text"].str.strip() != ""]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Datset prétraité sauvegardé dans {output_path}")
