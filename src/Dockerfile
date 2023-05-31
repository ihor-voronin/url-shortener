FROM python:3.9-slim-bullseye

WORKDIR /code/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get --yes install gcc python3-dev libpq-dev && \
    apt-get autoclean && apt-get autoremove && \
    apt-get clean

COPY . /code/

RUN pip install pipenv

RUN pipenv install --system --deploy --ignore-pipfile
RUN python -c "import fastapi; print(fastapi.__version__)"
RUN python -c "import alembic; print(alembic.__version__)"

EXPOSE 8000