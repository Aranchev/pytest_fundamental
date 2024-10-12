import pytest
from src._03_list.mex import _05_tic

def test_a():
    a, b, c = _05_tic.da("0 0 0", "0 0 0", "0 0 0")
    assert a == [0, 0, 0]
    assert b == [0, 0, 0]
    assert c == [0, 0, 0]

def test_player_1():
    a = _05_tic.player_1("1 0 0", "1 0 0", "1 0 0")
    a1 = _05_tic.player_1("0 1 0", "0 1 0", "0 1 0")
    a2 = _05_tic.player_1("0 0 1", "0 0 1", "0 0 1")
    a3 = _05_tic.player_1("1 1 1", "0 0 0", "0 0 0")
    a4 = _05_tic.player_1("0 0 0", "1 1 1", "0 0 0")
    a5 = _05_tic.player_1("0 0 0", "0 0 0", "1 1 1")
    a6 = _05_tic.player_1("1 0 0", "0 1 0", "0 0 1")
    a7 = _05_tic.player_1("0 0 1", "0 1 0", "1 0 0")
    assert a == 1
    assert a1 == 1
    assert a2 == 1
    assert a3 == 1
    assert a4 == 1
    assert a5 == 1
    assert a6 == 1
    assert a7 == 1
