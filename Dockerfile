# Use official Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose Hugging Face's container port
EXPOSE 7860

# Run the server
CMD ["python", "app.py"]
