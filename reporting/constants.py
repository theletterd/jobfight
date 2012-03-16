from functools import partial

from reporting import timeutil

class Resolution(object):
    WEEKLY = dict(
            range_function=timeutil.get_week_from_day,
            subtract_function=timeutil.weeks_ago,
    )

    MONTHLY = dict(
            range_function=timeutil.get_month_from_day,
            subtract_function=timeutil.months_ago,
    )

    QUARTERLY = dict(
            range_function=timeutil.get_quarter_from_day,
            subtract_function=timeutil.quarters_ago,
    )

class ReportRangeType(object):
    THIS_WEEK = dict(
            resolution=Resolution.WEEKLY,
            subtract_arg=0,
    )
    LAST_WEEK = dict(
            resolution=Resolution.WEEKLY,
            subtract_arg=1,
    )
    TWO_WEEKS_AGO = dict(
            resolution=Resolution.WEEKLY,
            subtract_arg=2,
    )

    THIS_MONTH = dict(
            resolution=Resolution.MONTHLY,
            subtract_arg=0,
    )
    LAST_MONTH = dict(
            resolution=Resolution.MONTHLY,
            subtract_arg=1,
    )
    TWO_MONTHS_AGO = dict(
            resolution=Resolution.MONTHLY,
            subtract_arg=2,
    )

    THIS_QUARTER = dict(
            resolution=Resolution.QUARTERLY,
            subtract_arg=0,
    )
    LAST_QUARTER = dict(
            resolution=Resolution.QUARTERLY,
            subtract_arg=1,
    )

    @classmethod
    def all_types(cls):
        # Hack to return all exposed values
        return [attr for attr in dir(cls) if not attr.startswith('_') and attr != 'all_types']


class ReportDataType(object):
    USER_STATUS = dict(
            i_key='user',
            j_key='status',
    )

    REC_STATUS = dict(
            i_key='req',
            j_key='status',
    )
