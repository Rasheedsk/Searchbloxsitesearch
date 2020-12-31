import pytest


@pytest.mark.smoke
def test_myfirstTestcase():
    A = 18
    B = 10
    if A > B:
        print("A is greater than B")
    else:
        print("B is less than A")

@pytest.mark.skip
def test_mySecondTestcase():
    print("This is my last testcase")