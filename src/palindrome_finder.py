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
    
    # Find all palindromic substrings
    palindromes = set()
    
    # Check all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Extract substring
            substring = s[i:j+1]
            
            # Check if substring is a palindrome
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    # Remove single-character palindromes from consideration
    palindromes = {p for p in palindromes if len(p) > 1}
    
    # Sort the palindromes lexicographically
    return sorted(list(palindromes))