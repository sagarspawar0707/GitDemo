import pytest

from pytestDemo.BaseClass import *


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_edit_profile(self,dataLoad):
        #dataLoad = pytest.helpers.dataLoad
        log=self.getlogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])
        print(dataLoad)
        print(dataLoad[0])
        print(dataLoad[1])
        print(dataLoad[2])