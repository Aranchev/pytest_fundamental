import pytest

from src._04_functions.lab import _03_calc

def test_add():
    a = _03_calc.add(1, 2)
    assert a == 3

def test_subtract():
    a = _03_calc.subtract(3, 1)
    assert a == 2

def test_multiply():
    a = _03_calc.multiply(3, 2)
    assert a == 6



