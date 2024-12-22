import pytest

from src._05_list_adv.mex import _02_take_skip_rope 

def test_numbers_letters():
    a, b = _02_take_skip_rope.numbers_letters(['s', 'k', 'i', 'p', 'T', 'e', 's', 't', '_', 'S', 't', 'r', 'i', 'n', 'g', '0', '4', '4', '1', '6', '0']) 
    assert a == ['0', '4', '4', '1', '6', '0'] 
    assert b == ['s', 'k', 'i', 'p', 'T', 'e', 's', 't', '_', 'S', 't', 'r', 'i', 'n', 'g']

def test_take_skip_numbers():
    b, a = _02_take_skip_rope.take_skip_numbers(['0', '4', '4', '1', '6', '0'])
    assert b == [4, 1, 0] 
    assert a == [0, 4, 6]
    
def test_finite():
    a = _02_take_skip_rope.finite(['s', 'k', 'i', 'p', 'T', 'e', 's', 't', '_', 'S', 't', 'r', 'i', 'n', 'g'], [0, 4, 6], [4, 1, 0])
    assert a == ['T', 'e', 's', 't', 'S', 't', 'r', 'i', 'n', 'g']

 


