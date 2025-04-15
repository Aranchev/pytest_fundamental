import pytest

from src._06_objects_classes.lab import _01_comment

@pytest.mark.parametrize(
    "username, content, likes",
    [
        ('user1', 'This is comment', 0)
    ]
)

def test_comment(username, content, likes):
    a = _01_comment.Comment(username, content, likes)
    assert a.username == 'user1' 
 
