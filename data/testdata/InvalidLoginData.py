import pytest


@pytest.fixture(scope="class", params=[("u1","p1"), ("u2","p2") ])

def invalidLoginData(request):
    return request.param