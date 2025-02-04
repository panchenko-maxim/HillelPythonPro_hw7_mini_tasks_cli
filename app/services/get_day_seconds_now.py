from datetime import datetime


def get_day_seconds_now() -> int:
    time_now = datetime.now()
    return time_now.hour * 3600 + time_now.minute * 60 + time_now.second