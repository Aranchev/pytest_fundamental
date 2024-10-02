import pytest
from src._03_list.lab import _02_cours

def test_first_input():
    assert _02_cours.first_input(2, '1', '2') == ['1', '2'] 

