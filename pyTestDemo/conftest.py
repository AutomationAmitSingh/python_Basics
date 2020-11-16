import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print(" I will execute last")


@pytest.fixture()
def data_load():
    print("user profile data is being created")
    return ["Rahul","Shetty","rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome","Rahul","shetty"), ("Firefox","shetty"), ("IE","SS")])
def cross_browser(request):
    return request.param
