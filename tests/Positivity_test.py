import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly_devision(self):
        assert self.calc.division(self, 2, 2) == 1

    def test_multiply_calculate_correctly_subtraction(self):
        assert self.calc.subtraction(self, 5, 2) == 3

    def test_multiply_calculate_correctly_adding(self):
        assert self.calc.adding(self, 2, 2) == 4

    def test_multiply_calculate_correctly_multiply(self):
        assert self.calc.multiply(self, 4, 2) == 8