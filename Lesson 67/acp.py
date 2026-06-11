class RomanConverter:
    def __init__(self, number):
        self.number = number

    def to_roman(self):
        values = [1000, 900, 500, 400,
                  100, 90, 50, 40,
                  10, 9, 5, 4, 1]

        numerals = ["M", "CM", "D", "CD",
                    "C", "XC", "L", "XL",
                    "X", "IX", "V", "IV", "I"]

        roman = ""
        num = self.number

        for i in range(len(values)):
            while num >= values[i]:
                roman += numerals[i]
                num -= values[i]

        return roman


try:
    number = int(input("Enter an integer (1-3999): "))

    if 1 <= number <= 3999:
        converter = RomanConverter(number)
        print("Roman Numeral:", converter.to_roman())
    else:
        print("Please enter a number between 1 and 3999.")

except ValueError:
    print("Invalid input! Please enter a valid integer.")