from django.conf import settings
from django.core.management import call_command
from django.utils import timezone
from django_cron import CronJobBase, Schedule


def db_backup(clean=False):
    if clean:
        call_command('dbbackup', '--clean')
    else:
        call_command('dbbackup')


def media_backup(clean=False):
    if clean:
        call_command('mediabackup', '--clean')
    else:
        call_command('mediabackup')


class DailyBackup(CronJobBase):
    if settings.BACKUP_DAILY:
        schedule = Schedule(run_at_times=settings.BACKUP_DAILY)
        code = 'simple_backup.daily_cron_job'    # a unique code

    def do(self):
        print('Daily Backup Start')

        db_backup(settings.BACKUP_CLEAN)

        if settings.BACKUP_MEDIA:
            media_backup(settings.BACKUP_CLEAN)

        print('Daily Backup Complete')


class WeeklyBackup(CronJobBase):
    if settings.BACKUP_WEEKLY:
        schedule = Schedule(run_at_times=settings.BACKUP_WEEKLY.values())
        code = 'simple_backup.weekly_cron_job'    # a unique code

    def do(self):
        now = timezone.now()
        day = now.strftime("%a")
        time = now.strftime('%h:%m')

        if day.lower() in settings.BACKUP_WEEKLY.keys():
            if time >= settings.BACKUP_WEEKLY[day.lower()]:
                print('Weekly Backup Start')

                db_backup(settings.BACKUP_CLEAN)

                if settings.BACKUP_MEDIA:
                    media_backup(settings.BACKUP_CLEAN)

                print('Weekly Backup Complete')


class MonthlyBackup(CronJobBase):
    if settings.BACKUP_MONTHLY:
        schedule = Schedule(run_at_times=settings.BACKUP_MONTHLY.values())
        code = 'simple_backup.monthly_cron_job'    # a unique code

    def do(self):
        now = timezone.now()
        day = str(now.day)
        time = now.strftime('%h:%m')

        if day in settings.BACKUP_MONTHLY.keys():
            if time >= settings.BACKUP_MONTHLY[day]:
                print('Monthly Backup Start')

                db_backup(settings.BACKUP_CLEAN)

                if settings.BACKUP_MEDIA:
                    media_backup(settings.BACKUP_CLEAN)

                print('Monthly Backup Complete')


class HealthCheck(CronJobBase):
    if settings.BACKUP_HEALTH_CHECK:
        schedule = Schedule(run_every_mins=settings.BACKUP_HEALTH_CHECK)
        code = 'simple_backup.health_cron_job'    # a unique code

    def do(self):
        print('Health Check OK')
