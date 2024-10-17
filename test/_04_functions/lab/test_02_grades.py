import pytest

from src._04_functions.lab import _02_grades

def test_da():
    a = _02_grades.da(2.99)
    b = _02_grades.da(3.99)
    c = _02_grades.da(4.99)
    d = _02_grades.da(5.99)
    assert a == 'Fail'
    assert b == 'Good'
    assert c == 'Very Good'
    assert d == 'Excellent'
    




