FROM python:3.12.10-slim

WORKDIR /app

COPY app/requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y build-essential \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get remove -y build-essential && apt-get autoremove -y

COPY app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
