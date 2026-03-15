FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y tcpdump

WORKDIR /app

COPY server.py .

EXPOSE 5000

CMD ["python", "server.py"]