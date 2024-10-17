import pytest

from src._04_functions.lab import _04_rep_str

def test_da():
    a = _04_rep_str.da('da', 2)
    assert a == 'dada'

