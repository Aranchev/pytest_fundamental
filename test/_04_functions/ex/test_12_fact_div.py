import pytest

from src._04_functions.ex import _12_fact_div

def test_first_fact():
    a = _12_fact_div.first_fact(5)
    assert a == 120
