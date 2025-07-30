from email_validator import validate_email, EmailNotValidError

class EmailValidator:
    def __init__(self, strict: bool = True):
        self.strict = strict

    def is_valid(self, email: str) -> bool:
        if not isinstance(email, str):
            raise TypeError("Email must be a string")

        if self.strict:
            try:
                validate_email(email)
                return True
            except EmailNotValidError:
                return False
        else:
            # Tryb uproszczony: wystarczy znak @ i coś po nim
            if "@" in email:
                local, _, domain = email.partition("@")
                return bool(local) and bool(domain)
            return False