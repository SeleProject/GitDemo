import pytest


@pytest.mark.skip
def test_firstdemo():
    msg = "Hello"
    assert msg == "hi" , "Message is not correct"

@pytest.mark.xfail
def test_secondNew(setup):
    a = 4
    b = 6
    assert a+2 == b