import os
import pytest
import tempfile
from src.file_utils import is_file_exists

def test_is_file_exists_with_existing_file():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Test that the function returns True for an existing file
        assert is_file_exists(temp_path) == True
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)

def test_is_file_exists_with_non_existing_file():
    # Use a path that is extremely unlikely to exist
    non_existent_path = "/tmp/very_unlikely_file_that_does_not_exist_12345.txt"
    assert is_file_exists(non_existent_path) == False

def test_is_file_exists_with_directory():
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Directories should return False
        assert is_file_exists(temp_dir) == False
    finally:
        # Clean up the temporary directory
        os.rmdir(temp_dir)

def test_is_file_exists_with_empty_path():
    # Test with an empty path
    assert is_file_exists("") == False

def test_is_file_exists_with_none():
    # Test with None input
    with pytest.raises(TypeError):
        is_file_exists(None)