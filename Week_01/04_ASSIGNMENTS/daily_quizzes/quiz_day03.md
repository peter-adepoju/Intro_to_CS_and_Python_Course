# 🧠 Quiz — Day 3
## Strings, Indexing, and Slicing

---

**Q1.** What does `"abc"[1]` return?

A) `"a"`
B) `"b"`
C) `"c"`
D) IndexError

---

**Q2.** Given `s = "Python"`, what is `s[-1]`?

A) `"P"`
B) `"h"`
C) `"n"`
D) Error

---

**Q3.** What does `len("Hello, World!")` return?

A) 10
B) 12
C) 13
D) 11

---

**Q4.** What is `"ha" * 3`?

A) `"ha ha ha"`
B) `"hahaha"`
C) `"ha3"`
D) Error — can't multiply a string by an int

---

**Q5.** Given `s = "abcdefgh"`, what does `s[2:5]` return?

A) `"bcd"`
B) `"cde"`
C) `"cdef"`
D) `"bcde"`

---

**Q6.** Which of these will raise an `IndexError`?

A) `"hello"[4]`
B) `"hello"[-5]`
C) `"hello"[5]`
D) `"hello"[0]`

---

**Q7.** What does `"abcde"[::-1]` return?

A) `"abcde"`
B) `"edcba"`
C) `"ace"`
D) Error

---

**Q8.** Can you do `s[0] = 'A'` where `s = "hello"`?

A) Yes — it changes the first character to `'A'`
B) No — strings are immutable; this raises a `TypeError`

---

**Q9.** What does `"hello" + "world"` produce?

A) `"hello world"`
B) `"helloworld"`
C) Error
D) `"hello+world"`

---

**Q10.** Given `s = "programming"`, what does `s[1:8:2]` return?

(Index reference: p=0, r=1, o=2, g=3, r=4, a=5, m=6, m=7, i=8, n=9, g=10)

A) `"rorm"`
B) `"rgam"`
C) `"roam"`
D) `"rormi"`

---
---

## 📋 Answer Key — Day 3

| Q | Answer | Explanation |
|---|---|---|
| 1 | B — `"b"` | Indexing starts at 0: `'a'`=0, `'b'`=1, `'c'`=2 |
| 2 | C — `"n"` | `s[-1]` is always the last character of the string |
| 3 | C — 13 | Count every character including the comma and space: H-e-l-l-o-,-(space)-W-o-r-l-d-! = 13 |
| 4 | B — `"hahaha"` | String repetition concatenates copies with no separator added |
| 5 | B — `"cde"` | Indices 2, 3, 4 are included; index 5 is excluded (stop is exclusive) — those are c, d, e |
| 6 | C — `"hello"[5]` | Valid indices for a 5-character string are 0–4 (positive) or -5 to -1 (negative); 5 is out of range |
| 7 | B — `"edcba"` | A step of -1 walks backward through the whole string, reversing it |
| 8 | B — No, raises TypeError | Strings are immutable in Python — you must build a new string instead |
| 9 | B — `"helloworld"` | `+` concatenates with no space inserted automatically |
| 10 | B — `"rgam"` | s[1]='r', s[3]='g', s[5]='a', s[7]='m' — stepping by 2 from index 1 up to (not including) 8 |

---

*Next: open `02_NOTEBOOKS/week_01/day04_input_output.ipynb`*
