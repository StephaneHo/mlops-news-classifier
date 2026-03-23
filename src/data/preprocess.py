import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd

nltk.download("stopwords")
# nécessaire pour que le lemmatizer puisse fonctionner
nltk.download("wordnet")


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = " ".join(
        [word for word in text.split() if word not in stopwords.words("english")]
    )
    # on ramène le texte à sa forme de base avec le lemmatizer
    lemmatizer = WordNetLemmatizer
    text = " ".join([lemmatizer.lematise(word) for word in text.split()])
    return text


def preprocess_dataset(input_path, output_path):
    df = pd.read_csv(input_path)
    df["text"] = df["text"].apply(clean_text)
    df.to_csv(output_path, index=False)
    print(f"Datset prétraité sauvegardé dans {output_path}")
