"""
INSTRUCTOR-ONLY ANSWER KEY
Weekend Assignment 2 — Week 2 Solutions

Do not place this file where students will see it before attempting
the assignment themselves. Keep in INSTRUCTOR_ANSWER_KEYS/ folders only.
"""

# ============================================================
# PART A
# ============================================================

# --- A1: Prime Number Checker ---
def check_prime(n):
    if n < 2:
        return False
    is_prime_flag = True
    divisor = 2
    while divisor < n:
        if n % divisor == 0:
            is_prime_flag = False
            break
        divisor += 1
    return is_prime_flag

for test_n in [2, 17, 18, 1, 97]:
    result = check_prime(test_n)
    print(f"{test_n} is prime: {result}")
print()

# Optimized version (only check up to sqrt(n)) -- mentioned as a bonus
def check_prime_optimized(n):
    if n < 2:
        return False
    is_prime_flag = True
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            is_prime_flag = False
            break
        divisor += 1
    return is_prime_flag

for test_n in [2, 17, 18, 1, 97]:
    result = check_prime_optimized(test_n)
    print(f"(optimized) {test_n} is prime: {result}")
print()


# --- A2: Number Pyramid ---
n = 5
width = 2 * n - 1   # width of the widest (last) row, for centering
for i in range(1, n + 1):
    row = str(i) * (2 * i - 1)
    print(row.center(width))
print()
# NOTE: this uses .center(), a string method not yet formally taught
# (it comes in Week 3). A student solution built only from Week 1-2
# tools would compute padding manually:
print("--- Manual-padding version (Week 1-2 tools only) ---")
n = 5
width = 2 * n - 1
for i in range(1, n + 1):
    row = str(i) * (2 * i - 1)
    pad = (width - len(row)) // 2
    print(" " * pad + row)
print()


# --- A3: Word Frequency in a Sentence ---
sentence = "the cat sat on the mat with another cat"
target = "cat"

sentence_lower = sentence.lower()
target_lower = target.lower()

count = 0
for i in range(len(sentence_lower) - len(target_lower) + 1):
    if sentence_lower[i:i + len(target_lower)] == target_lower:
        count += 1
print(f"'{target}' appears {count} times")
print()


# ============================================================
# PART B
# ============================================================

# --- B1: Number Guessing Game ---
secret = 63
guesses_used = 0
max_guesses = 7
won = False

test_guesses = iter([50, 70, 60, 65, 63])   # simulated guesses for testing

while guesses_used < max_guesses:
    guess = next(test_guesses)   # in a real run: int(input("Guess: "))
    guesses_used += 1
    if guess == secret:
        won = True
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")

if won:
    print(f"Correct! It took you {guesses_used} guesses.")
else:
    print(f"Out of guesses! The secret number was {secret}.")
print()


# --- B2: Digit Sum and Digital Root ---
number = 9875
current = number
while current >= 10:
    digit_sum = 0
    temp = current
    while temp > 0:
        digit_sum += temp % 10
        temp = temp // 10
    print(f"{current} -> digit sum = {digit_sum}")
    current = digit_sum
print(f"Digital root: {current}")
print()


# ============================================================
# PART C
# ============================================================

# --- C1: Mixed Review Answers ---
"""
1. Trace:
   for i in range(3):       # i = 0, 1, 2
       for j in range(2):   # j = 0, 1
           if i == j:
               continue
           print(i, j)

   i=0, j=0: i==j -> continue (skip)
   i=0, j=1: print "0 1"
   i=1, j=0: print "1 0"
   i=1, j=1: i==j -> continue (skip)
   i=2, j=0: print "2 0"
   i=2, j=1: print "2 1"

   Output:
   0 1
   1 0
   2 0
   2 1

2. Version A: total starts at 0, ends at 0+0+1+2+3+4 = 10
   Version B: total starts at 1, ends at 1+0+1+2+3+4 = 11
   They do NOT produce the same result -- the starting value of an
   accumulator directly affects the final answer when using +=.

3. 0.1 cannot be represented exactly in binary floating-point, the same
   way 1/3 cannot be represented exactly in decimal. Each addition of
   0.1 carries a tiny rounding error, and these errors accumulate, so
   the sum ends up extremely close to but not exactly equal to 0.3.

4. while count < 10 and not found:
   (or equivalently: while count < 10 and found == False:)

5. This loop is an infinite loop. n starts at 1 and increases by 2 each
   time (1, 3, 5, 7, 9, 11, 13, ...) -- it will never exactly equal 10,
   since it only ever takes odd values. The condition n != 10 will
   therefore never become False, so the loop never terminates.
"""

# --- C2: Bug Hunt Answers ---

# Snippet 1 -- BUG: uses '=' instead of '+=', so total just holds the
# LAST value of i instead of accumulating a sum
total = 0
for i in range(1, 10):
    total += i      # FIXED (was: total = i)
print(total)          # 45

# Snippet 2 -- BUG: n increases instead of decreases, so n > 0 is always
# true -- infinite loop
n = 5
while n > 0:
    print(n)
    n -= 1            # FIXED (was: n += 1)

# Snippet 3 -- BUG: print(i, j) is outside the inner loop (correct
# indentation-wise, it IS already outside) but it runs on every outer
# pass regardless of whether break fired, and j holds whatever value it
# had when the inner loop exited (not necessarily meaningful). A
# corrected version using a flag to track "no match found" looks like:
for i in range(3):
    no_match_flag = True
    for j in range(3):
        if i == j:
            no_match_flag = False
            break
    if no_match_flag:
        print(f"No match for i={i}")

# Snippet 4 -- BUG: factorial starts at 0, and anything multiplied by 0
# stays 0 forever
factorial = 1          # FIXED (was: factorial = 0)
for i in range(1, 6):
    factorial *= i
print(factorial)         # 120
