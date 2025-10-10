import pytest

from src._07_dictionaries.ex._11_force_book import existance_checker, ver 

def test_existance_checker():

    a = existance_checker('Light', 'Kim', {})
    assert a == (False, False)

    a1 = existance_checker('Light', 'Kim', {'Dark': 'Peter'})
    assert a1 == (False, False)


    b = existance_checker('Dark', 'Kim', {'Light': 'Kim'})
    assert b == (False, True)


    c = existance_checker('Light', 'Kim', {'Light': ['Peter']})
    assert c == (True, False)

def test_ver():
    
    # False - False
    a = ver('Light', 'Kim', existance_checker('Light', 'Kim', {}), {})
    assert a == {'Light': ['Kim']}

    # False - False
    a1 = ver('Light', 'Kim', existance_checker('Light', 'Kim', {'Dark': ['Peter']}), {'Dark': ['Peter']})
    assert a1 == {'Dark': ['Peter'], 'Light': ['Kim']}

    # False - True
    b = ver('Light', 'Kim', existance_checker('Dark', 'Kim', {'Light': ['Kim']}), {'Light': ['Kim']})
    assert b == {'Light': ['Kim']}

    c = ver('Light', 'Kim', existance_checker('Light', 'Kim', {'Light': ['Peter']}), {'Light': ['Peter']})
    assert c == {'Light': ['Peter', 'Kim']}



