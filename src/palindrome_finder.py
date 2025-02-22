def find_non_overlapping_palindromes(s):
    """
    Find all non-overlapping palindromic substrings in the input string,
    sorted in lexicographic order.
    
    Args:
        s (str): Input string to find palindromic substrings
    
    Returns:
        list: Sorted list of unique non-overlapping palindromic substrings
    """
    # Edge case: empty string
    if not s:
        return []
    
    # Find non-overlapping palindromes
    palindromes = set()
    
    # Check all possible substrings
    for i in range(len(s)):
        # Check palindromes starting from this index
        for j in range(len(s), i, -1):
            substring = s[i:j]
            
            # Check if substring is a valid palindrome
            if substring == substring[::-1] and len(substring) > 1:
                # Check if this palindrome overlaps with previous ones
                if all(substring not in prev for prev in palindromes):
                    # Remove any previously added shorter palindromes that are part of this one
                    palindromes = {p for p in palindromes if p not in substring}
                    palindromes.add(substring)
    
    # Sort the palindromes lexicographically
    return sorted(palindromes)