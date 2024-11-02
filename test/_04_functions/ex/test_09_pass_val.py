import pytest

from src._04_functions.ex import _09_pass_val

def test_lenght():
    a = _09_pass_val.lenght('logIn') # len == 5
    b = _09_pass_val.lenght('logina') # len == 6
    assert a == 'Password must be between 6 and 10 characters' 
    assert b == None

def test_let_num():
    a = _09_pass_val.let_num('logIn')
    b = _09_pass_val.let_num('MyPass123')
    c = _09_pass_val.let_num('Pa$s$s')
    assert a == None 
    assert b == None 
    assert c == 'Password must consist only of letters and digits' 
    
def test_at_least():
    a = _09_pass_val.at_least('login')
    assert a == 'Password must have at least 2 digits'


    
