import pytest
from unique import uniqueElements
@pytest.mark.parametrize("lst, expected", [
    ([1, 2, 2, 1, 3, 4, 4], [1, 2, 3, 4]),
    (["a", "b", "a", "c"], ["a", "b", "c"]),
    ([1, 1.0, 2, 2.0], [1, 1.0, 2, 2.0]),
    ([True, False, True], [True, False]),
    ([], []),
    ([None, None, 1, 2], [None, 1, 2]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, "1", 2, "2", True, False, True], [1, "1", 2, "2", True, False]),

])
def test_uniqueElements(lst, expected):    
    assert uniqueElements(lst) == expected