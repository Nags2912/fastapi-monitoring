# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy application files
COPY app.py requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt

# Expose FastAPI port
EXPOSE 8080

# Run FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
