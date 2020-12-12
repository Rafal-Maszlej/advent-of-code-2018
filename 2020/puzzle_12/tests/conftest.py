import pytest


@pytest.fixture
def data():
    return """F10
N3
F7
R90
F11""".split("\n")
