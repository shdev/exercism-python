from datetime import timedelta


def add_gigasecond(the_date):
    return the_date + timedelta(seconds=10**9)
