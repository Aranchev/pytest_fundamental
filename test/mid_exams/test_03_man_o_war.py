import pytest

from src.mid_exams import _03_man_o_war

def test_fire():
    a = _03_man_o_war.fire([13], ['Fire', '1', '1'])
    b = _03_man_o_war.fire([13, 11], ['Fire', '1', '10'])
    c = _03_man_o_war.fire([12, 22, 33, 44, 55, 32, 18], ['Fire', '2', '11'])

    assert a == [13]
    assert b == [13, 1]
    assert c == [12, 22, 22, 44, 55, 32, 18]

def test_defend():
    a = _03_man_o_war.defend([12, 13, 11, 20, 66], ['Defend', '0', '3', '5'])
    b = _03_man_o_war.defend([12, 13, 11, 20, 66], ['Defend', '0', '5', '5'])
    assert a == [7, 8, 6, 15, 66]
    assert b == [12, 13, 11, 20, 66]

def test_repair():
    a = _03_man_o_war.repair([7, 8, 6, 15, 66], ['Repair', '1', '33'], 70)
    b = _03_man_o_war.repair([7, 8, 6, 15, 66], ['Repair', '1', '100'], 70)
    c = _03_man_o_war.repair([7, 8, 6, 15, 66], ['Repair', '1', '61'], 70)


    assert a == [7, 41, 6, 15, 66]
    assert b == [7, 70, 6, 15, 66]
    assert c == [7, 69, 6, 15, 66]

def test_status():
    a = _03_man_o_war.status([7, 41, 6, 15, 66], 70)
    assert a == 2






