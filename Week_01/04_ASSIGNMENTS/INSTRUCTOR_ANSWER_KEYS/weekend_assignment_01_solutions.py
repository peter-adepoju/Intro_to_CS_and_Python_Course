"""
INSTRUCTOR-ONLY ANSWER KEY
Weekend Assignment 1 — Week 1 Solutions

Do not place this file where students will see it before attempting
the assignment themselves. Keep in INSTRUCTOR_ANSWER_KEYS/ folders only.
"""

# ============================================================
# PART A
# ============================================================

# --- A1: Receipt Generator ---
burger_name, burger_price = "Burger", 8.99
fries_name, fries_price = "Fries", 3.49
soda_name, soda_price = "Soda", 1.99

subtotal = burger_price + fries_price + soda_price
tax_rate = 0.085
tax = subtotal * tax_rate
total = subtotal + tax

print("RECEIPT")
print("-" * 25)
print(f"{burger_name:<15}{burger_price:>10.2f}")
print(f"{fries_name:<15}{fries_price:>10.2f}")
print(f"{soda_name:<15}{soda_price:>10.2f}")
print("-" * 25)
print(f"{'Subtotal':<15}{subtotal:>10.2f}")
print(f"{'Tax (8.5%)':<15}{tax:>10.2f}")
print(f"{'TOTAL':<15}{total:>10.2f}")
print()

# --- A2: Temperature Conversion Table ---
c1, c2, c3, c4, c5 = 0, 10, 20, 30, 37
c_extra = 100

def c_to_f(c):
    return c * 9/5 + 32

print(f"{'Celsius':<10}{'Fahrenheit':>10}")
print(f"{'-------':<10}{'----------':>10}")
for c in [c1, c2, c3, c4, c5, c_extra]:
    print(f"{c:>7.1f}   {c_to_f(c):>10.1f}")
print()
# NOTE: this answer key uses a for loop for brevity, but students at this
# point in the course have NOT learned loops yet — the expected student
# solution repeats the conversion+print logic five separate times.

# --- A3: String Analysis Tool ---
word = "level"   # example test value; students should test multiple words
length = len(word)
mid = length // 2
first_half = word[:mid]
second_half = word[mid:]  # extra char (if odd length) goes here
is_palindrome = (word == word[::-1])
same_start_end = (word[0] == word[-1])

print(f"Word: {word}")
print(f"Length: {length}")
print(f"First half: {first_half}")
print(f"Second half: {second_half}")
print(f"Is palindrome: {is_palindrome}")
print(f"Starts and ends with same letter: {same_start_end}")
print()


# ============================================================
# PART B
# ============================================================

# --- B1: Movie Ticket Pricing ---
age = 30          # example test value
is_matinee_input = "yes"   # example test value

if age < 13:
    base_price = 8.00
elif age >= 65:
    base_price = 9.00
else:
    base_price = 14.00

if is_matinee_input.lower() == "yes":
    final_price = base_price - 3.00
    if final_price < 5.00:
        final_price = 5.00
else:
    final_price = base_price

print(f"Ticket price: ${final_price:.2f}")
print()

# --- B2: Password Strength Checker ---
password = "Tr0ub4dor"   # example test value

length_ok = len(password) >= 8
has_digit = (
    "0" in password or "1" in password or "2" in password or
    "3" in password or "4" in password or "5" in password or
    "6" in password or "7" in password or "8" in password or
    "9" in password
)
common_weak = (
    password == "password" or password == "12345678" or
    password == "qwerty123"
)

if length_ok and has_digit and not common_weak:
    print("Strong password")
else:
    if not length_ok:
        print("FAILED: too short (must be at least 8 characters)")
    if not has_digit:
        print("FAILED: must contain at least one digit")
    if common_weak:
        print("FAILED: this is a commonly used weak password")
print()


# ============================================================
# PART C
# ============================================================

# --- C1: Mixed Review Answers ---
"""
1. (7 + 3) % 4 * 2
   Step 1: 7 + 3 = 10
   Step 2: 10 % 4 = 2   (% and * have equal precedence, evaluated left to right)
   Step 3: 2 * 2 = 4
   Answer: 4

2. s = "hello world"
   s[6:]  -> "world"
   s[:5]  -> "hello"
   s[6]   -> "w"

3. x = 5
   y = "5"
   print(x == y)        -> False (int 5 is never equal to str "5")
   print(str(x) == y)   -> True  (str(5) == "5" -> "5" == "5" -> True)

4. int(input(...)) crashes when the user types something that cannot be
   parsed as an integer (like "hello" or "3.14" or an empty string),
   because int() raises a ValueError when it cannot interpret the text
   as a whole number. We will learn to handle this gracefully with
   try/except in Week 7.

5. Chained comparison: 10 < x < 20
   'and' version:       x > 10 and x < 20
"""

# --- C2: Bug Hunt Answers ---

# Snippet 1 — BUG: uses = instead of == in the condition
x = 5
if x == 10:    # FIXED
    print("ten")

# Snippet 2 — BUG: can't concatenate str and int with +; age needs str()
name = "Alice"
age = 30
print("Name: " + name + " Age: " + str(age))   # FIXED

# Snippet 3 — BUG: uses two independent if's instead of if/elif,
# so for score=72, "Pass" is set then never overwritten (this one
# actually works correctly by coincidence for this score, but FAILS
# for score=95, where it would print "Excellent" -- correct here too
# actually, since 95 triggers BOTH conditions and "Excellent" is set
# last). The real bug shows up for score=95 vs score=72: students
# should realize the order of independent ifs can produce wrong
# results depending on which condition is checked last. Correct fix:
score = 72
grade = "Fail"   # add a default fallback
if score >= 90:
    grade = "Excellent"
elif score >= 60:
    grade = "Pass"
print(grade)

# Snippet 4 — BUG: index 5 is out of range for "hello" (valid: 0-4)
s = "hello"
print(s[4])   # FIXED (or use s[-1])
