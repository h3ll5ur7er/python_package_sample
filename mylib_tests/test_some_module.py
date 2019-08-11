import unittest

from mylib import func1

class SomeModuleTests(unittest.TestCase):
    def test_func2(self):
        expected = "func1"
        actual = func1("test_a", test_b="test_c")
        self.assertEqual(expected, actual)