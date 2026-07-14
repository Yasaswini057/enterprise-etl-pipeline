FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt stripe==15.3.0

COPY . ./
RUN mkdir -p logs data/raw data/processed

CMD ["python", "main.py"]
