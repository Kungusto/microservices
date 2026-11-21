FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -e requirements.txt

COPY src/ ./src/

CMD ["python", "-m", "src.setup"]