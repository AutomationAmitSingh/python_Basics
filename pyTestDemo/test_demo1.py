# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
import pytest


@pytest.mark.smoke
def test_first_program():
    print("Amit Singh")


@pytest.mark.xfail
def test_second_greet_credit_card():
    print("Good Morning")


def test_cross_browser(cross_browser):
    print(cross_browser[1])