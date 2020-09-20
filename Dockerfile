FROM python:3.8-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code
RUN apt-get update \
    && apt-get install -y postgresql-client \
    && pip install --upgrade pip

COPY requirements.txt /code/

COPY . /code/

# Start uWSGI
CMD ["cron"]