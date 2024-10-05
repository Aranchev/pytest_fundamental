import pytest
from src._03_list.mex import _02_mess

def test_char_string():
    a = _02_mess.char_string("This is some message for you")
    b = _02_mess.char_string("87j973u59dg37e725!")
    assert len(a) == 28 
    assert len(b) == 18 
    
def test_num_sum():
    a = _02_mess.num_sum("9992 562 8933")
    b = _02_mess.num_sum("2 122 1123 1321 9 17211")
    assert a == [29, 13, 23]
    assert b == [2, 5, 7, 7, 9, 12]
    assert a[0] == 29

def test_vurtalejka():
    a = _02_mess.vurtalejka("9992 562 8933", "This is some message for you")
    b = _02_mess.vurtalejka("2 122 1123 1321 9 17211", "87j973u59dg37e725!")
    assert a == 'hey'
    assert b == 'judge!'

