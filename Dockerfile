# Dockerfile for Google Extractor
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies for Playwright and PostgreSQL
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    gnupg \
    ca-certificates \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    librandr2 \
    libgbm1 \
    libasound2 \
    libpango-1.0-0 \
    libcairo2 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY extractor_platform/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright and chromium browser
RUN playwright install chromium --with-deps

# Copy project files
COPY extractor_platform /app/

# Collect static files
# RUN python manage.py collectstatic --no-input

# Expose port
EXPOSE 8000

# Default command: Run Gunicorn (though we might use a shell script)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]
