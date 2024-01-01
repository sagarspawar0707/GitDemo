import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("i will be executing last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Sagar","Pawar","sagarspawar0707@gmail.com"]


@pytest.fixture(params=[("chrome","Sagar","Pawar"),("Firefox","Sagar"),("IE","ss")])
def crossBrowser(request):
    return request.param
