import pytest
from src._04_functions.mex import _03_longer_line

@pytest.mark.parametrize(
"x1, y1, x2, y2, x3, y3, x4, y4, expected",
[
(1, 2, 3, 4, 9, 7, 5, 6, (2.83, 4.12)),
(0, 0, 3, 4, 1, 1, 4, 5, (5.0, 5.0))
]
)
def test_lenght(x1, y1, x2, y2, x3, y3, x4, y4, expected):
    result = _03_longer_line.lenght(x1, y1, x2, y2, x3, y3, x4, y4)
    assert result == expected

def test_distance():
    a, b, c, d = _03_longer_line.distance(1, 2, 3, 4, 9, 7, 5, 6)
    assert round(a, 2) == 2.24
    assert round(b, 2) == 5.0
    assert round(c, 2) == 11.4 
    assert round(d, 2) == 7.81 

