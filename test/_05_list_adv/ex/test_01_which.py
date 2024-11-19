import pytest

from src._05_list_adv.ex import _01_which

@pytest.mark.parametrize("a, b", [
('arp, live, strong', ['arp', 'live', 'strong']),
('lively, alive, harp, sharp, armstrong', ['lively', 'alive', 'harp', 'sharp', 'armstrong'])
])
def test_lit(a, b):
    c = _01_which.lit(a)
    assert c == b
    


