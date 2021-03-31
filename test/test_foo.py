import unittest

from src.foo import foo


class TestFoo(unittest.TestCase):

    def test_someFunc(self):
        self.assertEqual('eddie would go', foo.someFunction())

    def test_helloworld(self):
        self.assertTrue(True)

