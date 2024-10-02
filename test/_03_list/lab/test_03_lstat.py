import pytest
from src._03_list.lab import _03_lstat

def test_pos():
    assert _03_lstat.pos(10, 3, 2, -15, -4) == 3 

def test_neg():
    assert _03_lstat.neg(10, 3, 2, -15, -4) == 2

def test_count():
    assert _03_lstat.count(10, 3, 2, -15, -4) == 5

def test_sum_neg():
    assert _03_lstat.sum_neg(10, 3, 2, -15, -4) == -19

    


