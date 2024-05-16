import pytest

from pytestdemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataload")
class TestDemo(BaseClass):
    def test_profile(self,dataload):
        log = self.getLogger()
        log.info(dataload)
        #print(dataload)
        print(dataload[0])
        print(dataload[1])
