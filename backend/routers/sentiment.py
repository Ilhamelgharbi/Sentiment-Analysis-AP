from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from model import sentiment_pipeline

router = APIRouter()

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    label: str
    score: float

@router.post("/predict", response_model=SentimentResponse)
def predict_sentiment(request: SentimentRequest):
    if not request.text or request.text.strip() == "":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Text cannot be empty."
        )
    if sentiment_pipeline is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Sentiment model is not loaded."
        )

    try:
        result = sentiment_pipeline(request.text)[0]
        return SentimentResponse(label=result['label'], score=result['score'])
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing text: {str(e)}"
        )
