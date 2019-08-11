import unittest

from mylib.mypack import func2

class AnotherModuleTests(unittest.TestCase):
    def test_func2(self):
        expected = "func2"
        actual = func2("test_a", test_b="test_c")
        self.assertEqual(expected, actual)