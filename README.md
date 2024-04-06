# Sentiment Analysis API

This API analyzes the sentiment of text inputs using a pre-trained model. It is built using FastAPI and Pydantic.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/mian312/Text-Sentiment-API.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```
2. Navigate to `http://localhost:8000/docs` in your browser to access the Swagger UI.
3. Use the `/sentiment` endpoint to analyze the sentiment of text inputs by providing a POST request with JSON data containing the text to be analyzed.

## Endpoint

- `/sentiment`: Analyzes the sentiment of the given text.

## Request Format

- Send a POST request to `/sentiment` endpoint with JSON data containing the text to be analyzed. The JSON should follow the format:
    ```json
    {
        "text": "Text to be analyzed"
    }
    ```

## Response Format

- Upon successful analysis, the API returns a JSON response with the following format:
    ```json
    {
        "status": "success",
        "data": "sentiment analysis result"
    }
    ```

- If an error occurs during analysis, the API returns a JSON response with the following format:
    ```json
    {
        "status": "error",
        "message": "error message"
    }
    ```

## Examples

### Request

```http
POST /sentiment HTTP/1.1
Host: localhost:8000
Content-Type: application/json

{
    "text": "I love this product! It's amazing!"
}

```
### Response

```json
{
  "status": "success",
  "data": {
    "result": "Positive",
    "score": {
      "neg": 0.0,
      "neu": 0.318,
      "pos": 0.682,
      "compound": 0.8619
    }
  }
}
```