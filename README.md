# Exam

**Rules**

- Write every search yourself. Do **not** use `.index()`, `.count()` or
  `.reverse()`. (`for ... in` loops are fine.)
- Exercise 2 must use **binary search** — a linear scan will lose marks even
  if the answer is correct.
- Every attribute must be created inside `__init__` using `self.something = ...`
- When a function or method says it **returns** something, use `return` — do not `print`.

---

## Exercise 1 (3 marks)

**Problem:**

`find_last(data, target)`

Use **linear search** to return the index of the **last** place where
`target` appears in `data`. Return `-1` if it is not there.

Do not change the list.

**Example:**

    Example Input:
        data   = [4, 2, 4, 9, 4]
        target = 4

    Program Output:
        4

    Example Input:
        data   = [4, 2, 4, 9]
        target = 4

    Program Output:
        2

    Example Input:
        data   = [10, 20, 30]
        target = 99

    Program Output:
        -1

*Hint:* do not stop at the first match — keep going to the end and remember
the last match you saw.

---

## Exercise 2 (3 marks)

**Problem:**

`binary_search(data, target)`

`data` is a **sorted** list. Use **binary search** to return the index of
`target`, or `-1` if it is not in the list.

**Example:**

    Example Input:
        data   = [1, 3, 5, 7, 9, 11]
        target = 7

    Program Output:
        3

    Example Input:
        data   = [1, 3, 5, 7, 9, 11]
        target = 4

    Program Output:
        -1

    Example Input:
        data   = []
        target = 1

    Program Output:
        -1

Your function will also be tested on a list of 100,000 numbers.

---

## Exercise 3 (3 marks)

**Problem:**

- Create a `Product` class for an item in a shop.
    - Attributes:
        - `name`
        - `price` → the price of **one** item
        - `stock` → how many are in the shop
    - Methods:
        - `sell(amount)` → takes `amount` off `stock` and **returns** `True`.
          If `amount` is `0` or less, or more than the stock, nothing changes
          and it **returns** `False`. Selling exactly all the stock is allowed.
        - `restock(amount)` → adds `amount` to `stock` and **returns** `True`.
          If `amount` is `0` or less, nothing changes and it **returns** `False`.
        - `value()` → **returns** `price` × `stock`

**Example:**

    Input:
      p = Product("Pen", 500, 20)
      print(p.sell(3))
      print(p.sell(50))
      print(p.stock)
      print(p.restock(-5))
      print(p.value())

    Output:
      True
      False
      17
      False
      8500

---

## Exercise 4 (3 marks)

**Problem:**

A `Shop` stores `Product` **objects** from Exercise 3.

- Create a `Shop` class.
    - Attributes:
        - `name`
        - `products` → starts as an **empty list**
    - Methods:
        - `add_product(product)` → adds a `Product` object to `products`
        - `count()` → **returns** how many products the shop has
        - `find_product(name)` → use **linear search** to find the product with
          that name and **return the Product object**. If there is none,
          **return** `None`.
        - `total_value()` → **returns** the total `value()` of all products.
          An empty shop returns `0`.

**Important:** create the empty list inside `__init__`. Every shop must have
its own list.

**Example:**

    Input:
      shop = Shop("School Shop")
      shop.add_product(Product("Pen", 500, 20))
      shop.add_product(Product("Ruler", 800, 5))

      print(shop.count())
      print(shop.find_product("Ruler").price)
      print(shop.find_product("Eraser"))
      print(shop.total_value())

    Output:
      2
      800
      None
      14000

`total_value()` is 500 × 20 + 800 × 5 = 14000.

---

## How to test your work

    pytest -v
