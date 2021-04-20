import math

class RomanNumeralConverter:
    
    MAX_INTEGER_SUPPORT = 3999
    NUMERAL_KEYS = {
        1:   'I',
        5:   'V',
        10:  'X',
        50:  'L',
        100: 'C',
        500: 'D',
        1000:'M'
    }

    def get_user_input(self) -> int:
        valie_input = False
        while not valie_input:
            try:
                user_input = int(input("Input: "))
            except ValueError:
                print("Your input needs to be a numeral.")
                continue
            valie_input = True
            if user_input > self.MAX_INTEGER_SUPPORT:
                valie_input = False
                raise ValueError(f"This Roman Numeral Converter just supports numbers from 1-{self.MAX_INTEGER_SUPPORT}.")
        return user_input

    def calculate_number_of_digits(self, number: int, base: int = 10) -> int:
        temp = math.log(number, base)
        number_of_digits = math.floor(temp) + 1
        return number_of_digits

    def split_number_into_digits_and_exponent(self, number: int) -> list[int]:
        base = 10
        number_of_digits = self.calculate_number_of_digits(number, base)

        digit_list = []
        temp_number = number
        for exponent in reversed(range(number_of_digits)):
            digit_number = math.floor(temp_number / base ** exponent) * base ** exponent
            temp_number -= digit_number
            digit_list.append((digit_number, exponent))

        return digit_list

    def convert_digit_from_base_to_numeral_string(self, digit: int, base: int) -> str:
        roman_numeral_string = ''
        if digit > 0:
            for next_key in self.NUMERAL_KEYS.keys():
                if digit >= next_key:
                    previous_key = next_key
                    continue
                if digit == next_key-base:
                    roman_numeral_string = ''.join([self.NUMERAL_KEYS[base], self.NUMERAL_KEYS[next_key]])
                    return roman_numeral_string
            
            difference_to_key = round((digit - previous_key)/base)
            extra_ones = self.NUMERAL_KEYS[base]*difference_to_key
            roman_numeral_string = ''.join([self.NUMERAL_KEYS[previous_key], extra_ones])
        return roman_numeral_string

    def convert_to_numeral_string(self, base: int = 10) -> str:
        user_input = self.get_user_input()
        digit_exponent_list = self.split_number_into_digits_and_exponent(user_input)
        roman_numeral_string = ''
        for (digit, exponent) in digit_exponent_list:
            string_for_digit = self.convert_digit_from_base_to_numeral_string(digit, base**(exponent))
            roman_numeral_string += string_for_digit
        return roman_numeral_string
 
if __name__ == '__main__':
    rmc = RomanNumeralConverter()
    # print(rmc.convert_to_numeral_string())
    rmc.get_user_input()