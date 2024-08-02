from celery import Celery
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from datetime import timedelta

app = Celery('Core')

# Define the interval schedule
schedule, created = IntervalSchedule.objects.get_or_create(
    every=1,
    period=IntervalSchedule.DAYS
)

# Create or update the periodic task
PeriodicTask.objects.get_or_create(
    name='Check Budget End Dates and Check if Budget is still Valid',
    task='Core.tasks.check_budget_end_dates',
    defaults={
        'interval': schedule,
    }
)
