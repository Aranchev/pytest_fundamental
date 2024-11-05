import pytest

from src._05_list_adv.lab import _05_sort_names

def test_sp_l():
    a = _05_sort_names.sp_l('Ali, Marry, Kim, Teddy, Monika, John')
    assert a == ["Monika", "Marry", "Teddy", "John", "Ali", "Kim"]


