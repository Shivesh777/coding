# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

# create an array of boolean values, where the flag at index i indicates whether character i in the alphabet is contained in the string. The second time you see this character you can immediately return false.
# We can also immediately return f a l s e if the string length exceeds the number of unique characters in the alphabet. After all, you can't form a string of 280 unique characters out of a 128-character alphabet.


def is_unique(string: str) -> bool:
    """
    Check if a string has all unique characters using an optimized approach.

    Args:
        string (str): The input string to be checked.

    Returns:
        bool: True if the string has all unique characters, False otherwise.

    Examples:
        >>> is_unique("abcdef")
        True
        >>> is_unique("aabbcc")
        False
    """
    if len(string) > 128:
        return False

    checker = 0
    for char in string:
        ascii_val = ord(char)
        if (checker & (1 << ascii_val)) > 0:
            return False
        checker |= 1 << ascii_val

    return True
