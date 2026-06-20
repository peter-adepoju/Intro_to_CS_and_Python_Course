# 🧠 Quiz — Day 4
## Input, Output, and Formatting

---

**Q1.** What type does `input()` always return, regardless of what the
user types?

A) `int`
B) `float`
C) `str`
D) Whatever type the user types

---

**Q2.** What does this print?
```python
print("a", "b", "c", sep="-")
```

A) `a b c`
B) `a-b-c`
C) `abc`
D) `-a-b-c-`

---

**Q3.** Which is the correct way to get an integer from the user?

A) `x = input("Enter: ")`
B) `x = int("Enter: ")`
C) `x = int(input("Enter: "))`
D) `x = input(int("Enter: "))`

---

**Q4.** Given `pi = 3.14159`, what does `f"{pi:.2f}"` produce?

A) `"3.14159"`
B) `"3.14"`
C) `"3.1"`
D) `"pi"`

---

**Q5.** What is the difference between `\n` and `\t` in a string?

A) `\n` is a tab, `\t` is a newline
B) `\n` is a newline, `\t` is a tab
C) Both are newlines
D) Both are tabs

---

**Q6.** What does `f"{1234567:,}"` produce?

A) `"1234567"`
B) `"1,234,567"`
C) `"1.234.567"`
D) Error

---

**Q7.** What does this print?
```python
print("Hello", end="")
print("World")
```

A) `Hello World`
B) `HelloWorld`
C) `Hello` then `World` on a separate line
D) `Hello\nWorld`

---

**Q8.** A user types `"3.14"` when asked. After `x = float(input(...))`,
what is `type(x)`?

A) `str`
B) `int`
C) `float`
D) Error

---

**Q9.** Which f-string correctly formats `0.8532` as `"85.3%"`?

A) `f"{0.8532 * 100:.1f}%"`
B) `f"{0.8532:.1%}"`
C) Both A and B
D) Neither

---

**Q10.** What does this print?
```python
name = "Bob"
score = 87
print(f"{'Name':<8} {'Score':>6}")
print(f"{name:<8} {score:>6}")
```

A) Two lines of unaligned text
B) Two lines forming an aligned table — "Name" left-padded in an 8-char field, "Score" right-padded in a 6-char field
C) Error — you can't mix alignment specifiers
D) Just `"Name Score"`

---
---

## 📋 Answer Key — Day 4

| Q | Answer | Explanation |
|---|---|---|
| 1 | C — `str` | `input()` ALWAYS returns a string. You must convert manually with `int()`, `float()`, etc. |
| 2 | B — `"a-b-c"` | The `sep=` keyword argument changes the separator placed between printed arguments |
| 3 | C — `int(input("..."))` | Wrap the call to `input()` inside `int()` to convert the returned string into an integer |
| 4 | B — `"3.14"` | `.2f` format spec rounds and displays exactly 2 decimal places |
| 5 | B — `\n` is newline, `\t` is tab | Two of the most commonly used escape sequences — worth memorizing |
| 6 | B — `"1,234,567"` | The `,` format spec inserts thousands separators automatically |
| 7 | B — `"HelloWorld"` | `end=""` suppresses the default trailing newline, so the next `print()` continues on the same line |
| 8 | C — `float` | `float()` converts the string `"3.14"` into the float value `3.14` |
| 9 | C — Both A and B | A manually multiplies by 100 and formats as a float; B uses the built-in `%` format spec which does the multiplication automatically |
| 10 | B — an aligned table | `<8` left-aligns within an 8-character field, `>6` right-aligns within a 6-character field, producing neat columns |

---

*Next: open `02_NOTEBOOKS/week_01/day05_branching.ipynb`*
