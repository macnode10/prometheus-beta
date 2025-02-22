import pytest
from src.palindrome_finder import find_non_overlapping_palindromes

def test_find_non_overlapping_palindromes():
    # Test empty string
    assert find_non_overlapping_palindromes("") == []
    
    # Test string with no palindromes
    assert find_non_overlapping_palindromes("abc") == []
    
    # Test string with single-character palindromes
    assert find_non_overlapping_palindromes("abcba") == ["abcba"]
    
    # Test multiple palindromes
    assert find_non_overlapping_palindromes("aabaa") == ["aa", "aabaa"]
    
    # Test lexicographic sorting
    assert find_non_overlapping_palindromes("racecar") == ["aceca", "racecar"]
    
    # Test complex case with multiple palindromes
    assert find_non_overlapping_palindromes("abcddcbaxyz") == ["abcddc", "xyz"]
    
    # Test case with repeated palindromes
    assert find_non_overlapping_palindromes("aaaaa") == ["aaaa"]
    
    # Test case with mixed palindromes
    result = find_non_overlapping_palindromes("xabcbaxpqrqp")
    assert result == ["abcba", "pqrqp", "x"]