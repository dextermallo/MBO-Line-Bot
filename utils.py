import datetime


def get_today():
    now = datetime.datetime.now()
    return f'{now.year}/{now.month}/{now.day}'
