from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict_phishing

app = FastAPI()

class Data(BaseModel):
    email_text: str
    url: str

@app.post("/detect")
def detect(data: Data):
    return predict_phishing(data.email_text, data.url)
