import pytest
from src._04_functions.lab import _01_ab_val

def test_da():
    a = _01_ab_val.da('1 2.5 -3 -4.5')
    assert a == [1.0, 2.5, 3.0, 4.5]


