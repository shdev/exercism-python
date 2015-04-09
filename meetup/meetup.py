import calendar
from datetime import date, timedelta


class MeetupDayException(Exception):
    def __init__(self, value="Generic error"):
        self.value = value

    def __str__(self):
        return repr(self.value)

week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',
             'saturday', 'sunday', ]


def meetup_day(year, month, week_day, slang):

    week_day = week_day.lower()

    try:

        week_day_index = week_days.index(week_day)

        slang = slang.lower()

        start_days = {
            'teenth': 13,
            '1st': 1,
            '2nd': 8,
            '3rd': 15,
            '4th': 22,
            '5th': 29,
            'last': calendar.monthrange(year, month)[1] - 6,
        }

        return meetup_day_teenth(year, month, week_day_index,
                                 start_days[slang])
    except:
        pass

    raise MeetupDayException()


def meetup_day_teenth(year, month, week_day_index, start_day):
    # get the first teenth and go the weekday
    tmp_date = date(year, month, start_day)
    tmp_date_wd = tmp_date.weekday()
    if tmp_date_wd > week_day_index:
        week_day_index = week_day_index + 7

    return tmp_date + timedelta(days=week_day_index - tmp_date_wd)
