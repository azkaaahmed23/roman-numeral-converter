"""
Roman Numeral Converter
-----------------------
Beginner-friendly program to convert:
1. Roman numerals → Integer
2. Integer → Roman numerals
"""

# Special subtractive cases (e.g., IV = 4, IX = 9)
special_cases = {
    "CM": 900, "CD": 400, "XC": 90, "XL": 40,
    "IX": 9, "IV": 4
}

# Basic single Roman numeral values
roman_values = {
    "M": 1000, "D": 500, "C": 100,
    "L": 50, "X": 10, "V": 5, "I": 1
}


def roman_to_int(numeral: str) -> int:
    """
    Convert a Roman numeral string to an integer.
    """
    i = 0
    total = 0

    while i < len(numeral):
        # First check if the next two characters form a special case
        if i + 1 < len(numeral) and numeral[i:i+2] in special_cases:
            total += special_cases[numeral[i:i+2]]
            i += 2
        # Otherwise, process a single numeral
        elif numeral[i] in roman_values:
            total += roman_values[numeral[i]]
            i += 1
        else:
            raise ValueError(f"Invalid Roman numeral character: {numeral[i]}")

    return total


def int_to_roman(num: int) -> str:
    """
    Convert an integer (1–3999) to a Roman numeral string.
    """
    if num <= 0 or num > 3999:
        raise ValueError("Enter a number between 1 and 3999")

    roman_pairs = [
        ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
        ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
        ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
    ]

    result = ""
    for roman, value in roman_pairs:
        while num >= value:
            result += roman
            num -= value
    return result


def main():
    """
    Simple text-based menu for the converter.
    """
    while True:
        print("\nChoose an option:")
        print("1. Roman → Integer")
        print("2. Integer → Roman")
        print("3. Exit")

        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            roman_input = input("Enter the Roman numerals you want to convert: ").upper().strip()
            try:
                result = roman_to_int(roman_input)
                print(f"The Roman numerals you entered translates to: {result}!")
            except ValueError as e:
                print("Error:", e)

        elif choice == "2":
            try:
                number = int(input("Enter the integer you want to convert (1–3999): "))
                result = int_to_roman(number)
                print(f"The integer you entered translates to: {result}!")
            except ValueError as e:
                print("Error:", e)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
