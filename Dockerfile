FROM python:3.11

RUN mkdir ./app
WORKDIR /app

COPY ./app ./app
COPY ./pyproject.toml ./
COPY ./poetry.lock ./
COPY ./localhost+2-key.pem ./
COPY ./localhost+2.pem ./

RUN pip install poetry==1.2.2
RUN poetry config virtualenvs.create false
RUN poetry install

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--ssl-keyfile=./localhost+2-key.pem", "--ssl-certfile=./localhost+2.pem"]
