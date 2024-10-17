import pytest

from src._04_functions.ex import _01_small_of_three

def test_da():
    a = _01_small_of_three.da(1, 2, 3)
    assert a == 1

