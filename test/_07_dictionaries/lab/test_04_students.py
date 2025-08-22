from src._07_dictionaries.lab import _04_students

import pytest

@pytest.mark.parametrize(
    'course, dic, expected',
    [
        (
            'fundamentals',
            {
                'Peter': {123: 'programming basics'},
                'John': {5622: 'fundamentals'},
                'Maya': {89: 'fundamentals'},
                'Lilly': {633: 'fundamentals'}
            },
            'John - 5622\nMaya - 89\nLilly - 633\n'
        )
    ]
)

def test_cor_course(course, dic, expected):
    a = _04_students.cor_course(course, dic)
    assert a == expected
