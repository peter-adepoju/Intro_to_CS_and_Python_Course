# ============================================================
# ANSWER KEY FOR DAY 14 PRACTICE EXERCISES
# ============================================================
"""
# Exercise 1:
def temp_convert(temp, to_fahrenheit):
    \"\"\"
    Assumes: temp is a number, to_fahrenheit is a boolean
    Returns: temp converted to Fahrenheit if to_fahrenheit is True,
             otherwise temp converted from Fahrenheit to Celsius
    \"\"\"
    if to_fahrenheit:
        return temp * 9/5 + 32
    else:
        return (temp - 32) * 5/9

# Exercise 2:
def is_valid_age(age):
    \"\"\"
    Assumes: age is a value of any type
    Returns: True if age is an integer between 0 and 130 inclusive,
             False otherwise
    \"\"\"
    return type(age) == int and 0 <= age <= 130

print(is_valid_age(25))     # True
print(is_valid_age(-5))     # False
print(is_valid_age(150))    # False
print(is_valid_age(25.5))   # False (not an int)

# Exercise 3:
def is_invalid_triangle(a, b, c):
    \"\"\"
    Assumes: a, b, c are positive numbers (side lengths)
    Returns: True if the three sides cannot form a valid triangle
    \"\"\"
    return a + b <= c or a + c <= b or b + c <= a

def is_equilateral(a, b, c):
    \"\"\"
    Assumes: a, b, c are positive numbers (side lengths)
    Returns: True if all three sides are equal
    \"\"\"
    return a == b == c

def is_isosceles(a, b, c):
    \"\"\"
    Assumes: a, b, c are positive numbers (side lengths)
    Returns: True if exactly two (or more) sides are equal
    \"\"\"
    return a == b or b == c or a == c

def evaluate_triangle_decomposed(a, b, c):
    \"\"\"
    Assumes: a, b, c are positive numbers (side lengths)
    Prints the triangle's classification.
    \"\"\"
    if is_invalid_triangle(a, b, c):
        print("Invalid triangle")
    elif is_equilateral(a, b, c):
        print("Equilateral")
    elif is_isosceles(a, b, c):
        print("Isosceles")
    else:
        print("Scalene")

evaluate_triangle_decomposed(3, 3, 3)   # Equilateral
evaluate_triangle_decomposed(3, 3, 5)   # Isosceles
evaluate_triangle_decomposed(3, 4, 5)   # Scalene
evaluate_triangle_decomposed(1, 1, 10)  # Invalid triangle

# Challenge:
def is_vowel(char):
    \"\"\"
    Assumes: char is a single character
    Returns: True if char is a vowel (a, e, i, o, u, case-insensitive)
    \"\"\"
    return char.lower() in "aeiou"

def is_consonant(char):
    \"\"\"
    Assumes: char is a single character
    Returns: True if char is an alphabetic letter that is not a vowel
    \"\"\"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return char.lower() in alphabet and not is_vowel(char)

def is_digit_char(char):
    \"\"\"
    Assumes: char is a single character
    Returns: True if char is a digit character (0-9)
    \"\"\"
    return char in "0123456789"

def classify_string(s):
    \"\"\"
    Assumes: s is a string
    Prints counts of vowels, consonants, and digits in s.
    \"\"\"
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    for char in s:
        if is_vowel(char):
            vowel_count += 1
        elif is_consonant(char):
            consonant_count += 1
        elif is_digit_char(char):
            digit_count += 1
    print(f"Vowels: {vowel_count}, Consonants: {consonant_count}, Digits: {digit_count}")

classify_string("Hello World 123")
"""