FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Render uses PORT env var, but default to 10000
EXPOSE 10000

# Use shell form to allow env var substitution, or hardcode 10000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]