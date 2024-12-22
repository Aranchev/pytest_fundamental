import pytest

from src._05_list_adv.ex import _04_number_clasification

def test_trans():
    a = _04_number_clasification.trans('1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33')
    assert a == [1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33]

def test_positive():
    a = _04_number_clasification.positive([1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33])
    assert a == '1, 0, 5, 3, 4, 12, 19'


