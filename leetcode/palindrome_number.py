"""
LeetCode Problem #9: Palindrome Number

Problem Description:
Given an integer x, return true if x is a palindrome, and false otherwise.
A palindrome number reads the same forward and backward.

Example:
Input: x = 121
Output: True
Explanation: 121 reads as 121 from left to right and from right to left.

Example:
Input: x = -121
Output: False
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.

Time Complexity: O(log n) where n is the value of x
Space Complexity: O(1)
"""


def is_palindrome(x):
    """
    Check if a number is a palindrome.
    
    Args:
        x: Integer to check
        
    Returns:
        Boolean indicating if x is a palindrome
    """
    # Negative numbers are not palindromes
    # Numbers ending in 0 are not palindromes (except 0 itself)
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    # Reverse half of the number
    reversed_half = 0
    while x > reversed_half:
        # Extract the last digit and add it to reversed_half
        reversed_half = reversed_half * 10 + x % 10
        # Remove the last digit from x
        x //= 10
    
    # Check if the number is a palindrome
    # For even length numbers: x == reversed_half
    # For odd length numbers: x == reversed_half // 10 (ignore middle digit)
    return x == reversed_half or x == reversed_half // 10


# Test cases
if __name__ == "__main__":
    # Test case 1: Positive palindrome
    x1 = 121
    print(f"Input: x = {x1}")
    print(f"Output: {is_palindrome(x1)}")
    print()
    
    # Test case 2: Negative number
    x2 = -121
    print(f"Input: x = {x2}")
    print(f"Output: {is_palindrome(x2)}")
    print()
    
    # Test case 3: Not a palindrome
    x3 = 10
    print(f"Input: x = {x3}")
    print(f"Output: {is_palindrome(x3)}")
    print()
    
    # Test case 4: Single digit
    x4 = 7
    print(f"Input: x = {x4}")
    print(f"Output: {is_palindrome(x4)}")
