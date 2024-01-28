from transformers import  pipeline

# Load the sentiment analysis pipeline

def init_sentiment_model():
    sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
    return sentiment_pipeline

# sentiment_pipeline = init_sentiment_model()

# def get_sentiment(text):
#     # Get sentiment
#     result = sentiment_pipeline(text)

#     return result[0]