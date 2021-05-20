from hypothesis import given, strategies as st
from cmath import isclose
from calculator import Calculator


x = Calculator()


@given(n=st.floats(min_value=-10000, max_value=100000))
def test_add(n):
    x.reset()
    res = x.add(n)
    assert res == n


def test_multiplication(n):
    x.reset()
    res: int = x.add(1)
    res = x.multiply(n)
    assert res == n


def test_subtraction(n):
    x.reset()
    res = x.subtact(n)
    assert res == -n


def test_division(n):
    x.reset()
    res: int = x.add(100)
    res = x.devide(n)
    try:
        assert res == (100 / n)
    except ZeroDivisionError:
        return ZeroDivisionError


def test_root(n):
    x.reset()
    res = x.add(100)
    res = x.root(n)
    try:
        assert isclose(res, 100 ** (1 / n))
    except ZeroDivisionError:
        return ZeroDivisionError


def test_reset():
    x.reset()
    res = x.reset()
    assert res == 0


if __name__ == "__main__":
    test_add()
    test_subtraction()
    test_multiplication()
    test_division()
    test_root()
    test_reset()
