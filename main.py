from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS so external sites (like the evaluator) can call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Sentiment API is running"}
    
class Sentences(BaseModel):
    sentences: List[str]

positive_words = ["love", "good", "great", "awesome", "happy", "amazing"]
negative_words = ["bad", "sad", "terrible", "hate", "awful", "worst"]

def analyze_sentiment(sentence):
    text = sentence.lower()

    for word in positive_words:
        if word in text:
            return "happy"

    for word in negative_words:
        if word in text:
            return "sad"

    return "neutral"


@app.post("/sentiment")
def sentiment(data: Sentences):

    results = []

    for s in data.sentences:
        results.append({
            "sentence": s,
            "sentiment": analyze_sentiment(s)
        })

    return {"results": results}


