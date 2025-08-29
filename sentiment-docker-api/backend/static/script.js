// Simple Sentiment Analysis App

async function analyzeSentiment() {
    const textInput = document.getElementById('textInput');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const loading = document.getElementById('loading');
    const resultSection = document.getElementById('resultSection');
    const errorDiv = document.getElementById('error');
    
    const text = textInput.value.trim();
    
    if (!text) {
        showError('Please enter some text to analyze');
        return;
    }
    
    // Show loading
    analyzeBtn.disabled = true;
    analyzeBtn.textContent = 'Analyzing...';
    hideAll();
    loading.style.display = 'block';
    
    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: text })
        });
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Analysis failed');
        }
        
        const result = await response.json();
        showResult(result);
        
    } catch (error) {
        showError(error.message || 'Something went wrong');
    } finally {
        analyzeBtn.disabled = false;
        analyzeBtn.textContent = 'Analyze Sentiment';
        loading.style.display = 'none';
    }
}

function showResult(result) {
    hideAll();
    
    document.getElementById('sentimentBadge').textContent = `${result.sentiment} Sentiment`;
    document.getElementById('sentimentBadge').className = `sentiment-badge ${result.sentiment.toLowerCase()}`;
    document.getElementById('jsonOutput').textContent = JSON.stringify(result, null, 2);
    
    document.getElementById('resultSection').style.display = 'block';
}

function showError(message) {
    hideAll();
    document.getElementById('errorMessage').textContent = message;
    document.getElementById('error').style.display = 'block';
}

function hideAll() {
    document.getElementById('resultSection').style.display = 'none';
    document.getElementById('loading').style.display = 'none';
    document.getElementById('error').style.display = 'none';
}