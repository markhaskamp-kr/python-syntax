import unittest

def argsType(*args):
    return type(args)

def min(*args):
    min = args[0]

    for num in args:
        if num < min:
            min = num

    return min

def kwargsType(**kwargs):
    return type(kwargs)

def concat(**kwargs):
    return f"{kwargs['a']}{kwargs['b']}" 

class TestVarArgs(unittest.TestCase):

    def test_given_varargs__then_type_is_tuple(self):
        self.assertEqual('tuple', argsType(1,2,3).__name__)

    def test_given_varargs(self):
        self.assertEqual(42, min(101, 102, 42, 103))
        self.assertEqual(42, min(42, 103))

    def test_given_kwargs__then_type_is_dict(self):
        self.assertEqual('dict', kwargsType(foo='bar', baz=42).__name__)

    def test_given_kwargs(self):
        self.assertEqual('helloworld', concat(a='hello', b='world'))
