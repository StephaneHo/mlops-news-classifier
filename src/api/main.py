### Pour envoyer un texte et recevoir une prédiction

from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# sert à charger un modèle déjà entrainé depuis un fichier
# le load permet de désérialiser un objet Python
model = joblib.load("models/model.pkl")


class TextRequest(BaseModel):
    text: str


@app.post("/predict")
async def predict(request: TextRequest):
    prediction = model.predict([request.text])[0]
    return {"prediction: ": str(prediction)}
