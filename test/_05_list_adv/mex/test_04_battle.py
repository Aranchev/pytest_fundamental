import pytest

from src._05_list_adv.mex import _04_battle

def test_attacks():
    a = _04_battle.attacks('0-0 1-0 2-1 2-1 2-1 1-1 2-1')
    assert a == [[0, 0], [1, 0], [2, 1], [2, 1], [2, 1], [1, 1], [2, 1]]

def test_eliminate_zeros():
    a = _04_battle.eliminate_zeros([[1, 0, 0, 1], [2, 0, 0, 0], [0, 3, 0, 1]])
    assert a == [[1, 'x', 'x', 1], [2, 'x', 'x', 'x'], ['x', 3, 'x', 1]]

def test_ship_wreck():
    a = _04_battle.ship_wreck([[1, 'x', 'x', 1], [2, 'x', 'x', 'x'], ['x', 3, 'x', 1]], [[0, 0], [1, 0], [2, 1], [2, 1], [2, 1], [1, 1], [2, 1]])
    b = _04_battle.ship_wreck([[1, 'x', 5, 'x', 1], [6, 3, 9, 'x', 'x'], [7, 9, 4, 3, 2], [1, 'x', 'x', 4, 9], [5, 6, 'x', 3, 5]], [[0, 1], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [3, 0]])
    assert a == 2
    assert b == 2
