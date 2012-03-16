from collections import defaultdict
from datetime import timedelta
from functools import partial

from reporting import models

def matrix_for_daterange(start_date, end_date, i_key, j_key, **filter_kwargs):
    status_values_query = models.StatusValue.objects
    status_values_query = status_values_query.filter(**filter_kwargs)
    status_values_query = status_values_query.filter(date__gte=start_date)
    status_values_query = status_values_query.filter(date__lte=end_date)
    status_values = status_values_query.all()

    matrix = defaultdict(partial(defaultdict, int))
    for status_value in status_values:
        matrix[getattr(status_value, i_key)][getattr(status_value, j_key)] += status_value.value

    return matrix

def range_from_report_range_type(report_range_type):
    report_range_dict = report_range_type

    # This is all a little intense. All we're doing is figuring out a) a unit
    # of time to go back (subtract_func), b) how much of that unit to go back
    # (subtract_arg), and c) the range to derive from that new date
    # (range_function)
    range_function = report_range_dict['resolution']['range_function']
    subtract_function = report_range_dict['resolution']['subtract_function']
    subtract_arg = report_range_dict['subtract_arg']

    start_date, end_date = range_function(subtract_function(subtract_arg))
    return start_date, end_date

def pick_day_from_week(start_date, end_date):
    weekday_num = start_date.weekday()
    day_difference = weekday_num - 5

    return start_date - timedelta(days=day_difference)

def get_matrix(report_data_type, report_range_type, **filter_kwargs):
    matrix_args = report_data_type
    start_date, end_date = range_from_report_range_type(report_range_type)

    matrix_args['start_date'] = start_date
    matrix_args['end_date'] = end_date
    matrix_args.update(filter_kwargs)

    return matrix_for_daterange(**matrix_args)
