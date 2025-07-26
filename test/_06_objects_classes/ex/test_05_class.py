import pytest

from src._06_objects_classes.ex._05_class import Class

def test_add_students():
    da = Class("Da")
    da.add_student('Peter', 4.80)
    assert da.students == ['Peter']
    assert da.grades == [4.80]

def test_get_average_grade():
    da = Class("Da")
    da.add_student('Peter', 4.80)
    da.add_student('Peter', 4.70)
    # (4.8 + 4.7) / 2 = 4.75

    a = da.get_average_grade()
    assert a == 4.75
