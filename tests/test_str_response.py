import unittest

from importlib.machinery import SourceFileLoader

str_response = SourceFileLoader(
    "str_response", "./str_response/__init__.py"
).load_module()


class TestStrResponse(unittest.TestCase):
    def test_str_response(self):
        value = str_response.get_str(1)
        self.assertEqual(value, "Success!")


if __name__ == '__main__':
    unittest.main()
