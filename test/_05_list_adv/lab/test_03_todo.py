import pytest

from src._05_list_adv.lab import _03_todo

def test_split_str():
    a = _03_todo.split_str(['2-Walk the dog', '1-Drink coffee', '6-Dinner', '5-Work'])
    assert a == ['2 Walk the dog', '1 Drink coffee', '6 Dinner', '5 Work']

def test_order():
    a = _03_todo.order(['2 Walk the dog', '1 Drink coffee', '6 Dinner', '5 Work'])
    assert a == ['1 Drink coffee', '5 Work', '6 Dinner']
    
