import pytest

from src._04_functions.ex import _da_

def test_da():
    a = _da_.da()
    assert a == 'da'
