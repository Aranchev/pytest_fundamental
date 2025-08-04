import pytest

from src._05_list_adv.ex import _09_anon_threat

def test_merge():
    a = _09_anon_threat.merge(['abc', 'def', 'ghi'], 0, 1)
    b = _09_anon_threat.merge(['abc', 'def', 'ghi'], 0, 999)
    c = _09_anon_threat.merge(['123', '456', '789'], 1, 2)
    d = _09_anon_threat.merge(['123', '456', '789'], -3, -1)
    assert a == ['abcdef', 'ghi']
    assert b == ['abcdefghi']
    assert c == ['123', '456789']
    assert d == ['123', '456', '789']

def test_divide():
    a = _09_anon_threat.divide(['abcdefgh', 'gh'], 0, 4)
    b = _09_anon_threat.divide(['abcdef', 'ghi', 'jkl'], 0, 3)
    c = _09_anon_threat.divide(['ad', 'abcdef'], 1, 3)
    
    d = _09_anon_threat.divide(['abcd', 'efgh', 'ijkl'], 0, 3)
    e = _09_anon_threat.divide(['abcdef', 'gh'], 0, 4)
    f = _09_anon_threat.divide(['ab', 'cdefg'], 1, 2)

    assert a == ['ab', 'cd', 'ef', 'gh', 'gh']
    assert b == ['ab', 'cd', 'ef', 'ghi', 'jkl']
    assert c == ['ad', 'ab', 'cd', 'ef']
    assert d == ['a', 'b', 'cd', 'efgh', 'ijkl']
    assert e == ['a', 'b', 'c', 'def', 'gh']
    assert f == ['ab', 'cd', 'efg']




