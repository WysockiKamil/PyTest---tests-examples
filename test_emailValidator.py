import pytest
from email_validator import validate_email, EmailNotValidError
from emailValidator import validate_email_format

@pytest.mark.parametrize("email, expected", [
    ("jan.kowalski@wp.pl", True),
    ("jan@wp.pl", True),
    ("92@wp.pl", True),
    ("invalid-email", False),
    (".@example.com", False),
    ("@wp.pl", False),
    ("test@.com", False),
    ("test@", False),
    ("test@com", False),
    ("test@wp..pl", False),
])
def test_validate_email_format(email, expected):
    assert validate_email_format(email) == expected;