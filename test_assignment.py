import ast
import inspect
import textwrap

import pytest

from assignment import find_last, binary_search, Product, Shop


class CountingList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.accesses = 0

    def __getitem__(self, index):
        self.accesses += 1
        return super().__getitem__(index)

    def __iter__(self):
        self.accesses += len(self)
        return super().__iter__()

    def __contains__(self, value):
        self.accesses += len(self)
        return super().__contains__(value)

    def index(self, *args):
        self.accesses += len(self)
        return super().index(*args)

    def count(self, value):
        self.accesses += len(self)
        return super().count(value)


def check_not_used(function, banned):
    tree = ast.parse(textwrap.dedent(inspect.getsource(function)))
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr in banned:
                pytest.fail(function.__name__ + " uses ." + node.func.attr + "(). Write the search yourself.")


@pytest.mark.parametrize("data, target, expected", [
    [[4, 2, 4, 9, 4], 4, 4],
    [[4, 2, 4, 9], 4, 2],
    [[10, 20, 30], 10, 0],
    [[10, 20, 30], 30, 2],
    [["a", "b", "a", "c"], "a", 2],
])
def test1_find_last(data, target, expected):
    assert find_last(data, target) == expected


@pytest.mark.parametrize("data, target", [
    [[10, 20, 30], 99],
    [[], 5],
    [[7], 8],
])
def test1_not_found(data, target):
    assert find_last(data, target) == -1


def test1_no_shortcuts():
    check_not_used(find_last, ["index", "count", "reverse", "rindex"])
    data = [3, 1, 3, 2]
    assert find_last(data, 3) == 2
    assert data == [3, 1, 3, 2]


@pytest.mark.parametrize("data, target, expected", [
    [[1, 3, 5, 7, 9, 11], 7, 3],
    [[1, 3, 5, 7, 9, 11], 1, 0],
    [[1, 3, 5, 7, 9, 11], 11, 5],
    [[5], 5, 0],
    [[-8, -3, 0, 4, 10], -3, 1],
])
def test2_found(data, target, expected):
    assert binary_search(data, target) == expected


@pytest.mark.parametrize("data, target", [
    [[1, 3, 5, 7, 9, 11], 4],
    [[1, 3, 5, 7, 9, 11], 0],
    [[1, 3, 5, 7, 9, 11], 12],
    [[5], 2],
    [[], 1],
])
def test2_not_found(data, target):
    assert binary_search(data, target) == -1


def test2_efficiency():
    check_not_used(binary_search, ["index", "count"])
    data = CountingList(range(0, 200000, 2))
    assert binary_search(data, 123456) == 61728
    checked = data.accesses
    assert checked < 200, "Too many elements checked (" + str(checked) + "). Use binary search."
    data = CountingList(range(0, 200000, 2))
    assert binary_search(data, 123457) == -1
    checked = data.accesses
    assert checked < 200, "Too many elements checked (" + str(checked) + "). Use binary search."


def test3_new_product():
    p = Product("Pen", 500, 20)
    assert p.name == "Pen"
    assert p.price == 500
    assert p.stock == 20


def test3_sell():
    p = Product("Pen", 500, 20)
    assert p.sell(3) == True
    assert p.stock == 17
    assert p.sell(50) == False
    assert p.stock == 17
    assert p.sell(0) == False
    assert p.sell(-2) == False
    assert p.stock == 17
    assert p.sell(17) == True
    assert p.stock == 0


def test3_restock_and_value():
    p = Product("Notebook", 1500, 4)
    assert p.value() == 6000
    assert p.restock(6) == True
    assert p.stock == 10
    assert p.restock(0) == False
    assert p.restock(-5) == False
    assert p.stock == 10
    assert p.value() == 15000


def test4_add_and_count():
    shop = Shop("School Shop")
    assert shop.name == "School Shop"
    assert shop.products == []
    assert shop.count() == 0
    pen = Product("Pen", 500, 20)
    shop.add_product(pen)
    shop.add_product(Product("Ruler", 800, 5))
    assert shop.count() == 2
    assert shop.products[0] is pen
    other = Shop("Other Shop")
    assert other.products == []
    assert other.count() == 0


def test4_find_product():
    shop = Shop("School Shop")
    assert shop.find_product("Pen") is None
    pen = Product("Pen", 500, 20)
    ruler = Product("Ruler", 800, 5)
    shop.add_product(pen)
    shop.add_product(ruler)
    assert shop.find_product("Ruler") is ruler
    assert shop.find_product("Pen") is pen
    assert shop.find_product("Eraser") is None


def test4_total_value():
    shop = Shop("School Shop")
    assert shop.total_value() == 0
    shop.add_product(Product("Pen", 500, 20))
    shop.add_product(Product("Ruler", 800, 5))
    assert shop.total_value() == 14000
    shop.find_product("Pen").sell(10)
    assert shop.total_value() == 9000
