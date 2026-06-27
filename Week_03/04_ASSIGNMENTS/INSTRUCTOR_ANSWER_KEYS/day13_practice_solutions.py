# ============================================================
# ANSWER KEY FOR DAY 13 PRACTICE EXERCISES
# ============================================================
"""
# Exercise 1:
def triple(x):
    return x * 3

result = triple(4) + triple(5)
print(result)   # 12 + 15 = 27

# Exercise 2:
def sign(n):
    if n > 0:
        return "positive"
    if n < 0:
        return "negative"
    return "zero"

print(sign(5), sign(-3), sign(0))

# Exercise 3:
def three_min(a, b, c):
    smallest = a
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c
    return smallest

print(three_min(7, 2, 9))   # 2

# Exercise 4:
def divide_safely(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(divide_safely(10, 2))   # 5.0
print(divide_safely(10, 0))   # Cannot divide by zero

# Challenge:
def circle_area(radius):
    pi = 3.14159
    return pi * radius ** 2

def circle_circumference(radius):
    pi = 3.14159
    return 2 * pi * radius

def circle_summary(radius):
    area = circle_area(radius)
    circumference = circle_circumference(radius)
    return area, circumference

a, c = circle_summary(5)
print(f"Area: {a:.2f}, Circumference: {c:.2f}")
"""