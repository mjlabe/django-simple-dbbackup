from django.conf import settings
from django.core.management import call_command
from django.utils import timezone
from django_cron import CronJobBase, Schedule


class DailyBackup(CronJobBase):
    if settings.DAILY_BACKUP:
        schedule = Schedule(run_at_times=settings.DAILY_BACKUP)
        code = 'simple_backup.daily_cron_job'    # a unique code

    def do(self):
        call_command(
            'dbbackup', '--clean')

        call_command(
            'mediabackup', '--clean')

        print('Daily Backup Complete')


class WeeklyBackup(CronJobBase):
    if settings.WEEKLY_BACKUP:
        schedule = Schedule(run_at_times=settings.WEEKLY_BACKUP.values())
        code = 'simple_backup.weekly_cron_job'    # a unique code

    def do(self):
        now = timezone.now()
        day = now.strftime("%a")
        time = now.strftime('%h:%m')

        if day.lower() in settings.WEEKLY_BACKUP.keys():
            if time >= settings.WEEKLY_BACKUP[day.lower()]:
                call_command(
                    'dbbackup', '--clean')

                call_command(
                    'mediabackup', '--clean')

                print('Weekly Backup Complete')


class MonthlyBackup(CronJobBase):
    if settings.MONTHLY_BACKUP:
        schedule = Schedule(run_at_times=settings.MONTHLY_BACKUP.values())
        code = 'simple_backup.monthly_cron_job'    # a unique code

    def do(self):
        now = timezone.now()
        day = str(now.day)
        time = now.strftime('%h:%m')

        if day in settings.MONTHLY_BACKUP.keys():
            if time >= settings.MONTHLY_BACKUP[day]:
                call_command(
                    'dbbackup', '--clean')

                call_command(
                    'mediabackup', '--clean')

                print('Monthly Backup Complete')
