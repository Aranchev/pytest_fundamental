import pytest

from src._04_functions.ex import _06_sort

def test_sort():
    a = _06_sort.sort('6 2 4')
    assert a == [2, 4, 6]




