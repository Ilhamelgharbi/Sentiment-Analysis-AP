import gradio as gr
from transformers import pipeline

# Load model on CPU
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    device=-1
)

# Prediction function
def predict_sentiment(text):
    if not text.strip():
        return "Erreur : texte vide", 0.0
    result = sentiment_pipeline(text)[0]
    return result['label'], round(result['score'], 3)

# Gradio Interface
iface = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(lines=4, placeholder="Écris ton texte ici..."),
    outputs=["text", "number"],
    title="Mini UI Sentiment Analysis",
    description="Entrez un texte et obtenez son sentiment (POSITIVE / NEGATIVE) avec score."
)

# 🚀 Launch (Hugging Face will auto-run this)
iface.launch()
