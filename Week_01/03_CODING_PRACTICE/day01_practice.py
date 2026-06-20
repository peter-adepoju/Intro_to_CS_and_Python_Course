"""
Day 1 Practice — Types, Arithmetic, and Type Conversion
Week 1, Day 1

Instructions:
- Work through exercises 1-4 in order.
- Each exercise has a comment describing the goal.
- Write your code directly below the instructions.
- Run this file with: python day01_practice.py
- Compare your output with the expected output noted in each exercise.

Do NOT look at the answer key (bottom of this file, separated clearly)
until you've attempted every exercise yourself.
"""

# ============================================================
# EXERCISE 1: Basic Arithmetic
# ============================================================
# Compute the following and print each with a descriptive label:
# (a) The sum of 47 and 89
# (b) The product of 13 and 7
# (c) 100 divided by 7 (true division)
# (d) 100 divided by 7 (floor division)
# (e) The remainder of 100 divided by 7

# YOUR CODE HERE


# ============================================================
# EXERCISE 2: Type Conversion
# ============================================================
# Given the float value 19.87:
# (a) Print its type
# (b) Convert it to an int using int() and print the result
# (c) Convert it to an int using round() and print the result
# (d) Explain in a comment why (b) and (c) give different answers

value = 19.87
# YOUR CODE HERE


# ============================================================
# EXERCISE 3: The Divisibility Test
# ============================================================
# Write code that checks whether 144 is divisible by 12.
# Print True if it is, False if it isn't.
# Do this WITHOUT typing True or False directly — compute it
# using the % operator and a comparison.

# YOUR CODE HERE


# ============================================================
# EXERCISE 4: Unit Conversion Program
# ============================================================
# A recipe requires ingredients measured in cups, but you only have
# a scale that measures in grams. 1 cup of flour = 120 grams.
#
# Given a recipe that calls for 3.5 cups of flour, compute and print
# how many grams of flour are needed.
#
# Then, given that you have 500 grams of flour, compute and print
# how many cups that is (to 2 decimal places using an f-string).

cups_needed = 3.5
grams_available = 500
# YOUR CODE HERE


# ============================================================
# CHALLENGE: Digit Extraction
# ============================================================
# Given the 4-digit number 7392, extract and print each digit
# separately (7, then 3, then 9, then 2) using only // and %
# (Don't convert to a string — use pure arithmetic!)
#
# Hint: 7392 % 10 gives you the last digit (2).
#       7392 // 10 gives you 739 (chops off the last digit).
#       Repeat this process.

number = 7392
# YOUR CODE HERE


# ============================================================
# ANSWER KEY (Don't peek until you've tried everything above!)
# ============================================================
"""
# Exercise 1:
print("Sum:", 47 + 89)                  # 136
print("Product:", 13 * 7)               # 91
print("True division:", 100 / 7)        # 14.285714285714286
print("Floor division:", 100 // 7)      # 14
print("Remainder:", 100 % 7)            # 2

# Exercise 2:
value = 19.87
print(type(value))           # <class 'float'>
print(int(value))            # 19 (truncates)
print(round(value))          # 20 (rounds to nearest)
# int() always truncates toward zero regardless of how close the
# decimal is to the next integer. round() finds the nearest integer.

# Exercise 3:
print(144 % 12 == 0)         # True

# Exercise 4:
cups_needed = 3.5
grams_available = 500
grams_needed = cups_needed * 120
cups_from_grams = grams_available / 120
print(f"{cups_needed} cups of flour = {grams_needed}g")
print(f"{grams_available}g of flour = {cups_from_grams:.2f} cups")

# Challenge:
number = 7392
digit4 = number % 10        # 2
number = number // 10       # 739
digit3 = number % 10        # 9
number = number // 10       # 73
digit2 = number % 10        # 3
number = number // 10       # 7
digit1 = number % 10        # 7
print(digit1, digit2, digit3, digit4)   # 7 3 9 2
"""
