import os

def is_file_exists(file_path):
    """
    Check if a file exists at the given path.
    
    Args:
        file_path (str): The path to the file to check.
    
    Returns:
        bool: True if the file exists and is a file, False otherwise.
    
    Raises:
        TypeError: If the input is None
    """
    # Check for None input first
    if file_path is None:
        raise TypeError("File path cannot be None")
    
    # Check if path exists and is a file (not a directory)
    return os.path.exists(file_path) and os.path.isfile(file_path)