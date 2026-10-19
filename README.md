# Python Stack

Read the Abstract Data Types lecture (Stack section) before you start.
Abstract Data Types Lecture:
https://drive.google.com/file/d/1jXGQdSvuUYjGXl-PUuHMUzKWEBGQoARL/view?usp=sharing

**Rules for this assignment**

- Do **not** use `.append()` or `.pop()` inside `Push()` and `Pop()`.
  Change `TopOfStack` yourself and use `Stack[TopOfStack]`. The tests check for this.
- Functions **return** their answer. Only print when the exercise says so.
- Use `global Stack, TopOfStack` in every function that changes them.

---

## Exercise 1

**Problem:**

Build a stack that holds **10** integers.

- `Stack` → a global array of **10** elements, all set to `-1`
- `TopOfStack` → a global integer, set to `-1` (the stack is empty)

Then write two functions:

- `Push(DataToPush)`
  - If the stack is full (`TopOfStack` is 9), return `False`
  - Otherwise add 1 to `TopOfStack`, store `DataToPush` at `Stack[TopOfStack]`,
    and return `True`

- `Pop()`
  - If the stack is empty (`TopOfStack` is -1), return `-1`
  - Otherwise return the item at `Stack[TopOfStack]`, and take 1 off `TopOfStack`

**Careful with the order in Pop():** read the item **first**, then move `TopOfStack`.

**Example:**

    Input:
      print(Push(10))
      print(Push(20))
      print(Push(30))
      print(Pop())
      print(Pop())
      print(TopOfStack)

    Output:
      True
      True
      True
      30
      20
      0

    Input (on an empty stack):
      print(Pop())

    Output:
      -1

---

## Exercise 2

**Problem:**

Write four more functions that use the stack from Exercise 1.

- `Peek()` → returns the top item **without removing it**. Returns `-1` if the stack is empty.
- `IsEmpty()` → returns `True` if the stack is empty, otherwise `False`.
- `Size()` → returns **how many items** are in the stack.
- `ReverseList(Numbers)` → `Numbers` is a list of integers.
  - Push each number onto the stack.
  - If `Push()` returns `False`, print `Stack full` **once** and stop pushing.
  - Then pop **every** item off the stack into a new list, and return that list.

*Hint:* `Size()` is **not** `len(Stack)` — the array always has 10 elements.
Think about what `TopOfStack` tells you.

**Example:**

    Input:
      Push(8)
      Push(3)
      print(Peek())
      print(Size())
      print(IsEmpty())

    Output:
      3
      2
      False

    Input (on an empty stack):
      print(ReverseList([5, 9, 2, 7]))

    Output:
      [7, 2, 9, 5]

    Input (on an empty stack):
      print(ReverseList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

    Output:
      Stack full
      [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

Only the first 10 numbers fit. Numbers 11 and 12 are never pushed.

---

## Exercise 3

**Problem:**

`Balanced(Expression)`

`Expression` is a string. Return `True` if its brackets are **balanced**,
otherwise `False`.

Brackets are balanced when every opening bracket `(` `[` `{` has a matching
closing bracket `)` `]` `}` of the **same type**, closed in the **right order**.
All other characters are ignored.

Use your stack:

1. **Empty the stack first** by setting `TopOfStack` to `-1`.
2. Go through the string one character at a time.
3. Opening bracket → `Push()` it. If `Push()` returns `False`, return `False`.
4. Closing bracket → `Pop()` the top item. If it is **not** the matching opening
   bracket, return `False`. (If the stack was empty, `Pop()` returns `-1` — that doesn't match either.)
5. At the end, the brackets are balanced **only if the stack is empty**.

**Example:**

    Input:                            Output:
      Balanced("([]{})")                True
      Balanced("(a + b) * [c - d]")     True
      Balanced("([)]")                  False    ) closes [ - wrong type
      Balanced("(()")                   False    one ( is never closed
      Balanced("())")                   False    the last ) has nothing to close

---
