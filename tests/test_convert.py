from unittest import TestCase
from errors import incorrect_output, no_function_found, succeed


class TestConvert(TestCase):
    def test_convert(self):
        try:
            from conversion import convert
        except ImportError:
            self.assertFalse(no_function_found("convert"))

        celsius = [39.2, 36.5, 37.3, 37.8]
        result = convert(celsius)

        try:
            self.assertEqual(102.56, result[0])
            self.assertEqual(97.7, result[1])
            self.assertEqual(99.14, result[2])
            self.assertEqual(100.03999999999999, result[3])
            self.assertTrue(succeed("test cases passed"))
        except:
            self.assertFalse(incorrect_output("incorrect output returned"))