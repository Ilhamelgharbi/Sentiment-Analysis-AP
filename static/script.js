// Additional JavaScript functionality for SentimentAI

// Demo text examples
const demoTexts = [
    "I absolutely love this new product! It exceeded all my expectations and the customer service was fantastic.",
    "This movie is terrible. I wasted my time and money. The plot was confusing and the acting was awful.",
    "The weather today is okay, nothing special but not bad either.",
    "Thank you so much for your help! You've been incredibly supportive and I really appreciate it.",
    "I'm disappointed with the delayed delivery. This is the third time this has happened.",
    "This restaurant serves amazing food! The flavors are incredible and the atmosphere is perfect.",
    "I feel frustrated with the poor customer service. Nobody seems to care about solving my problem."
];

// Add demo text functionality
function loadDemoText() {
    const textInput = document.getElementById('textInput');
    const randomText = demoTexts[Math.floor(Math.random() * demoTexts.length)];
    textInput.value = randomText;
    
    // Trigger character count update
    const event = new Event('input');
    textInput.dispatchEvent(event);
}

// Add demo button to the page
document.addEventListener('DOMContentLoaded', function() {
    const formGroup = document.querySelector('.form-group');
    const demoButton = document.createElement('button');
    demoButton.type = 'button';
    demoButton.className = 'demo-button';
    demoButton.innerHTML = '🎲 Try Demo Text';
    demoButton.onclick = loadDemoText;
    
    // Add demo button styles
    const style = document.createElement('style');
    style.textContent = `
        .demo-button {
            background: #f3f4f6;
            color: #374151;
            border: 1px solid #d1d5db;
            padding: 0.5rem 1rem;
            border-radius: 0.375rem;
            font-size: 0.875rem;
            cursor: pointer;
            margin-top: 0.5rem;
            transition: all 0.2s ease;
        }
        .demo-button:hover {
            background: #e5e7eb;
            border-color: #9ca3af;
        }
        .character-count {
            margin-top: 0.5rem;
            text-align: right;
        }
    `;
    document.head.appendChild(style);
    
    // Insert demo button after textarea
    const textarea = document.getElementById('textInput');
    textarea.parentNode.insertBefore(demoButton, textarea.nextSibling);
});

// Enhanced error handling
window.addEventListener('error', function(e) {
    console.error('Application error:', e.error);
});

// Performance monitoring
const startTime = performance.now();
window.addEventListener('load', function() {
    const loadTime = performance.now() - startTime;
    console.log(`Page loaded in ${loadTime.toFixed(2)}ms`);
});

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + Enter to analyze
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        e.preventDefault();
        const analyzeBtn = document.getElementById('analyzeBtn');
        if (!analyzeBtn.disabled) {
            analyzeSentiment();
        }
    }
    
    // Escape to clear text
    if (e.key === 'Escape') {
        const textInput = document.getElementById('textInput');
        if (document.activeElement === textInput) {
            textInput.value = '';
            const event = new Event('input');
            textInput.dispatchEvent(event);
        }
    }
});

// Add keyboard shortcut hints
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.sentiment-form');
    const shortcutHint = document.createElement('div');
    shortcutHint.className = 'shortcut-hints';
    shortcutHint.innerHTML = `
        <small style="color: #6b7280; margin-top: 0.5rem; display: block;">
            💡 Shortcuts: <kbd>Ctrl+Enter</kbd> to analyze, <kbd>Esc</kbd> to clear
        </small>
    `;
    
    // Add kbd styles
    const style = document.createElement('style');
    style.textContent = `
        kbd {
            background: #f3f4f6;
            border: 1px solid #d1d5db;
            border-radius: 0.25rem;
            padding: 0.1rem 0.3rem;
            font-size: 0.75rem;
            font-family: monospace;
        }
    `;
    document.head.appendChild(style);
    
    form.appendChild(shortcutHint);
});

// Analytics placeholder (you can integrate with Google Analytics or other services)
function trackAnalysis(sentiment, confidence) {
    // Example: gtag('event', 'sentiment_analysis', { sentiment, confidence });
    console.log(`Analysis tracked: ${sentiment} (${confidence}%)`);
}

// Export functions for potential external use
window.SentimentAI = {
    analyzeSentiment,
    loadDemoText,
    trackAnalysis
};