import datetime
import unittest

class TestDateTime(unittest.TestCase):

    def setUp(self):
        self.dateStr = '20210330'
        self.formatStr = '%Y%m%d'

        self.datetimeO = datetime.datetime.strptime(self.dateStr, self.formatStr)

    def tearDown(self):
        self.datetimeO = None

    def test_given_strptime_parses_a_string_into_a_datetime_object(self):
        self.assertEqual('datetime', type(self.datetimeO).__name__)

    def test_given_strptime_parses_a_string_into_a_datetime_object_day(self):
        self.assertEqual(30, self.datetimeO.day)

    def test_given_strptime_parses_a_string_into_a_datetime_object_month(self):
        self.assertEqual(3, self.datetimeO.month)

    def test_given_strptime_parses_a_string_into_a_datetime_object_year(self):
        self.assertEqual(2021, self.datetimeO.year)

    def test_given_strftime_builds_a_string_from_a_datetime_object(self):
        sut = datetime.datetime.strftime(self.datetimeO, '%m-%d-%Y')
        self.assertEqual('03-30-2021', sut)



