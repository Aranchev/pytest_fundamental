import pytest

from src._04_functions.mex import _01_data_types

def test_da(capsys):
    _01_data_types.da('int', 5)
    out, err = capsys.readouterr()
    assert out == "10\n"

    _01_data_types.da('real', 2)
    out, err = capsys.readouterr()
    assert out == "3.00\n"
    
    _01_data_types.da('string', 'hello')
    out, err = capsys.readouterr()
    assert out == "$hello$\n"
