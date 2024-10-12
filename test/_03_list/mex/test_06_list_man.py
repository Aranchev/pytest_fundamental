import pytest
from src._03_list.mex import _06_list_man

def test_list_transformation():
    a = _06_list_man.list_transformation('1 3 5 7 9')
    assert a == [1, 3, 5, 7, 9]
    
def test_format_txt():
    b = _06_list_man.format_txt("exchange 2")
    assert b == ['exchange', '2']

def test_exchange():
    a = _06_list_man.exchange([1, 3, 5, 7, 9], ["exchange", "1"])
    assert a == [5, 7, 9, 1, 3] 

def test_max():
    a = _06_list_man.max_odd([5, 7, 9, 1, 3])
    assert a == 2

def test_max_even():
    a = _06_list_man.max_even([1, 2, 3, 4, 5])
    b = _06_list_man.max_even([1, 1, 0, 1, 1])
    assert a == 3
    assert b == 2

def test_min_even():
    a = _06_list_man.min_even([5, 7, 9, 1, 3])
    b = _06_list_man.min_even([1, 1, 0, 0, 1])
    assert a == "No matches" 
    assert b == 3

def test_min_odd():
    a = _06_list_man.min_odd([4, 3, 1, 1])
    assert a == 3 
