import sys
import unittest


def divider(m, n):
    val = m / n
    return val

class TestExceptions(unittest.TestCase):

    def test_given_divider__when_dividing_by_0__then_throw_ZeroDivisionError(self):
        with self.assertRaises(ZeroDivisionError):
            divider(12, 0)

    def test_given_exc_info__then_returns_tuple(self):
        try:
            divider(12, 0)

        except:
            info = sys.exc_info()
            self.assertEqual('tuple', type(info).__name__)

    def test_given_exc_info__then_returns_tuple_of_length_3(self):
        try:
            divider(12, 0)

        except:
            info = sys.exc_info()
            self.assertEqual(3, len(info))

    def test_given_exc_info__then_returns_tuple_first_element_is_class_object_of_type_of_error(self):
        try:
            divider(12, 0)

        except:
            info = sys.exc_info()
            self.assertEqual('ZeroDivisionError', info[0].__name__)

    def test_given_exc_info__then_returns_tuple_second_element_is_object_of_type_ZeroDivisionError(self):
        try:
            divider(12, 0)

        except:
            info = sys.exc_info()
            self.assertEqual("ZeroDivisionError", type(info[1]).__name__)

    def test_given_exc_info__then_returns_tuple_third_element_is_object_of_type_traceback(self):
        try:
            divider(12, 0)

        except:
            info = sys.exc_info()
            self.assertEqual('traceback', type(info[2]).__name__)

