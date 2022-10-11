FROM python:alpine

WORKDIR /app

COPY . .

CMD ["python", "ping.py"]
