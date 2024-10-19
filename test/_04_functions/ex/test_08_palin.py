import pytest

from src._04_functions.ex import _08_palin

def test_isol():
    a = _08_palin.isol('123, 323, 421, 121')
    assert a == ['123', '323', '421', '121']

def test_vrut():
    a = _08_palin.vrut(['123', '323', '421', '121'])    
    assert a == [False, True, False, True] 

