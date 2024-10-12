import pytest
from src._03_list.mex import _04_jos

def test_lst():
    a = _04_jos.lst("1 2 3 4 5 6 7")
    b = _04_jos.lst("10 5 65 104 1 0 2")
    assert a == [1, 2, 3, 4, 5, 6, 7]
    assert b == [10, 5, 65, 104, 1, 0, 2]

def test_spin():
    a = _04_jos.spin([10, 5, 65, 104, 1, 0, 2], 8)
    b = _04_jos.spin([1, 2, 3, 4, 5, 6, 7], 3)
    assert a == '[10,65,0,1,5,2,104]'

#    
# [2, 10, 5, 65, 104, 1, 0]
# [2, 5, 65, 104, 1, 0] 8 - 6 + 1 --> [0, 2, 5, 65, 104, 1, 0] 
