# https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker

FROM python:3

ARG BOOKIT_ENV

ENV BOOKIT_ENV=${BOOKIT_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=0.12.11

RUN pip install "poetry==$POETRY_VERSION"

RUN mkdir /code
WORKDIR /code

COPY poetry.lock pyproject.toml /code/
#Lets see if this is necessary first.
#RUN apt install libpq-dev python3-dev

RUN poetry config settings.virtualenvs.create false \
  && poetry install $(test "$BOOKIT_ENV" == production && echo "--no-dev") --no-interaction --no-ansi
COPY . /code/
