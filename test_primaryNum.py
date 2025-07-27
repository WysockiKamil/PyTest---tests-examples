import pytest
from primaryNum import isPrimary

@pytest.mark.parametrize("num, expected", [
    (-3, False),
    (-1, False),
    (0, False),
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (16, False),
    (17, True),
    (20, False),
    (25, False)
])
def test_isPrimary(num, expected):
    assert isPrimary(num) == expected

def test_isPrimary_invalid():
    with pytest.raises(TypeError):
        isPrimary("not a number")
    with pytest.raises(TypeError):
        isPrimary(None)
    with pytest.raises(TypeError):
        isPrimary([1, 2, 3])