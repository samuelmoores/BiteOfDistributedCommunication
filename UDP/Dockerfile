FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

# Install tcpdump (required for the project – you must run it inside receivers)
RUN apt-get update && \
    apt-get install -y tcpdump && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy EVERY .py file (sender, receiver, and your anycast files if you combine both tasks)
COPY *.py .

