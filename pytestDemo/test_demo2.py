#Any pytest file should start with test_ or _test
#pytest method names should start with test
#any code should be wrapped in method only
import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi"   "Test failed because string do not match"

def test_SecondCreditCard():
    print("Creditcard")
    a = 4
    b = 6
    assert a+2 == 6,  "Addition do not match"



