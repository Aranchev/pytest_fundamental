import pytest

from src._04_functions.lab import _06_rec_area

def test_rec_area():
    a = _06_rec_area.rec_area(3, 4)
    assert a == 12

