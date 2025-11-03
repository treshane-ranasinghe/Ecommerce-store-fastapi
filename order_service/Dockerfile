# ProductService/Dockerfile (same template for others)
FROM python:3.13-slim

# avoid buffering in logs
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# install build deps for some packages (optional)
RUN apt-get update \
  && apt-get install -y build-essential libpq-dev --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy app code
COPY . .

# expose port (informational; binding done by docker-compose)
EXPOSE 8000

# dev mode with auto-reload
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
