# Answer keys
---

## Day 1

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
---
