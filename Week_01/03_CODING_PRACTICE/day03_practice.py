"""
Day 3 Practice — Strings, Indexing, and Slicing
Week 1, Day 3

Run with: python day03_practice.py
"""

# ============================================================
# EXERCISE 1: Index Practice
# ============================================================
# Given s = "computational", print:
# (a) The character at index 0
# (b) The character at index 5
# (c) The last character (using negative indexing)
# (d) The second-to-last character

s = "computational"
# YOUR CODE HERE


# ============================================================
# EXERCISE 2: Slicing Practice
# ============================================================
# Given s = "computational", extract:
# (a) The first 4 characters ("comp")
# (b) The last 5 characters ("ional")
# (c) Characters at indices 3 through 7 (exclusive of 7)
# (d) Every 3rd character starting from index 0

s = "computational"
# YOUR CODE HERE


# ============================================================
# EXERCISE 3: String Building
# ============================================================
# Given first_name = "Ada" and last_name = "Lovelace", build a string
# that reads: "Lovelace, Ada (initials: A.L.)"
# Use only concatenation, slicing, and indexing (no string methods
# like .upper() or .format() yet — those come in Week 3).

first_name = "Ada"
last_name = "Lovelace"
# YOUR CODE HERE


# ============================================================
# EXERCISE 4: Reverse Without [::-1]
# ============================================================
# As a learning exercise, reverse the string "python" using slicing
# with explicit start/stop/step values (not the shortcut [::-1]).
# Then ALSO do it with [::-1] and verify they match.

word = "python"
# YOUR CODE HERE


# ============================================================
# EXERCISE 5: Substring Search (Manual)
# ============================================================
# Given s = "the quick brown fox", check (using the 'in' operator)
# whether each of these substrings is present:
# "quick", "slow", "fox", "Fox" (note the capital F)
# Print each result clearly labeled.

s = "the quick brown fox"
# YOUR CODE HERE


# ============================================================
# EXERCISE 6: Palindrome Checker
# ============================================================
# Write code that checks if the string "racecar" is a palindrome
# (reads the same forwards and backwards). Do this by comparing
# the string to its reverse. Test with "racecar" and "hello".

test_word = "racecar"
# YOUR CODE HERE


# ============================================================
# CHALLENGE: String Sandwich
# ============================================================
# Given two strings:
#   outer = "((**))"
#   inner = "PYTHON"
# Insert 'inner' into the exact middle of 'outer' so that the
# result reads: "((*PYTHON*))"
# (Hint: find the midpoint index of outer using len() // 2,
# then slice outer into two halves and concatenate with inner
# in between.)

outer = "((**))"
inner = "PYTHON"
# YOUR CODE HERE


# ============================================================
# ANSWER KEY
# ============================================================
"""
# Exercise 1:
s = "computational"
print(s[0])      # c
print(s[5])      # u
print(s[-1])     # l
print(s[-2])     # a

# Exercise 2:
s = "computational"
print(s[0:4])    # comp
print(s[-5:])    # ional
print(s[3:7])    # puta
print(s[::3])    # cpaol  (indices 0,3,6,9,12 -> c,p,a,o,l)

# Exercise 3:
first_name = "Ada"
last_name = "Lovelace"
result = last_name + ", " + first_name + " (initials: " + first_name[0] + "." + last_name[0] + ".)"
print(result)
# Lovelace, Ada (initials: A.L.)

# Exercise 4:
word = "python"
reversed_explicit = word[5:-7:-1] if False else word[len(word)-1::-1]
# Simpler explicit version:
reversed_explicit = word[5:None:-1]   # start at last index, go to the start
reversed_shortcut = word[::-1]
print(reversed_explicit)   # nohtyp
print(reversed_shortcut)   # nohtyp
print(reversed_explicit == reversed_shortcut)   # True

# Exercise 5:
s = "the quick brown fox"
print("quick" in s)   # True
print("slow" in s)    # False
print("fox" in s)     # True
print("Fox" in s)     # False (case-sensitive)

# Exercise 6:
test_word = "racecar"
is_palindrome = (test_word == test_word[::-1])
print(is_palindrome)   # True

test_word = "hello"
is_palindrome = (test_word == test_word[::-1])
print(is_palindrome)   # False

# Challenge:
outer = "((**))"
inner = "PYTHON"
mid = len(outer) // 2          # 3
result = outer[:mid] + inner + outer[mid:]
print(result)   # ((*PYTHON*))
"""
