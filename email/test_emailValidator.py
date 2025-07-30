import pytest
from emailValidator import EmailValidator


@pytest.mark.parametrize("email, expected", [
    ("jan.kowalski@wp.pl", True),
    ("invalid-email", False),
    ("test@.com", False),
    ("anna.nowak@gmail.com", True),
    ("@missinglocal.com", False),
    ("noatsymbol.com", False),
])
def test_strict_mode(email, expected):
    validator = EmailValidator(strict=True)
    assert validator.is_valid(email) == expected


@pytest.mark.parametrize("email, expected", [
    ("jan.kowalski@wp.pl", True),
    ("invalid-email", False),
    ("test@com", True),  # zaakceptowany w trybie uproszczonym
    ("@example.com", False),  # uproszczona walidacja
    ("noatsymbol.com", False),
])
def test_relaxed_mode(email, expected):
    validator = EmailValidator(strict=False)
    assert validator.is_valid(email) == expected

@pytest.mark.parametrize("email", [["abc@wp.pl"], None, [10], {"temp": 15}])        
def test_invalid_email_type(email):
    validator = EmailValidator()
    with pytest.raises(TypeError, match="Email must be a string"):
        validator.is_valid(email)
