import pytest
from mailFronCSV import load_emails_from_csv
from emailValidator import validate_email_format

@pytest.mark.parametrize("email, expected", load_emails_from_csv())
def test_email_validation(email, expected):
    assert validate_email_format(email) == expected