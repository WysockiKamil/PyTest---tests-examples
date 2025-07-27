import pytest
from fizzbuzz import fizzbuzz

@pytest.mark.parametrize("number, expected", [
    (3, "Fizz"),
    (5, "Buzz"),
    (15, "FizzBuzz"),
    (7, "7"),
    (0, "FizzBuzz"),
    (-3, "Fizz"),
    (-5, "Buzz")
])
def test_fizzbuzz(number, expected):
    assert fizzbuzz(number) == expected

@pytest.mark.parametrize("invalid_input", ["not a number", None, [1, 2, 3], {"a": 1}])
def test_fizzbuzz_invalid_type(invalid_input):
    with pytest.raises(TypeError, match="Argument must be an int or float"):
        fizzbuzz(invalid_input)