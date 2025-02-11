FROM python:3.10-slim-buster

WORKDIR /app
COPY main.py .
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

CMD ["gunicorn", "-w", "1", "main:app"]
