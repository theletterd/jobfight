"""
"""

import datetime

from django.test import TestCase

from reporting import timeutil


class TimeutilTestCase(TestCase):

    def setUp(self):
        self.CURRENT_YEAR = 2012
        self.CURRENT_MONTH = 6
        self.CURRENT_DAY = 30
        self.today = datetime.date(year=self.CURRENT_YEAR, month=self.CURRENT_MONTH, day=self.CURRENT_DAY)

    def test_default_today(self):
        self.assertEqual(
                timeutil.default_today(),
                datetime.date.today(),
        )

        self.assertEqual(
                timeutil.default_today(day=self.today),
                self.today,
        )

    def test_weeks_ago(self):
        last_week = self.today - datetime.timedelta(days=7)
        self.assertEqual(
                timeutil.weeks_ago(1, self.today),
                last_week,
        )

        week_before = last_week - datetime.timedelta(days=7)
        self.assertEqual(
                timeutil.weeks_ago(2, self.today),
                week_before,
        )

        next_week = self.today + datetime.timedelta(days=7)
        self.assertEqual(
                timeutil.weeks_ago(-1, self.today),
                next_week,
        )

    def get_month_from_day(self):
        self.assertEqual(
                timeutil.get_month_from_day(datetime.date(2012, 12, 15)),
                (datetime.date(2012, 12, 1), datetime.date(2012, 12, 31))
        )
        self.assertEqual(
                timeutil.get_month_from_day(datetime.date(2012, 11, 30)),
                (datetime.date(2012, 11, 1), datetime.date(2012, 11, 30))
        )
        self.assertEqual(
                timeutil.get_month_from_day(datetime.date(2012, 11, 1)),
                (datetime.date(2012, 11, 1), datetime.date(2012, 11, 30))
        )
        self.assertEqual(
                timeutil.get_month_from_day(datetime.date(2012, 2, 4)),
                (datetime.date(2012, 2, 1), datetime.date(2012, 2, 29))
        )

    def test_months_ago(self):
        last_month = datetime.date(year=self.CURRENT_YEAR, month=self.CURRENT_MONTH - 1, day=self.CURRENT_DAY)
        self.assertEqual(
                timeutil.months_ago(1, self.today),
                last_month
        )

        next_month = datetime.date(year=self.CURRENT_YEAR, month=self.CURRENT_MONTH + 1, day=self.CURRENT_DAY)
        self.assertEqual(
                timeutil.months_ago(-1, self.today),
                next_month
        )

        new_years_day = datetime.date(year=self.CURRENT_YEAR, month=1, day=1)
        december_first = datetime.date(year=self.CURRENT_YEAR - 1, month=12, day=1)
        self.assertEqual(
                timeutil.months_ago(1, new_years_day),
                december_first
        )
        self.assertEqual(
                timeutil.months_ahead(1, december_first),
                new_years_day
        )

        december_first_year_before = datetime.date(year=self.CURRENT_YEAR - 2, month=12, day=1)
        self.assertEqual(
                timeutil.months_ago(13, new_years_day),
                december_first_year_before
        )
        self.assertEqual(
                timeutil.months_ahead(13, december_first_year_before),
                new_years_day
        )

    def test_quarters_ago(self):
        last_quarter = datetime.date(year=self.CURRENT_YEAR, month=self.CURRENT_MONTH - 3, day=self.CURRENT_DAY)
        self.assertEqual(
                timeutil.quarters_ago(1, self.today),
                last_quarter
        )

        next_quarter = datetime.date(year=self.CURRENT_YEAR, month=self.CURRENT_MONTH + 3, day=self.CURRENT_DAY)
        self.assertEqual(
                timeutil.quarters_ago(-1, self.today),
                next_quarter
        )

        new_years_day = datetime.date(year=self.CURRENT_YEAR, month=1, day=1)
        self.assertEqual(
                timeutil.quarters_ago(-1, new_years_day),
                datetime.date(year=self.CURRENT_YEAR, month=4, day=1)
        )
        self.assertEqual(
                timeutil.quarters_ago(1, new_years_day),
                datetime.date(year=self.CURRENT_YEAR - 1, month=10, day=1)
        )
        self.assertEqual(
                timeutil.quarters_ago(2, new_years_day),
                datetime.date(year=self.CURRENT_YEAR - 1, month=7, day=1)
        )
        self.assertEqual(
                timeutil.quarters_ago(3, new_years_day),
                datetime.date(year=self.CURRENT_YEAR - 1, month=4, day=1)
        )
