import unittest
from unittest import TestCase
from unittest import mock

from ..main_cls import RomanNumeralConverter


class Test_RomanNumeralConverter(TestCase):

    def setUp(self):
        self.rmc = RomanNumeralConverter()


    @mock.patch('builtins.input', side_effect=['Cat', '10'])
    def test_after_non_numeral_input_followed_by_numeral_input_will_be_called_twice(self, input):
        self.rmc.get_user_input()
        self.assertEqual(input.call_count, 2)

    @mock.patch('builtins.input', side_effect=['10'])
    def test_numeral_string_input_will_return_integer_type(self, input):
        self.assertIsInstance(self.rmc.get_user_input(), int)

    @mock.patch('builtins.input', side_effect=['115'])
    def test_numeral_string_input_returned_as_integer_value(self, input):
        self.assertEqual(115, self.rmc.get_user_input())

    def test_split_number_into_digits_and_exponents_list(self):
        self.assertEqual([(100, 2), (10, 1) , (1, 0)], self.rmc.split_number_into_digits_and_exponent(111))
        self.assertEqual([(10, 1), (1, 0)], self.rmc.split_number_into_digits_and_exponent(11))
        self.assertEqual([(50, 1), (4, 0)], self.rmc.split_number_into_digits_and_exponent(54))
        self.assertEqual([(6, 0)], self.rmc.split_number_into_digits_and_exponent(6))
        self.assertEqual([(1000, 3), (400, 2), (80, 1), (9, 0)], self.rmc.split_number_into_digits_and_exponent(1489))
        self.assertEqual([(800, 2), (0, 1), (0, 0)], self.rmc.split_number_into_digits_and_exponent(800))

    def test_convert_first_digit_to_numeral_string(self):
        base = 1
        self.assertEqual('', self.rmc.convert_digit_from_base_to_numeral_string(0, base))
        self.assertEqual('I', self.rmc.convert_digit_from_base_to_numeral_string(1, base))
        self.assertEqual('II', self.rmc.convert_digit_from_base_to_numeral_string(2, base))
        self.assertEqual('III', self.rmc.convert_digit_from_base_to_numeral_string(3, base))
        self.assertEqual('IV', self.rmc.convert_digit_from_base_to_numeral_string(4, base))
        self.assertEqual('V', self.rmc.convert_digit_from_base_to_numeral_string(5, base))
        self.assertEqual('VI', self.rmc.convert_digit_from_base_to_numeral_string(6, base))
        self.assertEqual('VII', self.rmc.convert_digit_from_base_to_numeral_string(7, base))
        self.assertEqual('VIII', self.rmc.convert_digit_from_base_to_numeral_string(8, base))
        self.assertEqual('IX', self.rmc.convert_digit_from_base_to_numeral_string(9, base))

    def test_convert_second_digit_to_numeral_string(self):
        base = 10
        self.assertEqual('', self.rmc.convert_digit_from_base_to_numeral_string(0, base))
        self.assertEqual('X', self.rmc.convert_digit_from_base_to_numeral_string(10, base))
        self.assertEqual('XX', self.rmc.convert_digit_from_base_to_numeral_string(20, base))
        self.assertEqual('XXX', self.rmc.convert_digit_from_base_to_numeral_string(30, base))
        self.assertEqual('XL', self.rmc.convert_digit_from_base_to_numeral_string(40, base))
        self.assertEqual('L', self.rmc.convert_digit_from_base_to_numeral_string(50, base))
        self.assertEqual('LX', self.rmc.convert_digit_from_base_to_numeral_string(60, base))
        self.assertEqual('LXX', self.rmc.convert_digit_from_base_to_numeral_string(70, base))
        self.assertEqual('LXXX', self.rmc.convert_digit_from_base_to_numeral_string(80, base))
        self.assertEqual('XC', self.rmc.convert_digit_from_base_to_numeral_string(90, base))

    def test_convert_third_digit_to_numeral_string(self):
        base = 100
        self.assertEqual('', self.rmc.convert_digit_from_base_to_numeral_string(0, base))
        self.assertEqual('C', self.rmc.convert_digit_from_base_to_numeral_string(100, base))
        self.assertEqual('CC', self.rmc.convert_digit_from_base_to_numeral_string(200, base))
        self.assertEqual('CCC', self.rmc.convert_digit_from_base_to_numeral_string(300, base))
        self.assertEqual('CD', self.rmc.convert_digit_from_base_to_numeral_string(400, base))
        self.assertEqual('D', self.rmc.convert_digit_from_base_to_numeral_string(500, base))
        self.assertEqual('DC', self.rmc.convert_digit_from_base_to_numeral_string(600, base))
        self.assertEqual('DCC', self.rmc.convert_digit_from_base_to_numeral_string(700, base))
        self.assertEqual('DCCC', self.rmc.convert_digit_from_base_to_numeral_string(800, base))
        self.assertEqual('CM', self.rmc.convert_digit_from_base_to_numeral_string(900, base))

    def test_convert_fourth_digit_to_numeral_string(self):
        base = 1000
        self.assertEqual('', self.rmc.convert_digit_from_base_to_numeral_string(0, base))
        self.assertEqual('M', self.rmc.convert_digit_from_base_to_numeral_string(1000, base))
        self.assertEqual('MM', self.rmc.convert_digit_from_base_to_numeral_string(2000, base))
        self.assertEqual('MMM', self.rmc.convert_digit_from_base_to_numeral_string(3000, base))

    @mock.patch('builtins.input', side_effect=['3999', '4000'])
    def test_upper_input_limit_of_3999(self, input):
        self.assertEqual(3999, self.rmc.get_user_input())
        with self.assertRaises(ValueError):
            self.rmc.get_user_input()

    def test_get_the_number_of_digits_for_base_and_for_integer_input(self):
        base = 10
        self.assertEqual(1, self.rmc.calculate_number_of_digits(1, base))
        self.assertEqual(2, self.rmc.calculate_number_of_digits(15, base))
        self.assertEqual(3, self.rmc.calculate_number_of_digits(258, base))
        self.assertEqual(4, self.rmc.calculate_number_of_digits(6577, base))
        self.assertEqual(5, self.rmc.calculate_number_of_digits(65423, base))
        base = 2
        self.assertEqual(3, self.rmc.calculate_number_of_digits(7, base))
        self.assertEqual(8, self.rmc.calculate_number_of_digits(255, base))
        self.assertEqual(10, self.rmc.calculate_number_of_digits(1023, base))

    @mock.patch('builtins.input', side_effect=['11', '154', '1874', '10', '200'])
    def test_converting_combined_digits(self, input):
        self.assertEqual('XI', self.rmc.convert_to_numeral_string())
        self.assertEqual('CLIV', self.rmc.convert_to_numeral_string())
        self.assertEqual('MDCCCLXXIV', self.rmc.convert_to_numeral_string())
        self.assertEqual('X', self.rmc.convert_to_numeral_string())
        self.assertEqual('CC', self.rmc.convert_to_numeral_string())
    


if __name__ == '__main__':
    unittest.main()