import datetime
import time
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

    def test_given_time_localtime_function__then_return_object_of_type_struct_time(self):
        self.assertEqual(type(time.localtime()).__name__, 'struct_time')

    def test_given_time__then_struct_time_attributes(self):
        t = time.localtime()
        self.assertTrue(t.tm_year > 2000 and t.tm_year < 3000)
        self.assertTrue(t.tm_mon >= 1 and t.tm_mon <= 12)
        self.assertTrue(t.tm_mday >= 1 and t.tm_mday <= 31)
        self.assertTrue(t.tm_hour >= 0 and t.tm_hour <= 23)
        self.assertTrue(t.tm_min >= 0 and t.tm_min <= 59)
        self.assertTrue(t.tm_sec >= 0 and t.tm_sec <= 61)

        sunday = 1480867613
        monday = 1480932000
        tSunday = time.localtime(sunday)
        tMonday = time.localtime(monday)
        self.assertEqual(0, tMonday.tm_wday)
        self.assertEqual(6, tSunday.tm_wday)

    def test_given_time_time_function__then_returns_seconds_since_the_epoch_as_a_float(self):
        self.assertEqual(type(time.time()).__name__, 'float')

