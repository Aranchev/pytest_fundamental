import pytest

from src._05_list_adv.lab import _06_even


@pytest.mark.parametrize("a, expected", [
('3, 2, 1, 5, 8', ([1, 4])),
('2, 4, 6, 9, 10', [0, 1, 2, 4])
])
def test_da(a, expected):
    a = _06_even.da(a)
    assert a == expected 


