import pytest

from src._05_list_adv.lab import _04_palin

def test_da():
    a = _04_palin.da('wow father mom wow shirt stats') 
    assert a == ['wow', 'father', 'mom', 'wow', 'shirt', 'stats']

def test_pa():
    a = _04_palin.find_pa(['wow', 'father', 'mom', 'wow', 'shirt', 'stats'])
    assert a == ['wow', 'mom', 'wow', 'stats']

def test_occ():
    a = _04_palin.find_occ(['wow', 'mom', 'wow', 'stats'], 'wow')
    assert a == 2


