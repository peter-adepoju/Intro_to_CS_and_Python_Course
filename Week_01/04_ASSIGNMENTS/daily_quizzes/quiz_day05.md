# 🧠 Quiz — Day 5
## Branching and Conditionals

---

**Q1.** What does this code print?
```python
x = 7
if x > 5:
    print("big")
print("done")
```

A) Only "done"
B) Only "big"
C) "big" then "done"
D) Neither

---

**Q2.** What does `True and False` evaluate to?

A) True
B) False
C) None
D) Error

---

**Q3.** Which of the following is a correctly written `if` statement in Python?

A) `if (x == 5) then:`
B) `if x == 5:`
C) `if x == 5`
D) `If x == 5:`

---

**Q4.** What does this code print when `x = 10`?
```python
if x > 0:
    print("positive")
elif x > 5:
    print("more than 5")
else:
    print("non-positive")
```

A) "positive" only
B) "more than 5" only
C) Both "positive" and "more than 5"
D) "non-positive"

---

**Q5.** What does `not True or False` evaluate to?
(Remember: `not` binds tighter than `or`.)

A) True
B) False
C) None
D) Error

---

**Q6.** What is the bug in this code?
```python
x = 5
if x = 5:
    print("five")
```

A) The condition should be `x == 5`
B) The indentation is wrong
C) `print` needs different parentheses
D) There is no bug

---

**Q7.** For which value of `y` will the `else` branch run?
```python
x = 10
if x < y:
    print("x is smaller")
elif x > y:
    print("x is larger")
else:
    print("equal")
```

A) `y = 5`
B) `y = 10`
C) `y = 15`
D) No value of y makes else run

---

**Q8.** What does this code print when `score = 75`?
```python
if score >= 90:
    print("A")
if score >= 80:
    print("B")
if score >= 70:
    print("C")
if score >= 60:
    print("D")
```

A) "C" only
B) "C" and "D"
C) "A", "B", "C", and "D"
D) Nothing

---

**Q9.** What is the correct expression for "x is between 0 and 100, inclusive"?

A) `0 < x < 100`
B) `x >= 0 and x <= 100`
C) `0 <= x <= 100`
D) Both B and C are correct

---

**Q10.** Trace this code with `x = 3`. What does it print?
```python
result = ""
if x % 2 == 0:
    result += "even"
else:
    result += "odd"
if x > 2:
    result += "_big"
print(result)
```

A) "odd"
B) "even_big"
C) "odd_big"
D) "oddeven_big"

---
---

## 📋 Answer Key — Day 5

| Q | Answer | Explanation |
|---|---|---|
| 1 | C — "big" then "done" | "done" is at the same indentation as `if`, meaning it's outside the if-block and always runs |
| 2 | B — False | `and` requires BOTH operands to be True for the result to be True |
| 3 | B — `if x == 5:` | No `then` keyword in Python, needs `==` (not `=`) for comparison, lowercase `if`, and a trailing colon |
| 4 | A — "positive" only | The first condition (`x > 0`) is True, so its block runs and the `elif`/`else` are skipped entirely — even though `x > 5` is also true |
| 5 | B — False | `not True` evaluates first to `False`; then `False or False` is `False` |
| 6 | A — should be `x == 5` | `=` is the assignment operator; `==` is needed for equality comparison inside a condition |
| 7 | B — `y = 10` | When `x == y` (both 10), neither `if` nor `elif` condition is True, so control falls to `else` |
| 8 | B — "C" and "D" | These are four independent `if` statements, not `elif` chains — both `score >= 70` and `score >= 60` are True for `score = 75` |
| 9 | D — Both B and C | Python supports Python-specific chained comparisons (`0 <= x <= 100`), which is equivalent to the `and` version |
| 10 | C — "odd_big" | x=3 is odd (3 % 2 = 1, not 0) → result becomes "odd"; then 3 > 2 is True → result becomes "odd_big" |

---

## Week 1 Complete!

If you scored well on most of these questions, you're ready for Week 2.
If several answers surprised you, spend extra time this weekend re-reading
the relevant textbook sections before moving on.

*Next: `04_ASSIGNMENTS/week_01/weekend_assignment_01.md`*
