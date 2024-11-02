from dagster import ScheduleDefinition
from ..jobs import trip_update_job
from ..jobs import weekly_update_job

trip_update_schedule = ScheduleDefinition(
    job=trip_update_job,
    cron_schedule="0 0 5 * *",  # każdego 5-go dnia miesiąca o północy
)

weekly_update_schedule = ScheduleDefinition(
    job=weekly_update_job,
    cron_schedule="0 0 * * 1", # każdy poniedziałek o północy
)
