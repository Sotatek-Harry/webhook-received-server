FROM python:3.10-slim
WORKDIR /app

RUN apt-get update
RUN python3.10 -m pip install --upgrade pip && \
  python3.10 -m pip install poetry

COPY . /app

RUN poetry install --no-interaction

CMD poetry run uvicorn main:app --host 0.0.0.0
