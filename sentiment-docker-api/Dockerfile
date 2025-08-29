# Use official Python lightweight image
FROM python:3.11-slim

# Set working directory
WORKDIR /app/backend

# Create cache directory with proper permissions
RUN mkdir -p /.cache && chmod 777 /.cache

# Copy requirements first to leverage caching
COPY ./backend/requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Install PyTorch (CPU version to save space) + Transformers
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu \
    && pip install --no-cache-dir transformers

# Pre-download the model to avoid runtime permission issues
#RUN python -c "from transformers import pipeline; pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')"

# Copy backend code
COPY ./backend/ /app/backend/

# Expose port 7860
EXPOSE 7860

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=7860

# Run FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
