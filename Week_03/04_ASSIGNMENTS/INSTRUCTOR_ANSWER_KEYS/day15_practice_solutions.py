# ============================================================
# ANSWER KEY FOR DAY 15 PRACTICE EXERCISES
# ============================================================
'''
# Exercise 1:
# Trace: transform(5) -> step1 = double(5) = 10
#                      -> step2 = increment(10) = 11
#                      -> returns 11
# Prints: 11

# Exercise 2:
def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_kelvin(f):
    celsius = (f - 32) * 5 / 9
    return celsius_to_kelvin(celsius)

print(fahrenheit_to_kelvin(32))    # 273.15 (32F = 0C)
print(fahrenheit_to_kelvin(212))   # 373.15 (212F = 100C)

# Exercise 3:
def is_prime(n):
    """Assumes n is an integer. Returns True if n is prime."""
    if n < 2:
        return False
    divisor = 2
    while divisor < n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True

def count_primes_up_to(n):
    """Assumes n is a positive integer. Returns count of primes from 2 to n."""
    count = 0
    for candidate in range(2, n + 1):
        if is_prime(candidate):
            count += 1
    return count

print(count_primes_up_to(50))   # 15

# Exercise 4:
def bisection_cube_root(x, epsilon=0.01):
    """Assumes x is non-negative. Returns approx cube root of x."""
    low = 0.0
    high = max(x, 1.0)
    guess = (low + high) / 2
    while abs(guess ** 3 - x) >= epsilon:
        if guess ** 3 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
    return guess

print(bisection_cube_root(27))     # close to 3
print(bisection_cube_root(1000))   # close to 10

# Exercise 5:
def bisection_sqrt_with_count(x, epsilon=0.01):
    """Returns (approx sqrt of x, number of iterations)."""
    low = 0.0
    high = max(x, 1.0)
    guess = (low + high) / 2
    iterations = 0
    while abs(guess ** 2 - x) >= epsilon:
        if guess ** 2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
        iterations += 1
    return guess, iterations

result, count = bisection_sqrt_with_count(1000)
print(f"sqrt approx: {result}, iterations: {count}")

# Challenge:
def count_up(n, current=1):
    """Assumes n is a positive integer. Prints 1 up to n, recursively."""
    if current > n:
        return
    print(current)
    count_up(n, current + 1)

count_up(5)
# 1 2 3 4 5, each on its own line
'''