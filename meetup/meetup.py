from calendar import Calendar
from datetime import date, timedelta


class MeetupDayException(Exception):
    def __init__(self, value="Generic error"):
        self.value = value

    def __str__(self):
        return repr(self.value)

week_days = [
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday',
]


def meetup_day(year, month, week_day, slang):

    # parse the week_day
    week_day = week_day.lower()
    try:
        week_day_index = week_days.index(week_day)

        slang = slang.lower()

        if slang == 'teenth':
            return meetup_day_teenth(year, month, week_day_index)
        else:
            cal = Calendar(0).monthdayscalendar(year, month)
            if slang == 'last':
                return meetup_day_last(year, month, week_day_index, cal)
            elif slang == '1st':
                return meetup_day_apearence(year, month, week_day_index,
                                            0, cal)
            elif slang == '2nd':
                return meetup_day_apearence(year, month, week_day_index,
                                            1, cal)
            elif slang == '3rd':
                return meetup_day_apearence(year, month, week_day_index,
                                            2, cal)
            elif slang == '4th':
                return meetup_day_apearence(year, month, week_day_index,
                                            3, cal)
            elif slang == '5th':
                return meetup_day_apearence(year, month, week_day_index,
                                            4, cal)
    except:
        pass

    raise MeetupDayException()


def meetup_day_teenth(year, month, week_day_index):
    # get the first teenth and go the weekday
    tmp_date = date(year, month, 13)
    tmp_date_wd = tmp_date.weekday()
    if tmp_date_wd > week_day_index:
        week_day_index = week_day_index + 7

    return tmp_date + timedelta(days=week_day_index - tmp_date_wd)


def meetup_day_last(year, month, week_day_index, cal):
    # check if in the last week the day is present,
    # if not take the second last week
    day = cal[-1][week_day_index]
    if day == 0:
        day = cal[-2][week_day_index]

    return date(year, month, day)


def meetup_day_apearence(year, month, week_day_index, apearence, cal):
    day = cal[0][week_day_index]
    if day == 0:
        day = cal[apearence + 1][week_day_index]
    else:
        day = cal[apearence][week_day_index]
    if day != 0:
        return date(year, month, day)
    else:
        raise MeetupDayException
