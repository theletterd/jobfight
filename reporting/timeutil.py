import calendar
from datetime import date
from datetime import timedelta

def default_today(day=None):
    if day is None:
        day = date.today()
    return day

def get_week_from_day(day):
    weekday = day.weekday()
    start_date = day + timedelta(days=(1 - weekday))
    end_date = day + timedelta(days=(7 - weekday))

    return start_date, end_date

def weeks_ago(num_weeks, day=None):
    day = default_today(day)
    return day - timedelta(weeks=num_weeks)

def get_month_from_day(day):
    day_of_month = day.day
    start_date = day + timedelta(days=(1 - day_of_month))

    month_num = (day.month + 1)
    year_num = day.year
    if month_num > 12:
        year_num += 1
    month_num %= 12
    end_date = date(year_num, month_num, 1)
    end_date -= timedelta(days=1)

    return start_date, end_date

def months_ago(num_months, day=None):
    day = default_today(day)
    month_num = (day.month - num_months)
    year_num = day.year
    while month_num < 1:
        month_num += 12
        year_num -= 1

    try:
        ret_date = day.replace(year=year_num, month=month_num)
    except ValueError:
        _, last_day = calendar.monthrange(year_num, month_num)
        ret_date = date(year_num, month_num, last_day)
    return ret_date
