import pytest
from calculator import add, subtract, multiply, divide

@pytest.mark.parametrize("addend1, addend2, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (-5, -1, -6),
    (-5, 200, 195),
    (200, -5, 195)
])
def test_add(addend1, addend2, expected):
    assert add(addend1, addend2) == expected

@pytest.mark.parametrize("minuend, subtrahend, expected", [
    (5, 3, 2),
    (0, 0, 0),
    (-1, -1, 0),
    (-5, -1, -4),
    (-5, 200, -205),
    (200, -5, 205)
])
def test_subtract(minuend, subtrahend, expected):
    assert subtract(minuend, subtrahend) == expected

@pytest.mark.parametrize("factor1, factor2, expected", [
    (2, 3, 6),
    (-1, 1, -1),
    (0, 5, 0),
    (-6, -1, 6),
    (-5, 200, -1000),
    (200, -5, -1000)
])
def test_multiply( factor1, factor2, expected):
    assert multiply(factor1, factor2) == expected

@pytest.mark.parametrize("dividend, divisor, expected", [
    (6, 3, 2),
    (-6, -2, 3),
    (-10, 2, -5),
    (10, -2, -5)
])
def test_divide(dividend, divisor, expected):
    assert divide(dividend, divisor) == expected

@pytest.mark.parametrize("dividend, divisor", [
    (1, 0),
    (0, 0)
])
def test_divide_by_zero(dividend, divisor):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(dividend, divisor)

@pytest.mark.parametrize("dividend, divisor", [
    (0, 1)
])
def test_zero_divided(dividend, divisor):
    with pytest.raises(ValueError, match="Zero cannot be divided"):
        divide(dividend, divisor)