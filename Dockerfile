# Use official Python lightweight image
FROM python:3.11-slim

# Set working directory
WORKDIR /app/backend

# Copy requirements first to leverage caching
COPY backend/requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt
# Install PyTorch (CPU version to save space) + Transformers
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu \
    && pip install --no-cache-dir transformers

# Copy backend code
COPY backend/ /app/backend/

# Copy static folder
COPY static/ /app/static/
COPY tests/ /app/tests/

# Expose port 7860
EXPOSE 7860

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=7860

# Run FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
