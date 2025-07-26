import pytest

from src._06_objects_classes.ex._09_movie import Movie

@pytest.fixture
def inception_movie():
    return Movie('Inception', 'Christopher Nolan')

@pytest.fixture
def matrix_movie():
    return Movie('The Matrix', 'The Wachowskis')

@pytest.fixture
def predator_movie():
    return Movie('The Predator', 'Shane Black')


class TestMovie:
    def test_init(self, inception_movie, matrix_movie, predator_movie):
        assert inception_movie.name == 'Inception'
        assert inception_movie.director == 'Christopher Nolan'
        assert matrix_movie.name == 'The Matrix'
        assert matrix_movie.director == 'The Wachowskis'
        assert predator_movie.name == 'The Predator'
        assert predator_movie.director == 'Shane Black'

    def test_change_name(self, inception_movie, matrix_movie, predator_movie):
        predator_movie.change_name('My Movie')
        assert predator_movie.name == 'My Movie'

    def test_change_director(self, inception_movie, matrix_movie, predator_movie):
        inception_movie.change_director('Me')
        assert inception_movie.director == 'Me'

    def test_watch(self, inception_movie, matrix_movie, predator_movie):
        inception_movie.watch()
        matrix_movie.watch()

        assert inception_movie.watched == True
        assert inception_movie.__class__._Movie__watched_movies == 2
        assert Movie._Movie__watched_movies == 2

         








