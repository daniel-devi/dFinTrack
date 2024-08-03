from celery import Celery
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from datetime import timedelta

app = Celery('Core')

#* ---Define the interval schedule----

# Daily Schedule for Celery Workers
schedule_daily, created = IntervalSchedule.objects.get_or_create(
    every=1,
    period=IntervalSchedule.DAYS
)

# Every 5 Minutes Schedule for celery Worker
schedule_five_minutes, created = IntervalSchedule.objects.get_or_create(
    every=5,
    period=IntervalSchedule.MINUTES
)

#* --- Create or update the periodic task---

#? Budget Model Tasks

# celery beat for check_budget_end_dates_tasks
PeriodicTask.objects.get_or_create(
    name='Check Budget End Dates and Check if Budget is still Valid',
    task='Core.tasks.check_budget_end_dates',
    defaults={
        'interval': schedule_daily,
    }
)


# celery beat for check_budget_has_been_exceeded task
PeriodicTask.objects.get_or_create(
    name='Check Budget has been exceeded',
    task='Core.tasks.check_budget_has_been_exceeded',
    defaults={
        'interval': schedule_five_minutes,
    }
)


#? Financial Goal Tasks

# celery beat for check_financial_goal_end_dates_and_sends_reminder task
PeriodicTask.objects.get_or_create(
    name='Check Financial Goal End Dates and sends reminder',
    task='Core.tasks.check_financial_goal_end_dates_and_sends_reminder',
    defaults={
        'interval': schedule_daily,
    }
)


# celery beats for check_financial_goal_has_been_met task
PeriodicTask.objects.get_or_create(
    name='Check Financial Goal has been met',
    task='Core.tasks.check_financial_goals_has_been_met',
    defaults={
        'interval': schedule_five_minutes,
    }
)


# celery beats for check_financial_goal_end_dates task
PeriodicTask.objects.get_or_create(
    name='Check Financial Goal has end dates',
    task='Core.tasks.check_financial_goals_end_dates',
    defaults={
        'interval': schedule_daily,
    }
)


# celery beats for check_financial_goal_end_dates_and_sends_reminder task
"""
PeriodicTask.objects.get_or_create(
    name='Check Financial Goal has met',
    task='Core.tasks.check_financial_goals_has_been_met',
    defaults={
        'interval': schedule_five_minutes,
    }
)
"""