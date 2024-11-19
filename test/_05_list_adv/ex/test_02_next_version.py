import pytest

from src._05_list_adv.ex import _02_next_version

def test_da():
    a = _02_next_version.da('1.2.3')
    assert a == [1, 2, 3]



