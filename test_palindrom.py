import pytest
from palindrom import ifPalindrome

@pytest.mark.parametrize("word, expected", [
    ("radar", True),
    ("RADAR", True),
    ("Level", True),
    ("hello", False),
    ("Kobyła ma mały bok", True)
])
def test_ifPalindrome(word, expected):
    assert ifPalindrome(word) == expected