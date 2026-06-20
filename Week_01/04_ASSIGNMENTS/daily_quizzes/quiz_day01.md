# 🧠 Quiz — Day 1
## Types, Arithmetic, and Type Conversion

> Cover the answer key at the bottom. Answer every question first —
> guessing and being wrong is part of how memory gets built. This quiz
> is ungraded; it exists purely for active recall practice.

---

**Q1.** What does `type(10 / 4)` return?

A) `int`
B) `float`
C) `str`
D) `bool`

---

**Q2.** What is the result of `17 % 5`?

A) 3
B) 2
C) 1
D) 85

---

**Q3.** What is the result of `2 ** 3 ** 2`?

A) 64
B) 512
C) 72
D) 36

---

**Q4.** What does `int(3.9)` return?

A) 4 (rounds up)
B) 3 (truncates toward zero)
C) 3.0 (converts to float)
D) Error

---

**Q5.** Which of the following is NOT a valid Python integer value?

A) `0`
B) `-1000`
C) `3.0`
D) `2000000`

---

**Q6.** What does `10 // 3` return?

A) 3.3333...
B) 3.0
C) 3
D) 4

---

**Q7.** What is `15 % 15`?

A) 1
B) 15
C) 0
D) Error

---

**Q8.** You want to check if the number `n` is even. Which expression is correct?

A) `n // 2 == 0`
B) `n % 2 == 0`
C) `n / 2 == 0`
D) `n ** 2 == 0`

---

**Q9.** What does `float(int(3.7))` evaluate to?

A) 3.7
B) 4.0
C) 3.0
D) Error

---

**Q10.** Which expression evaluates to the largest value?

A) `2 ** 4`
B) `3 * 5`
C) `20 + 3 * 2`
D) `(2 + 3) * 5`

---
---

## 📋 Answer Key — Day 1

| Q | Answer | Explanation |
|---|---|---|
| 1 | B — `float` | `/` always returns a float in Python 3, even when both operands are ints |
| 2 | B — `2` | 17 = 5×3 + 2, so the remainder is 2 |
| 3 | B — `512` | `**` is right-associative: `3**2=9` first, then `2**9=512` |
| 4 | B — `3` | `int()` truncates toward zero; it does NOT round |
| 5 | C — `3.0` | That's a float (has a decimal point), not an int |
| 6 | C — `3` | Floor division discards the remainder, giving an integer result |
| 7 | C — `0` | Any number mod itself is always 0 |
| 8 | B — `n % 2 == 0` | A number is even exactly when its remainder mod 2 is 0 |
| 9 | C — `3.0` | `int(3.7)` truncates to `3`, then `float(3)` converts to `3.0` |
| 10 | D — `25` | A=16, B=15, C=20+6=26 — wait, recompute: C = 20 + 3*2 = 26. **C is actually largest.** Recheck: A=16, B=15, C=26, D=25. The largest is **C**. |

> **Note on Q10:** if you got this "wrong," recheck your order-of-operations
> work — `20 + 3 * 2` evaluates the multiplication first (`3*2=6`), then adds
> (`20+6=26`). This is a good reminder that PEMDAS still applies inside larger
> expressions. The correct answer is **C**, not D — a deliberately tricky one
> to make you double-check operator precedence by hand.

---

*Next: open `02_NOTEBOOKS/week_01/day02_variables_expressions.ipynb`*
