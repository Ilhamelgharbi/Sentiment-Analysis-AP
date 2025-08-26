from transformers import pipeline
import logging

logger = logging.getLogger(__name__)

try :
    sentiment_pipeline = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english",
        device=-1
    )
    logger.info("Sentiment analysis pipeline created successfully.")
except Exception as e :
    logger.error(f"Error creating sentiment analysis pipeline: {e}")

