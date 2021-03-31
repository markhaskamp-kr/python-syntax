import unittest

class TestDict(unittest.TestCase):

    def setUp(self):
        self.d = {'foo':'one', 'bar':'two', 'baz':'three'}

    def tearDown(self):
        self.d = None


    def test_fetch_for_key__when_key_exists__then_return_value(self):
        self.assertEqual('one', self.d['foo'])

    def test_fetch_for_key__when_key_does_not_exist__then_throw_KeyError(self):
        with self.assertRaises(KeyError):
            self.d['abc']

    def test_given_get__when_key_exists__then_return_value(self):
        self.assertEqual('one', self.d.get('foo'))

    def test_given_get__when_key_does_not_exist__then_return_None(self):
        self.assertEqual(None, self.d.get('abc'))

