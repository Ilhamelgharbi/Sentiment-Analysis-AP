# 🧠 SentimentAI - Professional Sentiment Analysis API

A FastAPI-based sentiment analysis microservice using Hugging Face's DistilBERT model for accurate emotion detection in text.

![Python](https://img.shields.io/badge/python-v3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0+-green.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🚀 Features

- **High Accuracy**: Uses `distilbert-base-uncased-finetuned-sst-2-english` model
- **Fast Processing**: Optimized for CPU inference
- **REST API**: Clean JSON input/output
- **Web Interface**: Beautiful HTML testing interface
- **Docker Ready**: Containerized for easy deployment
- **Error Handling**: Comprehensive error management
- **Interactive Docs**: Swagger UI at `/docs`

## 🏗️ Project Structure

```
sentiment-api/
├── backend/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── model.py             # HuggingFace model loader
│   ├── routers/
│   │   ├── __init__.py
│   │   └── sentiment.py     # API endpoints
│   └── templates/
│       └── index.html       # Web interface
├── static/
│   ├── style.css            # Styling
│   └── script.js            # Frontend logic
├── tests/
│   └── test_sentiment.py    # Unit tests
├── Dockerfile               # Container configuration
├── requirements.txt         # Dependencies
└── README.md               # This file
```

## 🔧 Installation & Usage

### Local Development

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd sentiment-api
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
cd backend
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

5. **Access the application**
- Web Interface: http://127.0.0.1:8000
- API Docs: http://127.0.0.1:8000/docs
- Health Check: http://127.0.0.1:8000/health

### Docker Deployment

1. **Build the image**
```bash
docker build -t sentiment-api .
```

2. **Run the container**
```bash
docker run -p 7860:7860 sentiment-api
```

3. **Access the application**
- Web Interface: http://localhost:7860
- API Docs: http://localhost:7860/docs

## 🔌 API Usage

### Predict Sentiment

**Endpoint:** `POST /predict`

**Request:**
```json
{
  "text": "I love this product! It's amazing."
}
```

**Response:**
```json
{
  "label": "POSITIVE",
  "score": 0.9998
}
```

### Health Check

**Endpoint:** `GET /health`

**Response:**
```json
{
  "status": "healthy",
  "service": "Sentiment Analysis API",
  "version": "1.0"
}
```

## 🧪 Testing

### Run Unit Tests
```bash
python -m pytest tests/ -v
```

### Test the API
```bash
# Test positive sentiment
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "I love this!"}'

# Test negative sentiment
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "This is terrible."}'
```

## 🌐 Deployment

### Hugging Face Spaces

1. Create a new Space on [Hugging Face Spaces](https://huggingface.co/spaces)
2. Choose "Docker" as the SDK
3. Upload your code with the Dockerfile
4. The app will be automatically deployed

**Live Demo:** [Your Hugging Face Space URL]

## 📊 Model Information

- **Model:** `distilbert-base-uncased-finetuned-sst-2-english`
- **Type:** Binary sentiment classification (POSITIVE/NEGATIVE)
- **Framework:** Transformers (Hugging Face)
- **Device:** CPU optimized
- **Accuracy:** ~91% on SST-2 dataset

## 🛠️ Technical Stack

- **Backend:** FastAPI 0.68.0+
- **ML Model:** Hugging Face Transformers
- **Frontend:** HTML5, CSS3, JavaScript
- **Containerization:** Docker
- **Python:** 3.11+

## 📈 Performance

- **Latency:** ~100-300ms per request
- **Throughput:** ~10-50 requests/second (CPU dependent)
- **Memory:** ~1GB RAM required

## 🔒 Error Handling

The API handles various error scenarios:

- **Empty text:** Returns 400 Bad Request
- **Model loading failure:** Returns 500 Internal Server Error
- **Processing errors:** Returns 500 with detailed error message

## 📝 Development Notes

### Adding New Features

1. **New endpoints:** Add to `backend/routers/`
2. **Frontend changes:** Modify `static/` files
3. **Tests:** Add to `tests/` directory

### Environment Variables

- `PORT`: Server port (default: 8000 locally, 7860 in Docker)
- `HOST`: Server host (default: 127.0.0.1)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for the DistilBERT model
- [FastAPI](https://fastapi.tiangolo.com/) for the excellent web framework
- [Docker](https://www.docker.com/) for containerization

---

**Built with ❤️ for the AI community**
