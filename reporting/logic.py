from collections import defaultdict
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

def get_matrix(report_data_type, report_range_type, **filter_kwargs):
    matrix_args = report_data_type

    report_range_dict = report_range_type
    range_function = report_range_dict['resolution']['range_function']
    subtract_function = report_range_dict['resolution']['subtract_function']
    subtract_arg = report_range_dict['subtract_arg']

    # This is all a little intense. All we're doing is figuring out a) a unit
    # of time to go back (subtract_func), b) how much of that unit to go back
    # (subtract_arg), and c) the range to derive from that new date
    # (range_function)
    start_date, end_date = range_function(subtract_function(subtract_arg))
    matrix_args['start_date'] = start_date
    matrix_args['end_date'] = end_date
    matrix_args.update(filter_kwargs)

    return matrix_for_daterange(**matrix_args)
