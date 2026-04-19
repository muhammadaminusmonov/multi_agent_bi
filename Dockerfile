FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the 'app' directory into the container's '/app' directory.
# The structure becomes: /app/app/
COPY ./app ./app

EXPOSE 8000

# The CMD should point to the 'app' module inside the 'app' folder.
# The correct path is 'app.main:app'
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]