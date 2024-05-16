import pytest
@pytest.mark.usefixtures("setup")
class Test:
 def test_fixturedemo1(self):
    print("hi111")

 def test_fixturedemo2(self):
    print("hi2222")

 def test_fixturedemo3(self):
    print("hi3333")

 def test_fixturedemo4(self):
    print("hi4444")