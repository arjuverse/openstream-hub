FROM python:3.12-slim

WORKDIR /app

# Install system dependencies required for building python packages and PostgreSQL support
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt psycopg2-binary

# Copy backend source code
COPY . .

EXPOSE 8000

CMD ["uvicorn", "openstream.main:app", "--host", "0.0.0.0", "--port", "8000"]
