"""
LeetCode Problem #344: Reverse String

Problem Description:
Write a function that reverses a string. The input string is given as an array 
of characters s. You must do this by modifying the input array in-place with 
O(1) extra memory.

Example:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(1) - in-place modification
"""


def reverse_string(s):
    """
    Reverse a string in-place using two pointers.
    
    Args:
        s: List of characters (modified in-place)
        
    Returns:
        None (modifies s in-place)
    """
    # Two pointer approach
    left = 0
    right = len(s) - 1
    
    # Swap characters from both ends moving towards the center
    while left < right:
        # Swap characters
        s[left], s[right] = s[right], s[left]
        
        # Move pointers
        left += 1
        right -= 1


# Alternative Pythonic solution
def reverse_string_pythonic(s):
    """
    Reverse a string using Python's built-in reverse method.
    
    Args:
        s: List of characters (modified in-place)
        
    Returns:
        None (modifies s in-place)
    """
    s.reverse()


# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = ["h", "e", "l", "l", "o"]
    print(f"Input: s = {s1}")
    reverse_string(s1)
    print(f"Output: {s1}")
    print()
    
    # Test case 2
    s2 = ["H", "a", "n", "n", "a", "h"]
    print(f"Input: s = {s2}")
    reverse_string(s2)
    print(f"Output: {s2}")
    print()
    
    # Test case 3: Using Pythonic approach
    s3 = ["p", "y", "t", "h", "o", "n"]
    print(f"Input: s = {s3}")
    reverse_string_pythonic(s3)
    print(f"Output (using pythonic approach): {s3}")
