# ============================================================
# ANSWER KEY FOR DAY 6 PRACTICE EXERCISES
# ============================================================
"""
# Exercise 1:
n = 100
while n >= 90:
    print(n)
    n -= 1

# Exercise 2:
value = 1
doublings = 0
while value <= 1000:
    print(value)
    value *= 2
    doublings += 1
print(f"It took {doublings} doublings to exceed 1000")

# Exercise 3:
sentence = ""
word = input("Enter a word (or 'done' to finish): ")
while word != "done":
    if sentence == "":
        sentence = word
    else:
        sentence = sentence + " " + word
    word = input("Enter a word (or 'done' to finish): ")
print("Final sentence:", sentence)

# Exercise 4:
remaining = 100
count = 0
while remaining - 7 >= 0:
    remaining -= 7
    count += 1
print(f"Subtracted 7 a total of {count} times")
print(f"Final remainder: {remaining}")

# Challenge:
n = 27
steps = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    steps += 1
print(f"Collatz sequence from 27 took {steps} steps to reach 1")
"""
