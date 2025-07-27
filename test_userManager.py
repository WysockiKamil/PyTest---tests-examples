import pytest
from userManagment import User, UserManager

@pytest.fixture
def user():
    return User("Jan", "Kowalski", "jan.kowalski@mail.pl", 25)