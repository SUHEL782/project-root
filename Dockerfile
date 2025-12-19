FROM python:3.11-slim

WORKDIR /task

RUN apt-get update && apt-get install -y bash coreutils \
    && pip install --no-cache-dir pytest \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN chmod +x run-tests.sh analyze_logs.sh

CMD ["./run-tests.sh"]

