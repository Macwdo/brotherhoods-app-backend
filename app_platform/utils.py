from datetime import datetime, timedelta, timezone


def get_next_wednesday_date():
    today = datetime.now(tz=timezone.utc)
    days_until_wednesday = (2 - today.weekday()) % 7
    return today + timedelta(days=days_until_wednesday)
