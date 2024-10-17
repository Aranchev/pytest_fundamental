import pytest

from src._04_functions.ex import _03_char_in_range

def test_da():
    a = _03_char_in_range.da('a', 'd')
    b = _03_char_in_range.da('#', ':')
    assert a == 'b c ' 
    assert b == "$ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 " 
