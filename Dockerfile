FROM python:3.8-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/

RUN apt-get update \
    && apt-get install -y postgresql-client \
    && apt-get install -y cron \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . /code/

# Copy backup-cron file to the cron.d directory
COPY backup-cron /etc/cron.d/backup-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/backup-cron

# Apply cron job
RUN crontab /etc/cron.d/backup-cron

# Run the command on container startup
CMD ["cron", "-f"]
