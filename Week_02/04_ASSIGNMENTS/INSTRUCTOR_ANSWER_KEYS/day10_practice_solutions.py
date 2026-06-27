# ============================================================
# ANSWER KEY FOR DAY 10 PRACTICE EXERCISES
# ============================================================
"""
# Exercise 1:
# Trace: i=0 -> 0%3==0 -> continue (skip)
#        i=1 -> not mult of 3, not 7 -> print 1
#        i=2 -> not mult of 3, not 7 -> print 2
#        i=3 -> 3%3==0 -> continue (skip)
#        i=4 -> print 4
#        i=5 -> print 5
#        i=6 -> 6%3==0 -> continue (skip)
#        i=7 -> break (exits before printing)
# Output: 1 2 4 5

# Exercise 2:
word = "Hello"
has_upper = False
for char in word:
    if char != char.lower():
        has_upper = True
        break
print(has_upper)

# Exercise 3:
s = "xyzqr"
vowels = "aeiouAEIOU"
found_flag = False
position = -1
for i in range(len(s)):
    if s[i] in vowels:
        found_flag = True
        position = i
        break
if found_flag:
    print(f"First vowel at position {position}: {s[position]}")
else:
    print("No vowels found")

# Exercise 4:
numbers = [34, 12, 67, 3, 89, 21]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print(smallest)   # 3

# Exercise 5:
s = "a1b2c3"
digit_count = 0
digit_sum = 0
for char in s:
    if char in "0123456789":
        digit_count += 1
        digit_sum += int(char)
print(f"count={digit_count}, sum={digit_sum}")

# Challenge:
string1 = "hello"
string2 = "world"
found_flag = False
common_char = None
for char in string1:
    if char in string2:
        common_char = char
        found_flag = True
        break
if found_flag:
    print(f"First common character: {common_char}")
else:
    print("No common characters")
"""
