from datetime import datetime, timedelta


def get_next_wednesday_date():
    today = datetime.today()
    days_until_wednesday = (2 - today.weekday()) % 7
    return today + timedelta(days=days_until_wednesday)
