#!F:\Python-Projects\Projects\RomanNumeralsConverter\env\Scripts\python.exe

from classes.roman_numeral_converter import RomanNumeralConverter

def main():
    rmc = RomanNumeralConverter()
    not_done = True
    while not_done:
        print("\n\nRoman Numeral Converter. Please make your Input.")
        result = rmc.convert_to_numeral_string()
        print(f"Your Number is {result!r} as a Roman Numeral")
        not_done = int(input("Continue? (1/0): "))


if __name__ == '__main__':
    main()