import pytest
from src._03_list.mex import _03_car_race

def test_sequence():
    a = _03_car_race.sequence("29 13 9 0 13 0 21 0 14 82 12")
    assert a == ['29', '13', '9', '0', '13', '0', '21', '0', '14', '82', '12']
    assert len(a) == 11
  
def test_racer1():
    a = _03_car_race.racer1(['29', '13', '9', '0', '13', '0', '21', '0', '14', '82', '12'], 5)
    b = _03_car_race.racer1(['123', '20', '4', '0', '13', '0', '0', '5', '5', '14', '0'], 5)
    assert a == [29, 13, 9, 0, 13]
    assert b == [123, 20, 4, 0, 13] 

def test_racer2():
    a = _03_car_race.racer2(['29', '13', '9', '0', '13', '0', '21', '0', '14', '82', '12'], 5)
    b = _03_car_race.racer2(['123', '20', '4', '0', '13', '0', '0', '5', '5', '14', '0'], 5)
    assert a == [12, 82, 14, 0, 21]
    assert b == [0, 14, 5, 5, 0]

def test_racer_time():
    a = _03_car_race.racer_time([29, 13, 9, 0, 13])
    b = _03_car_race.racer_time([12, 82, 14, 0, 21])
    assert round(a, 1) == 53.8
    assert round(b, 1) == 107.4

