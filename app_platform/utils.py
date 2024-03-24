from datetime import timedelta
from django.utils import timezone
def get_next_wednesday_date():
    today = timezone.localtime()
    days_until_wednesday = (2 - today.weekday()) % 7
    return today + timedelta(days=days_until_wednesday)


def get_previous_wednesday_date():
    today = timezone.localtime()
    days_to_substract = (today.weekday() - 2) % 7
    return today + timedelta(days=days_to_substract)
