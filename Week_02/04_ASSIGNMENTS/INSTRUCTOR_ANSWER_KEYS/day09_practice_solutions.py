# ============================================================
# ANSWER KEY FOR DAY 9 PRACTICE EXERCISES
# ============================================================
"""
# Exercise 1:
x = 81
guess = 0
while guess ** 4 < x:
    guess += 1
if guess ** 4 == x:
    print(f"The fourth root of {x} is {guess}")
else:
    print(f"{x} has no integer fourth root")

# Exercise 2:
n = 0
while n ** 2 <= 1000:
    n += 1
print(f"Smallest n with n^2 > 1000: n={n}, n^2={n**2}")

# Exercise 3:
for a in range(21):
    b = a
    c = 2 * a
    if a + b + c == 30:
        print(f"a={a}, b={b}, c={c}")

# Exercise 4:
total = 0
for i in range(100):
    total += 0.1
print(total)
print(abs(total - 10.0) < 0.0001)

# Challenge:
binary_str = "1101"
decimal_value = 0
for char in binary_str:
    decimal_value = decimal_value * 2 + int(char)
print(decimal_value)   # 13
"""
