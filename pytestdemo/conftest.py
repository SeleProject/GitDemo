import pytest


@pytest.fixture(scope="class")
def setup():
    print("First")
    yield
    print("helloooooo")

@pytest.fixture()
def dataload():
    print("user profile")
    return ["Emil","mariya","ns"]