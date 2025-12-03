# Use official Python slim image
FROM python:3.11-slim

# Prevent Python from writing pyc files & enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Upgrade pip and install build tools
RUN pip install --upgrade pip wheel setuptools

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port 8000 for Gunicorn
EXPOSE 8000

# Run Gunicorn to serve the app
CMD ["gunicorn", "alx_project_nexus.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
