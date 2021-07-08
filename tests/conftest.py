import pytest

from calculator.calculator import Calculator


@pytest.fixture(scope="class")
def calculator(request):
    request.cls.calculator = Calculator()
