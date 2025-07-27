import pytest
from isEven import isEven

@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, False),
    (0, True),
    (-2, True),
    (-3, False),
    (4.0, True),
    (5.5, False),
    (1.0, False)
])
def test_isEven(number, expected):
    assert isEven(number) == expected

@pytest.mark.parametrize("invalid_input", ["abc", None, [10], {"temp": 15}])
def test_isEven_type_error(invalid_input):
    with pytest.raises(TypeError, match="Argument must be a number"):
        isEven(invalid_input)