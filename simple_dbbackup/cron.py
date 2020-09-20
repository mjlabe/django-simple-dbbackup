from django.conf import settings
from django.core.management import call_command
from django.utils import timezone
from django_cron import CronJobBase, Schedule


class DailyBackup(CronJobBase):
    if settings.DAILY_BACKUP_TIMES:
        RUN_AT_TIMES = [i for i in settings.DAILY_BACKUP_TIMES.split(",")]

        schedule = Schedule(run_at_times=RUN_AT_TIMES)
        code = 'simple_backup.daily_cron_job'    # a unique code

    def do(self):
        call_command(
            'dbbackup', '--clean')

        call_command(
            'mediabackup', '--clean')

        print('Daily Backup Complete')


class WeeklyBackup(CronJobBase):
    date_times = {}
    times = []

    if settings.WEEKLY_BACKUP_DATE_TIMES:
        weekly = [i.split(" ") for i in settings.WEEKLY_BACKUP_DATE_TIMES]

        for k, v in weekly:
            date_times[k.lower()] = v
            times.append(v)

        RUN_AT_TIMES = times

        schedule = Schedule(run_at_times=RUN_AT_TIMES)
        code = 'simple_backup.weekly_cron_job'    # a unique code

    def do(self):
        now = timezone.now()
        day = now.strftime("%a")
        time = now.strftime('%h:%m:%s')

        if day.lower() in self.date_times.keys():
            if self.date_times[day] >= time:
                call_command(
                    'dbbackup', '--clean')

                call_command(
                    'mediabackup', '--clean')

                print('Weekly Backup Complete')
