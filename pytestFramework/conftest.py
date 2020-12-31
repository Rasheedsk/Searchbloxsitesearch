import pytest

@pytest.fixture()
def dataload():
    print("I wil print first")
    return ["Rasheed", "28", "7899298070"]