"""
INSTRUCTOR-ONLY ANSWER KEY
Weekend Assignment 3 — Week 3 Cumulative Review Solutions

Do not place this file where students will see it before attempting
the assignment themselves. Keep in INSTRUCTOR_ANSWER_KEYS/ folders only.
"""

# ============================================================
# PART A
# ============================================================

# --- A1: Full Trace ---
def add_five(x):
    return x + 5

def double(x):
    return x * 2

def mystery(x):
    a = add_five(x)   # a = 3 + 5 = 8
    b = double(a)       # b = 8 * 2 = 16
    c = add_five(b)     # c = 16 + 5 = 21
    return c

print(mystery(3))   # 21
print()

# --- A2: Scope Trace ---
value = 100

def update(value):
    value = value + 1   # this creates/modifies a LOCAL 'value', the
                          # parameter -- it shadows the global 'value'
                          # for the duration of this call only
    return value

new_value = update(value)
print(value, new_value)
# Prints: 100 101
# Explanation: the parameter 'value' inside update() is a completely
# separate, local binding from the global 'value'. Reassigning it
# inside the function (value = value + 1) only affects that local
# copy -- the global 'value' is never touched, since we never assign
# to the global name, only read it once to provide the initial
# argument. This is consistent with Chapter 13's discussion of local
# scope: parameters are always local to their function.
print()


# ============================================================
# PART B
# ============================================================

# --- B1: Spec-First Design ---
def days_to_hours(days):
    """
    Assumes: days is a non-negative number
    Returns: the equivalent number of hours
    """
    return days * 24

print(days_to_hours(3))    # 72
print(days_to_hours(0.5))  # 12.0
print()

# --- B2: Decomposition Practice ---
def calculate_base_cost(weight_kg, distance_km):
    """
    Assumes: weight_kg and distance_km are non-negative numbers
    Returns: the base shipping cost before any express surcharge
    """
    return weight_kg * 0.5 + distance_km * 0.01

def apply_express_surcharge(base_cost, express):
    """
    Assumes: base_cost is a non-negative number, express is a boolean
    Returns: base_cost increased by 50% if express is True, otherwise
             base_cost unchanged
    """
    if express:
        return base_cost * 1.5
    return base_cost

def shipping_cost(weight_kg, distance_km, express):
    """
    Assumes: weight_kg, distance_km are non-negative numbers,
             express is a boolean
    Returns: the final shipping cost, rounded to 2 decimal places
    """
    base_cost = calculate_base_cost(weight_kg, distance_km)
    final_cost = apply_express_surcharge(base_cost, express)
    return round(final_cost, 2)

print(shipping_cost(10, 100, False))   # 6.0
print(shipping_cost(10, 100, True))    # 9.0
print()


# ============================================================
# PART C: Bug Hunt
# ============================================================

# Snippet 1 -- BUG: add() only prints, never returns, so the + between
# two None values raises a TypeError
def add(a, b):
    return a + b   # FIXED (was: print(a + b))

total = add(3, 4) + add(5, 6)
print(total)   # 18

# Snippet 2 -- BUG: default parameter y=10 comes before non-default z,
# which is a SyntaxError. Fix by reordering parameters.
def f(x, z, y=10):   # FIXED (was: def f(x, y=10, z):)
    return x + y + z

print(f(1, 2))        # 1 + 10 + 2 = 13
print(f(1, 2, 3))     # 1 + 3 + 2 = 6

# Snippet 3 -- BUG: assigning to 'count' inside increment() makes it
# local to the function, so reading 'count' would raise
# UnboundLocalError if read before assignment in this body (and even
# without that specific error here, the global 'count' is never
# actually updated). Fix using the preferred pattern: pass current
# value in, return new value out.
def increment(current_count):
    return current_count + 1

count = 0
count = increment(count)
print(count)   # 1

# Snippet 4 -- BUG: missing return cases for scores below 80 means the
# function implicitly returns None for those scores
def get_grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:          # FIXED: added missing cases
        return "C"
    if score >= 60:
        return "D"
    return "F"

print(get_grade(65))   # D
