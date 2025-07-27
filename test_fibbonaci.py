import pytest
from fibbonaci import fibbonaci

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55)
])
def test_fibbonaci(n, expected):
    assert fibbonaci(n) == expected

@pytest.mark.parametrize("invalid_input", ["abc", None, [10], {"temp": 15}])
def test_factorial_invalid_type(invalid_input):
    with pytest.raises(TypeError, match="Podana musi być liczba całkowita"):
        fibbonaci("abc")

@pytest.mark.parametrize("negative_input", [-1, -5, -10])
def test_factorial_negative_input(negative_input):
    with pytest.raises(ValueError, match="Podana musi być liczba nieujemna"):
        fibbonaci(negative_input)