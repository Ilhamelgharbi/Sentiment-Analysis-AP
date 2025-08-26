import pytest
from fastapi.testclient import TestClient
import sys
import os

# Add the backend directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../backend'))

from backend.main import app

client = TestClient(app)

class TestSentimentAPI:
    """Test suite for Sentiment Analysis API"""
    
    def test_health_endpoint(self):
        """Test the health check endpoint"""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "service" in data
        assert "version" in data
    
    def test_predict_positive_sentiment(self):
        """Test sentiment analysis with positive text"""
        response = client.post(
            "/predict",
            json={"text": "I love this product! It's amazing and wonderful."}
        )
        assert response.status_code == 200
        data = response.json()
        assert "label" in data
        assert "score" in data
        assert data["label"] in ["POSITIVE", "NEGATIVE"]
        assert 0 <= data["score"] <= 1
    
    def test_predict_negative_sentiment(self):
        """Test sentiment analysis with negative text"""
        response = client.post(
            "/predict",
            json={"text": "This is terrible and awful. I hate it completely."}
        )
        assert response.status_code == 200
        data = response.json()
        assert "label" in data
        assert "score" in data
        assert data["label"] in ["POSITIVE", "NEGATIVE"]
        assert 0 <= data["score"] <= 1
    
    def test_predict_empty_text(self):
        """Test sentiment analysis with empty text"""
        response = client.post(
            "/predict",
            json={"text": ""}
        )
        assert response.status_code == 400
        data = response.json()
        assert "detail" in data
        assert "empty" in data["detail"].lower()
    
    def test_predict_whitespace_text(self):
        """Test sentiment analysis with whitespace only"""
        response = client.post(
            "/predict",
            json={"text": "   "}
        )
        assert response.status_code == 400
    
    def test_predict_invalid_json(self):
        """Test with invalid JSON structure"""
        response = client.post(
            "/predict",
            json={"invalid_field": "some text"}
        )
        assert response.status_code == 422  # Validation error
    
    def test_home_page(self):
        """Test that the home page loads successfully"""
        response = client.get("/")
        assert response.status_code == 200
        assert "text/html" in response.headers.get("content-type", "")
    
    def test_docs_endpoint(self):
        """Test that Swagger docs are accessible"""
        response = client.get("/docs")
        assert response.status_code == 200
    
    def test_predict_long_text(self):
        """Test sentiment analysis with long text"""
        long_text = "This is a great product. " * 100  # 500+ characters
        response = client.post(
            "/predict",
            json={"text": long_text}
        )
        assert response.status_code == 200
        data = response.json()
        assert "label" in data
        assert "score" in data

# Benchmark test (bonus)
class TestPerformance:
    """Performance and benchmark tests"""
    
    def test_response_time(self):
        """Test that API responds within reasonable time"""
        import time
        
        start_time = time.time()
        response = client.post(
            "/predict",
            json={"text": "This is a test for response time measurement."}
        )
        end_time = time.time()
        
        assert response.status_code == 200
        response_time = end_time - start_time
        assert response_time < 5.0  # Should respond within 5 seconds
        
        print(f"Response time: {response_time:.3f} seconds")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
