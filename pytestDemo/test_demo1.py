#Any pytest file should start with test_ or _test
#pytest method names should start with test
#any code should be wrapped in method only
import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")

@pytest.mark.xfail
def test_SecondProgramCreditcard():
    print("Good Morning")