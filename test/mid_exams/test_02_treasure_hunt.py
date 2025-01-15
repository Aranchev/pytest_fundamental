import pytest

from src.mid_exams import _02_treasure_hunt

def test_loot():
    a = _02_treasure_hunt.loot(['Gold', 'Silver', 'Bronze', 'Medallion', 'Cup'], ['Loot', 'Wood', 'Gold', 'Coins'])
    b = _02_treasure_hunt.loot(['Coins', 'Wood', 'Gold', 'Silver', 'Bronze', 'Medallion', 'Cup'], ['Loot', 'Silver', 'Pistol'])

    assert a == ['Coins', 'Wood', 'Gold', 'Silver', 'Bronze', 'Medallion', 'Cup']
    assert b == ['Pistol', 'Coins', 'Wood', 'Gold', 'Silver', 'Bronze', 'Medallion', 'Cup']

def test_drop():
    a = _02_treasure_hunt.drop(['Pistol', 'Coins', 'Wood', 'Gold', 'Silver', 'Bronze', 'Medallion', 'Cup'], ['Drop', '3'])

    b = _02_treasure_hunt.drop(['1', '2', '3'], ['Drop', '3'])

    assert a == ['Pistol', 'Coins', 'Wood', 'Silver', 'Bronze', 'Medallion', 'Cup', 'Gold']

    assert b == ['1', '2', '3'] 

def test_steal():
    a, b = _02_treasure_hunt.steal(['Pistol', 'Coins', 'Wood', 'Silver', 'Bronze', 'Medallion', 'Cup', 'Gold'], ['Steal', '3'])
    c, d = _02_treasure_hunt.steal(['Pistol', 'Coins', 'Wood', 'Silver', 'Bronze', 'Medallion', 'Cup', 'Gold'], ['Steal', '9'])

    assert a == ['Pistol', 'Coins', 'Wood', 'Silver', 'Bronze']
    assert b == ['Medallion', 'Cup', 'Gold']
    assert d == ['Pistol', 'Coins', 'Wood', 'Silver', 'Bronze', 'Medallion', 'Cup', 'Gold']

 


