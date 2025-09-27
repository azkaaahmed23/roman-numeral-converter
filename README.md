# Roman Numeral Converter

A beginner-friendly Python program for converting between **Roman numerals** and **integers**.

---

## Features 

* **Roman $\leftrightarrow$ Integer Conversion**: Converts in both directions.
* **Full Range Support**: Handles integers from **1 to 3999** for conversion to Roman numerals.
* **Subtractive Notation**: Correctly processes special cases like **IV** (4), **IX** (9), **XL** (40), etc.
* **Simple Interface**: Easy-to-use, text-based menu for interaction.
* **Robust Input Handling**: Includes validation for invalid characters or out-of-range integers.

---

## How to Run 

1.  Ensure you have **Python 3** installed on your system.
2.  Save the code as a Python file (e.g., `roman_converter.py`).
3.  Open your terminal or command prompt, navigate to the file's directory, and run:

```bash
python roman_converter.py
```
Follow the simple on-screen menu to choose your conversion type.

---

## Examples

### Roman → Integer

Enter the Roman numerals you want to convert: XIV

The Roman numerals you entered translates to: 14!


### Integer → Roman

Enter the integer you want to convert (1–3999): 2025

The integer you entered translates to: MMXXV!


---
## Core Functions
The program uses two main functions for the conversion logic:

roman_to_int(numeral: str) -> int: Converts a Roman numeral string to an integer.

int_to_roman(num: int) -> str: Converts an integer (1–3999) to a Roman numeral string.

---

## Notes 
Only standard Roman numerals (I, V, X, L, C, D, M) are supported.

The integer range for Roman numeral conversion is 1 to 3999 (the typical limit for standard representation).

