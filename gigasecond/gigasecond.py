import datetime


def add_gigasecond(moment: datetime) -> datetime:
    return moment + datetime.timedelta(seconds=1000000000)
