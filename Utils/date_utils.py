from datetime import date, timedelta


def get_yesterday():
    today = date.today()
    return today - timedelta(days=1)


def day_before():
    return get_yesterday() - timedelta(days=1)
