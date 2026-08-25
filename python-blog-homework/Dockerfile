FROM python:3.10.2-alpine3.15

WORKDIR /app

COPY scraper.py .

RUN pip install --no-cache-dir requests beautifulsoup4

CMD ["python", "scraper.py"]
