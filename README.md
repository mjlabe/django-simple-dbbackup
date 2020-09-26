# django-simple-dbbackup

A Django Database Backup solution for people who hate dealing with infrastructure.

## Setup

Create a file in the project root called `backup_settings.py` with the following settings:

```
from django_simple_dbbackup.settings import *


SECRET_KEY = '75nv75t8hgc780c4mg0hcmg0g0mr0ggthth0ghmc3tr'

DBBACKUP_CONNECTORS = {
    'default': {
        'USER': os.getenv('DATABASE_USER', None),
        'HOST': os.getenv('DATABASE_HOST', None),
    }
}

BACKUP_MEDIA = True

BACKUP_DAILY = ['02:00', '12:00']
BACKUP_WEEKLY = {'monday': '12:00', 'sunday': '12:00'}
BACKUP_WEEKLY_MONTHLY = {'1': '02:00', '15': '02:00'}
BACKUP_HEALTH_CHECK = 1
```

Set the following environment variables for your database:

```
DATABASE_USER
DATABASE_HOST
```

Mount `.pgpass` file to... TBD after I get the cron to run.

Run `make build` then `make run`
