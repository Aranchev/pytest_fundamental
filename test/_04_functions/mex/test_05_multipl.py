import pytest

from src._04_functions.mex import _05_multipl 

@pytest.mark.parametrize("a, b, c, expected", [
    (1, 2, 3, ("positive")),
    (-1, 2, 3, ("negative")),
    (-1, -2, 3, ("positive")),
    (-1, -2, -3, ("negative")),
    (0, -2, -3, ("zero"))
])
def test_number(a, b, c, expected):
    a = _05_multipl.number(a, b, c)
    assert a == expected 
