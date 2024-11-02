import pytest

from src._04_functions.ex import _10_perf_num

def test_number():
    a = _10_perf_num.number(6)
    b = _10_perf_num.number(28)
    c = _10_perf_num.number(1236498)
    assert a == 'We have a perfect number!'
    assert b == 'We have a perfect number!'
    assert c == "It's not so perfect."



