import unittest

from src.foo import foo


class TestFoo(unittest.TestCase):

    def test_someFunc_from_a_module_in_its_own_sub_directory(self):
        self.assertEqual('eddie would go', foo.someFunction())

    def test_helloworld(self):
        self.assertTrue(True)

