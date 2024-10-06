import pytest
from src._03_list.mex import _04_jos

def test_lst():
    a = _04_jos.lst("1 2 3 4 5 6 7", 3)
    assert a == ['1', '2', '3', '4', '5', '6', '7']

def test_rot():
    a = _04_jos.rot(['1', '2', '3', '4', '5', '6', '7'], 3)
    assert a == [3]


