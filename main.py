from fastapi import FastAPI
from pydantic import BaseModel
from sentiment import get_sentiment

app = FastAPI()


class SentimentRequest(BaseModel):
    text: str


@app.post("/sentiment")
def analyze_sentiment(request: SentimentRequest):
    """
    Analyzes the sentiment of the given text.

    Parameters:
    - request: SentimentRequest object containing the text to be analyzed.

    Returns:
    - A dictionary with the following keys:
        - "status": The status of the sentiment analysis ("success" or "error").
        - "data": The sentiment analysis result if successful.
        - "message": The error message if an exception occurs.
    """
    try:
        data = get_sentiment(request.text)
        return {
            "status": "success",
            "data": data
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

