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
    first_day_num, last_day_num = calendar.monthrange(year_num, month_num)
    return date(day.year, day.month, first_day_num), date(day.year, day.month, last_day_num)

def months_ago(num_months, day=None):
    day = default_today(day)
    month_num = (day.month - num_months)
    year_num = day.year

    while month_num < 1 or month_num > 12:
        if month_num < 1:
            year_num -= 1
            month_num += 12
        else:
            year_num += 1
            month_num -= 12

    try:
        ret_date = day.replace(year=year_num, month=month_num)
    except ValueError:
        _, last_day = calendar.monthrange(year_num, month_num)
        ret_date = date(year_num, month_num, last_day)
    return ret_date

def months_ahead(num_months, day=None):
    return months_ago(-num_months, day=day)

def get_quarter_from_day(day):
    month_num = day.month
    quarter_num = (month_num - 1) / 3

    new_years_day = day.replace(day=1, month=1)
    start_date = months_ahead((quarter_num * 3), new_years_day)
    end_date = months_ahead(((quarter_num + 1) * 3), new_years_day)
    # Make it non-inclusive
    end_date -= timedelta(days=1)

    return start_date, end_date

def quarters_ago(num_quarters, day=None):
    day = default_today(day)
    return months_ago(num_quarters*3, day=day)
