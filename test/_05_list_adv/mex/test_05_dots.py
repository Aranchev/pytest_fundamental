import pytest

from src._05_list_adv.mex import _05_dots

'''
1. localization of the initial point 
'''

def test_localize_dot():
    a = _05_dots.localize_dot([
['.', '.', '-', '-', '-', '-'], 
['.', '-', '-', '-', '-', '-'], 
['-', '-', '-', '-', '-', '-'], 
['-', '-', '-', '-', '-', '-'] 
])
    assert a == [0, 0]

    b = _05_dots.localize_dot([
['-', '-', '-', '-', '-', '-'], 
['-', '-', '-', '-', '-', '-'], 
['-', '-', '-', '-', '-', '-'], 
['-', '-', '-', '-', '-', '-'] 
])
    assert b == None 

'''
2. availability of the initial point's sides  
'''

def test_check_sides():
    a, b = _05_dots.check_sides([
['.', '.', '-', '-', '-', '-'], 
['.', '-', '-', '.', '-', '-'], 
['-', '-', '-', '-', '-', '-'], 
['-', '-', '-', '-', '-', '-']
],
[0, 0])
    
    assert a == [1, 3]
    assert b == [
['x', '.', '-', '-', '-', '-'], 
['.', '-', '-', '.', '-', '-'], 
['-', '-', '-', '-', '-', '-'], 
['-', '-', '-', '-', '-', '-']
]

'''
3. Deriving the parameters of the initial point's available sides 
'''

def test_cont():
    a = _05_dots.cont([0, 0], [1, 3])

    assert a == [[1, 0], [0, 1]]

'''
4. Check the sides of given points.
'''

def test_check_sides_two():
    a, b = _05_dots.check_sides_two([
['x', '.', '-', '-', '-', '-'], 
['.', '-', '-', '-', '-', '-'], 
['-', '-', '-', '-', '-', '-'], 
['-', '-', '-', '-', '-', '-']
],
[[1, 0], [0, 1]])

    assert a == [[], []]
    assert b == [
['x', 'x', '-', '-', '-', '-'], 
['x', '-', '-', '-', '-', '-'], 
['-', '-', '-', '-', '-', '-'], 
['-', '-', '-', '-', '-', '-']
]

    c, d = _05_dots.check_sides_two([
['x', '.', '.', '-', '-', '-'], 
['.', '.', '-', '.', '-', '-'], 
['.', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-']
],
[[1, 0], [0, 1]])

    assert c == [[1, 3], [1, 3]]
    assert d == [
['x', 'x', '.', '-', '-', '-'], 
['x', '.', '-', '.', '-', '-'], 
['.', '-', '-', '-', '-', '-'], 
['-', '-', '-', '-', '-', '-']
]

def test_zipidi():
    a, b = _05_dots.zipidi([[1, 0], [0, 1]], [[1, 3], [1, 3]], [
['x', 'x', '.', '-', '-', '-'], 
['x', '.', '-', '.', '-', '-'], 
['.', '-', '-', '-', '-', '-'], 
['-', '-', '-', '-', '-', '-']
])
    assert a == [[2, 0], [1, 1], [0, 2]]
    assert b ==[ 
['x', 'x', 'x', '-', '-', '-'], 
['x', 'x', '-', '.', '-', '-'], 
['x', '-', '-', '-', '-', '-'], 
['-', '-', '-', '-', '-', '-']
]

