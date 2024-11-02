import pytest

from src._05_list_adv.lab import _01_no_vol

@pytest.mark.parametrize("b, exp",
     [("Python", ("Pythn")),
     ("ILovePython", ("LvPythn"))
])
def test_da(b, exp):
    a = _01_no_vol.da(b)
    assert a == exp 
