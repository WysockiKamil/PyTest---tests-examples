import pytest
from factorial import factorial

@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (10, 3628800),
    (15, 1307674368000)
])
def test_factorial(n, expected):
    assert factorial(n) == expected

@pytest.mark.parametrize("invalid_input", ["abc", None, [10], {"temp": 15}])
def test_factorial_invalid_type(invalid_input):
    with pytest.raises(TypeError, match="Podana musi być liczba całkowita"):
        factorial("abc")

@pytest.mark.parametrize("negative_input", [-1, -5, -10])
def test_factorial_negative_input(negative_input):
    with pytest.raises(ValueError, match="Podana musi być liczba nieujemna"):
        factorial(negative_input)