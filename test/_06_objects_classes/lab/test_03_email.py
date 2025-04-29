import pytest

from src._06_objects_classes.lab import _03_email

def test_class():
    a = _03_email.Email('gosho', 'pesho', "hi,pesho")
    assert a.sender == 'gosho'
    assert a.receiver == 'pesho'
    assert a.content == 'hi,pesho'
    assert a.is_sent == False

def test_send():
    a = _03_email.Email('gosho', 'pesho', 'ico')
    a.send()
    assert a.is_sent == True 

