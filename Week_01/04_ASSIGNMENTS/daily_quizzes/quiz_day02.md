# 🧠 Quiz — Day 2
## Variables, Bindings, and Expressions

---

**Q1.** After these lines, what is the value of `y`?
```python
x = 10
y = x + 5
x = 20
```

A) 15
B) 25
C) 20
D) 10

---

**Q2.** What does the following code print?
```python
a = 3
a = a * 2
a += 1
print(a)
```

A) 3
B) 6
C) 7
D) 8

---

**Q3.** Which of these is a valid Python variable name?

A) `2fast`
B) `my-variable`
C) `total_score`
D) `for`

---

**Q4.** After this code runs, what are the final values of `x` and `y`?
```python
x = 5
y = x
x = x + 1
```

A) x=6, y=6
B) x=5, y=5
C) x=6, y=5
D) x=5, y=6

---

**Q5.** What is wrong with this attempted swap?
```python
x = 1
y = 2
y = x
x = y
```

A) Nothing — it works correctly
B) It sets both x and y to 1
C) It raises an error
D) It sets both x and y to 2

---

**Q6.** What does this print?
```python
n = 10
n -= 3
n *= 2
print(n)
```

A) 17
B) 14
C) 7
D) 20

---

**Q7.** Which of these is an *expression* (produces a value) rather than a
plain *statement*?

A) `x = 5`
B) `print("hello")`
C) `3 + 4`
D) `x += 1`

---

**Q8.** Which is the preferred Python style for a variable holding the
number of active users?

A) `ActiveUsers`
B) `active-users`
C) `active_users`
D) `ACTIVE_USERS`

---

**Q9.** Trace this code. What is `result` at the end?
```python
a = 4
b = a + 2    # b becomes 6
a = b * 3    # a becomes 18
b = a - b    # b becomes 18 - 6
result = a + b
```

A) 24
B) 30
C) 18
D) 36

---

**Q10.** True or False: In Python, `x = 5` and `5 = x` accomplish the same thing.

A) True — order doesn't matter
B) False — `5 = x` is a SyntaxError because you cannot assign to a literal value

---
---

## 📋 Answer Key — Day 2

| Q | Answer | Explanation |
|---|---|---|
| 1 | A — 15 | `y` was bound to `x + 5 = 15` while `x` was still 10. Reassigning `x` afterward does not retroactively change `y`. |
| 2 | C — 7 | `a=3` → `a=6` (×2) → `a=7` (+1) |
| 3 | C — `total_score` | A starts with a digit (illegal), B has a hyphen (illegal), D is a reserved keyword |
| 4 | C — x=6, y=5 | `y` was bound to 5 (x's value at that moment); reassigning x afterward doesn't change y |
| 5 | B — both become 1 | `y = x` makes y=1; then `x = y` makes x=1. The original y=2 was overwritten and lost before it could be used. |
| 6 | B — 14 | n=10 → n=7 (n-=3) → n=14 (n*=2) |
| 7 | C — `3 + 4` | This evaluates to the value 7. A, B, D are statements (they perform actions, B has a side effect of printing but produces no usable value itself) |
| 8 | C — `active_users` | Python convention is snake_case: lowercase words joined by underscores |
| 9 | B — 30 | a=4, b=6, a=18, b=18-6=12, result=18+12=30 |
| 10 | B — False | The left-hand side of `=` must be a valid name (a "target"), not a literal value like `5` |

---

*Next: open `02_NOTEBOOKS/week_01/day03_strings.ipynb`*
