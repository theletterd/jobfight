from collections import defaultdict
from functools import partial

from reporting import models

def matrix_for_daterange(start_date, end_date, i_key, j_key, filters=None):
    if filters is None:
        filters = []

    status_values_query = models.StatusValue.objects
    for filter in filters:
        status_values_query = status_values_query.filter(filter)
    status_values_query.filter(date__gte=start_date)
    status_values_query.filter(date__lte=end_date)
    status_values = status_values_query.all()

    matrix = defaultdict(partial(defaultdict, int))
    for status_value in status_values:
        matrix[getattr(status_value, i_key)][getattr(status_value, j_key)] += status_value.value

    return matrix

