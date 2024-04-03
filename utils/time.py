from datetime import timedelta
from django.utils import timezone
from datetime import datetime


def get_next_wednesday_date() -> datetime:
    today = timezone.localtime()
    if today.weekday() == 2:
        return today

    days_until_wednesday = (2 - today.weekday() + 7) % 7
    return today + timedelta(days=days_until_wednesday)


def get_previous_wednesday_date() -> datetime:
    today = timezone.localtime()
    if today.weekday() == 2:
        return today - timedelta(days=7)

    days_to_substract = (today.weekday() - 2 + 7) % 7
    return today - timedelta(days=days_to_substract)
