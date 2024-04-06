from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from autocorrect import Speller

spell = Speller(lang='en')

def get_sentiment(text):
    """
    Analyzes the sentiment of a given text and returns the result and score.

    Args:
        text (str): The text to be analyzed.

    Returns:
        dict: A dictionary containing the result and score of the sentiment analysis.
            The 'result' key holds the sentiment result, which can be 'Positive', 'Negative', or 'Neutral'.
            The 'score' key holds a dictionary with sentiment scores, including 'compound', 'neg', 'neu', and 'pos'.
    """
    # Convert the text into a list to analyze it sentence by sentence
    Text = [str(text)] 
    # Spell check each sentence
    Sentence = [spell(i) for i in Text]  

    analyzer = SentimentIntensityAnalyzer()

    result = ''
    score = {}
    for i in Sentence:
        sentiment = analyzer.polarity_scores(i)
        score = sentiment
        if sentiment['compound'] >= 0.05:
            result = "Positive"
        elif sentiment['compound'] <= -0.05:
            result = "Negative"
        else:
            result = "Neutral"
    
    return {
        "result": result,
        "score": score
    }

# while True:
#     text = input("Enter your text: ")
#     if text == "exit":
#         break
#     result = get_sentiment(text)
#     print(result)