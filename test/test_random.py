from random import randint, random ,seed
import time
import unittest


class TestRandom(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_given_random__then_generates_float_less_than_1(self):
        seed(int(time.time()))
        actual = random()

        self.assertTrue(actual < 1.0)

    def test_given_randint__then_generates_integers_from_arg1_inclusive_to_arg2_inclusive(self):
        min = None
        max = None
        arg1 = 0
        arg2 = 9
        rangeCount = 1000

        seed(int(time.time()))
        n = randint(arg1, arg2)
        min = n
        max = n

        for i in range(rangeCount - 1):
            n = randint(arg1, arg2)
            if n < min:
                min = n
            if n > max:
                max = n

        self.assertEqual(min, arg1)
        self.assertEqual(max, arg2)


