def switch_cases(str1, str2):
    """
    Takes two strings and returns a new string with swapped character cases.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: A new string where lowercase characters become uppercase and vice versa
    """
    # Convert str1 characters to opposite case
    str1_switched = ''.join(c.lower() if c.isupper() else c.upper() for c in str1)
    
    # Convert str2 characters to opposite case
    str2_switched = ''.join(c.lower() if c.isupper() else c.upper() for c in str2)
    
    # Handle special cases: empty strings or single strings
    if not str1 and not str2:
        return ""
    elif not str1:
        return str2_switched
    elif not str2:
        return str1_switched
    
    # If strings contain no alphabetic characters, join them without space
    if not any(c.isalpha() for c in str1 + str2):
        return str1_switched + str2_switched
    
    return str1_switched + " " + str2_switched