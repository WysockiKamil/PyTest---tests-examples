from email_validator import validate_email, EmailNotValidError

def validate_email_format(email: str):
    try:
        valid = validate_email(email)
        print(f"Email '{email}' jest poprawny!")
        return True
    except EmailNotValidError as e:
        print(f"Email '{email}' jest niepoprawny!")
        return False