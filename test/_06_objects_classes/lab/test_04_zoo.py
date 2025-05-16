import pytest

from src._06_objects_classes.lab._04_zoo import Zoo

def test_add_animals():
   zoo = Zoo("Test Zoo") 
   zoo.add_animals('mammal', 'lion')
   zoo.add_animals('fish', 'salmon')
   assert 'lion' in zoo.mammals
   assert 'salmon' in zoo.fishes

