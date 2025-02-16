import pytest
from src.string_utils import replace_spaces_with_underscores

def test_replace_spaces_with_underscores_basic():
    assert replace_spaces_with_underscores("hello world") == "hello_world"

def test_replace_spaces_with_underscores_multiple_spaces():
    assert replace_spaces_with_underscores("hello  world  test") == "hello__world__test"

def test_replace_spaces_with_underscores_leading_trailing_spaces():
    assert replace_spaces_with_underscores(" hello world ") == "_hello_world_"

def test_replace_spaces_with_underscores_empty_string():
    assert replace_spaces_with_underscores("") == ""

def test_replace_spaces_with_underscores_no_spaces():
    assert replace_spaces_with_underscores("helloworld") == "helloworld"

def test_replace_spaces_with_underscores_invalid_input():
    with pytest.raises(TypeError):
        replace_spaces_with_underscores(123)
    with pytest.raises(TypeError):
        replace_spaces_with_underscores(None)