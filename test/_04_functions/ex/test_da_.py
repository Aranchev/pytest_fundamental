import pytest

from src._04_functions.ex import _da_

def test_rem():
    a = _da_.rem('Remove 0', 'pa|Do|ha|mm|er')
    assert a == 'Do ha mm er'
