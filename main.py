from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

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