"""
LeetCode Problem #13: Roman to Integer

Problem Description:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII,
which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.

Given a roman numeral, convert it to an integer.

Example:
Input: s = "III"
Output: 3

Example:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(1)
"""


def roman_to_int(s):
    """
    Convert a Roman numeral to an integer.
    
    Args:
        s: String representing a Roman numeral
        
    Returns:
        Integer value of the Roman numeral
    """
    # Dictionary mapping Roman symbols to their values
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    # Iterate through the string from right to left
    for char in reversed(s):
        current_value = roman_map[char]
        
        # If current value is less than previous, subtract it (e.g., IV = 5 - 1)
        # Otherwise, add it
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        
        prev_value = current_value
    
    return total


# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "III"
    print(f"Input: s = \"{s1}\"")
    print(f"Output: {roman_to_int(s1)}")
    print()
    
    # Test case 2
    s2 = "LVIII"
    print(f"Input: s = \"{s2}\"")
    print(f"Output: {roman_to_int(s2)}")
    print()
    
    # Test case 3
    s3 = "MCMXCIV"
    print(f"Input: s = \"{s3}\"")
    print(f"Output: {roman_to_int(s3)}")
    print("Explanation: M = 1000, CM = 900, XC = 90, IV = 4")
