FROM python:3.11-slim

WORKDIR /code

RUN apt-get update && apt-get -y install gcc

RUN pip install poetry
ADD pyproject.toml /code/
RUN poetry config installer.max-workers 10
RUN poetry install --no-root

COPY . /code/

