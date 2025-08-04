import pytest
from src._03_list.mex import _06_list_mani

def test_list_transformation():
    a = _06_list_mani.list_transformation('1 3 5 7 9')
    assert a == [1, 3, 5, 7, 9]

def test_format_txt():
    b = _06_list_mani.format_txt("exchange 2")
    c = _06_list_mani.format_txt("exchange 10")
    assert b == ['exchange', '2']
    assert c == ['exchange', '10']

def test_exchange():
    a = _06_list_mani.exchange([1, 3, 5, 7, 9], ["exchange", "1"])
    b = _06_list_mani.exchange([1, 10, 100, 100], ['exchange', '10'])
    assert a == [5, 7, 9, 1, 3] 
    assert b == 'Invalid index'    

def test_max_odd():
    a = _06_list_mani.max_odd([5, 7, 9, 1, 3])
    b = _06_list_mani.max_odd([2, 4, 6])
    c = _06_list_mani.max_odd([2, 2, 1, 1])
    assert a == 2
    assert b == 'No matches' 
    assert c == 3

def test_max_even():
    a = _06_list_mani.max_even([1, 2, 3, 4, 5])
    b = _06_list_mani.max_even([1, 10, 100, 1000])
    c = _06_list_mani.max_even([1, 3, 5, 7, 9])
    d = _06_list_mani.max_even([1, 2, 2, 1])
    e = _06_list_mani.max_even([10, 100, 1000, 1])

    assert a == 3
    assert b == 3
    assert c == 'No matches'
    assert d == 2
    assert e == 2

def test_min_odd():
    a = _06_list_mani.min_odd([4, 3, 1, 1])
    b = _06_list_mani.min_odd([1, 10, 100, 1000])
    c = _06_list_mani.min_odd([2, 4, 6, 8])
    assert a == 3 
    assert b == 0
    assert c == 'No matches'

def test_min_even():
    a = _06_list_mani.min_even([5, 7, 9, 1, 3])
    b = _06_list_mani.min_even([1, 1, 0, 0, 1])
    assert a == "No matches" 
    assert b == 3

def test_first_odd():
    a = _06_list_mani.first_odd([5, 7, 9, 1, 3], 2)
    b = _06_list_mani.first_odd([2, 2, 2, 2, 2], 2)
    c = _06_list_mani.first_odd([1, 2, 3], 4)
    assert a == [5, 7]
    assert b == []
    assert c == 'Invalid count'


def test_first_even():
    a = _06_list_mani.first_even([1, 8, 2, 3], 2)
    b = _06_list_mani.first_even([1, 10, 100, 1000], 5)
    c = _06_list_mani.first_even([1, 1, 1, 1], 2)
    d = _06_list_mani.first_even([1, 8, 2, 3, 4, 6, 4], 2)
    assert a == [8, 2]
    assert b == 'Invalid count'

def test_last_odd():
    a = _06_list_mani.last_odd([1, 8, 2, 3], 2)
    b = _06_list_mani.last_odd([2, 2, 2, 2], 2) 
    c = _06_list_mani.last_odd([1, 2, 3, 4, 5, 6], 2)
    d = _06_list_mani.last_odd([1, 2, 3], 4)

    assert a == [1, 3]
    assert b == []
    assert c == [3, 5]
    assert d == 'Invalid count'


