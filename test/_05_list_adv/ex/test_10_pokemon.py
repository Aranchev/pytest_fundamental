
import pytest

from src._05_list_adv.ex import _10_pokemon

def test_increase_decrease():
    a, b = _10_pokemon.increase_decrease([5, 10, 6, 3, 5], 2)
    c, d = _10_pokemon.increase_decrease([11, 4, 9, 11], 4)
    e, f = _10_pokemon.increase_decrease([22, 15, 20, 22], 1)
    g, h = _10_pokemon.increase_decrease([7, 5, 7], 1)
    i, j = _10_pokemon.increase_decrease([2, 2], 3)
    k, l = _10_pokemon.increase_decrease([4, 4], 0)
    m, n = _10_pokemon.increase_decrease([8], 0)

    o, p = _10_pokemon.increase_decrease([4, 5, 3], 1)
    q, r = _10_pokemon.increase_decrease([9, 8], 1)
    s, t = _10_pokemon.increase_decrease([1], 0)


    assert a, b == ([11, 4, 9, 11], 6)
    assert c, d == ([22, 15, 20, 22], 11)
    assert e, f == ([7, 5, 7], 15)
    assert g, h == ([2, 2], 5)
    assert i, j == ([4, 4], 2)
    assert k, l == ([8], 4)
    assert m == []
    assert n == 8

    assert o, p == ([9, 8], 5)
    assert q, r == ([1], 8)
    assert s == []
    assert t == 1
    





