import ast
import importlib
import inspect
import textwrap

import pytest

import assignment


@pytest.fixture
def s():
    return importlib.reload(assignment)


def check_no_list_methods(function):
    tree = ast.parse(textwrap.dedent(inspect.getsource(function)))
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr in ["append", "pop", "insert", "remove", "extend", "clear"]:
                pytest.fail(
                    function.__name__ + "() uses ." + node.func.attr + "(). "
                    "Change TopOfStack and use Stack[TopOfStack] instead."
                )


def test1_initial_stack(s):
    assert s.Stack == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert s.TopOfStack == -1


def test1_push(s):
    assert s.Push(15) == True
    assert s.TopOfStack == 0
    assert s.Stack[0] == 15
    assert s.Push(27) == True
    assert s.TopOfStack == 1
    assert s.Stack[1] == 27


def test1_push_when_full(s):
    for x in range(10):
        assert s.Push(x) == True
    assert s.TopOfStack == 9
    assert s.Push(99) == False
    assert s.TopOfStack == 9
    assert s.Stack == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test1_pop(s):
    s.Push(10)
    s.Push(20)
    s.Push(30)
    assert s.Pop() == 30
    assert s.TopOfStack == 1
    assert s.Pop() == 20
    assert s.Pop() == 10
    assert s.TopOfStack == -1


def test1_pop_when_empty(s):
    assert s.Pop() == -1
    assert s.TopOfStack == -1
    s.Push(5)
    s.Pop()
    assert s.Pop() == -1
    assert s.TopOfStack == -1


def test1_uses_top_of_stack(s):
    check_no_list_methods(s.Push)
    check_no_list_methods(s.Pop)
    for x in range(12):
        s.Push(x)
    for x in range(12):
        s.Pop()
    assert len(s.Stack) == 10


def test2_peek(s):
    assert s.Peek() == -1
    s.Push(8)
    s.Push(3)
    assert s.Peek() == 3
    assert s.Peek() == 3
    assert s.TopOfStack == 1
    s.Pop()
    assert s.Peek() == 8


def test2_is_empty_and_size(s):
    assert s.IsEmpty() == True
    assert s.Size() == 0
    s.Push(4)
    s.Push(6)
    assert s.IsEmpty() == False
    assert s.Size() == 2
    s.Pop()
    s.Pop()
    assert s.IsEmpty() == True
    assert s.Size() == 0


def test2_reverse_list(s):
    assert s.ReverseList([1, 2, 3]) == [3, 2, 1]
    assert s.TopOfStack == -1
    assert s.ReverseList([42]) == [42]
    assert s.ReverseList([]) == []
    assert s.ReverseList([5, 9, 2, 7]) == [7, 2, 9, 5]


def test2_reverse_list_when_full(s, capsys):
    result = s.ReverseList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    assert result == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert capsys.readouterr().out.count("Stack full") == 1


@pytest.mark.parametrize("expression", [
    "()",
    "([]{})",
    "{[()()]}",
    "(a + b) * [c - d]",
    "no brackets here",
    "",
])
def test3_balanced(s, expression):
    assert s.Balanced(expression) == True


@pytest.mark.parametrize("expression", [
    "(",
    ")",
    "(]",
    "([)]",
    "(()",
    "())",
    "{[}]",
])
def test3_not_balanced(s, expression):
    assert s.Balanced(expression) == False


def test3_starts_empty(s):
    assert s.Balanced("((") == False
    assert s.Balanced("()") == True
    assert s.Balanced("[[[") == False
    assert s.Balanced("[]") == True


def test3_stack_full(s):
    assert s.Balanced("(((((((((())))))))))") == True
    assert s.Balanced("((((((((((()))))))))))") == False
