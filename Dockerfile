FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Set the PYTHONPATH environment variable to include the working directory
ENV PYTHONPATH=/app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY ./app ./app

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application using the PORT environment variable provided by Render
CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT