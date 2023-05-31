import unittest
from helper.descriptors import StringValidator, ValidationMessages


class StringValidatorTestCase(unittest.TestCase):
    def test_valid_string(self):
        validator = StringValidator('mahnaz', 'fallah', '123456')
        self.assertEqual(validator.name, 'mahnaz')
        self.assertEqual(validator.last_name, 'fallah')
        self.assertEqual(validator.phone_number, '123456')


if __name__ == '__main__':
    unittest.main()