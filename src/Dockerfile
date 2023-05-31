FROM python:3.9-slim-bullseye as code_base

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /src

COPY ./Pipfile .
COPY ./Pipfile.lock .

RUN apt-get update && \
    apt-get --yes install gcc python3-dev libpq-dev && \
    apt-get autoclean && apt-get autoremove && \
    apt-get clean

RUN pip install --user pipenv

ENV PIPENV_VENV_IN_PROJECT=1

RUN /root/.local/bin/pipenv sync

RUN ./.venv/bin/python -c "import fastapi; print(fastapi.__version__)"

COPY . .