import gradio as gr
from transformers import pipeline

# Charger le modèle (CPU pour plus léger)
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    device=-1
)

# Fonction de prédiction
def predict_sentiment(text):
    if not text.strip():
        return "Erreur : texte vide", 0.0
    result = sentiment_pipeline(text)[0]
    return result['label'], round(result['score'], 3)

# Interface Gradio
iface = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(lines=4, placeholder="Écris ton texte ici..."),
    outputs=["text", "number"],
    title="Mini UI Sentiment Analysis",
    description="Entrez un texte et obtenez son sentiment (POSITIVE / NEGATIVE) avec score."
)

# Lancer en local
if __name__ == "__main__":
    iface.launch()  # share=True si tu veux un lien public temporaire
