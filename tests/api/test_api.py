import pytest
"""
class User:

    def __init__(self) -> None:
        self.name = "Natalia"
        self.second_name = "Shylina"

@pytest.fixture
def user():
    yield User() """


@pytest.mark.change
def test_remove_name(user):
    user.name = ' '
    assert user.name == ' '


@pytest.mark.check
def test_name(user):
    assert user.name == 'Natalia'    


@pytest.mark.check
def test_second_name(user):
    assert user.second_name == 'Shylina'        