FROM python:3.11.4-bookworm

RUN pip install --upgrade pip && pip install poetry==1.5

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --only main

COPY . .

EXPOSE 8000
CMD uvicorn main:app --host 0.0.0.0 --port 8000