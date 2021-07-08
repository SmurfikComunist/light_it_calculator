""" Calculator module test cases """

import pytest

from calculator.calculator import Calculator


@pytest.mark.usefixtures("calculator")
class TestCalculator:
    calculator: Calculator

    @pytest.mark.parametrize(
        'x, y, result',
        [
            (7, 2, 9),
            (-4, -5, -9),
            (-4, 7, 3),
            (6, -8, -2),
            (0, 0, 0),
            (20, 33, 53)
        ]
    )
    def test_add(self, x: int, y: int, result: int):
        assert result == self.calculator.add(x=x, y=y)

    @pytest.mark.parametrize(
        'x, y, result',
        [
            (7, 2, 5),
            (-4, -5, 1),
            (-4, 7, -11),
            (6, -8, 14),
            (0, 0, 0),
            (20, 33, -13)
        ]
    )
    def test_subtract(self, x: int, y: int, result: int):
        assert result == self.calculator.subtract(x=x, y=y)

    @pytest.mark.parametrize(
        'x, y, result',
        [
            (7, 2, 3.5),
            (-4, -5, 0.8),
            (-21, 7, -3),
            (6, -8, -0.75),
            (10, 5, 2),
            (0, 3, 0)
        ]
    )
    def test_divide_valid(self, x: int, y: int, result: int):
        assert result == self.calculator.divide(x=x, y=y)

    @pytest.mark.parametrize(
        'x, y, result',
        [
            (7, 0, ZeroDivisionError),
            (0, 0, ZeroDivisionError),
            (5, 0, ZeroDivisionError)
        ]
    )
    def test_divide_invalid(self, x: int, y: int, result: Exception):
        with pytest.raises(result):
            self.calculator.divide(x=x, y=y)

    @pytest.mark.parametrize(
        'x, y, result',
        [
            (7, 2, 14),
            (-4, -5, 20),
            (-21, 7, -147),
            (6, -8, -48),
            (10, 5, 50),
            (0, 3, 0)
        ]
    )
    def test_multiply(self, x: int, y: int, result: int):
        assert result == self.calculator.multiply(x=x, y=y)

    @pytest.mark.parametrize(
        'x, y, result',
        [
            (7, 2, 1),
            (17, 3, 2),
            (-4, -5, -4),
            (-21, 7, 0),
            (6, -8, -2),
            (10, 5, 0),
            (0, 3, 0)
        ]
    )
    def test_mod(self, x: int, y: int, result: int):
        assert result == self.calculator.mod(x=x, y=y)

    @pytest.mark.parametrize(
        'x, y, result',
        [
            (7, 2, 49),
            (17, 3, 4913),
            (-21, 7, -1801088541),
            (10, 5, 100000),
            (0, 3, 0)
        ]
    )
    def test_power(self, x: int, y: int, result: int):
        assert result == self.calculator.power(x=x, y=y)

    @pytest.mark.parametrize(
        'x, result',
        [
            (25, 5),
            (121, 11),
            (81, 9),
            (0, 0)
        ]
    )
    def test_root_valid(self, x: int, result: int):
        assert result == self.calculator.root(x=x)

    @pytest.mark.parametrize(
        'x, result',
        [
            (-25, ValueError),
            (-121, ValueError),
            (-81, ValueError)
        ]
    )
    def test_root_invalid(self, x: int, result: Exception):
        with pytest.raises(result):
            self.calculator.root(x=x)
