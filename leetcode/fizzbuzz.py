"""
LeetCode Problem #412: FizzBuzz

Problem Description:
Given an integer n, return a string array answer (1-indexed) where:
- answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
- answer[i] == "Fizz" if i is divisible by 3.
- answer[i] == "Buzz" if i is divisible by 5.
- answer[i] == i (as a string) if none of the above conditions are true.

Example:
Input: n = 3
Output: ["1","2","Fizz"]

Example:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Example:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

Time Complexity: O(n)
Space Complexity: O(n) for the output array
"""


def fizzbuzz(n):
    """
    Generate FizzBuzz sequence for numbers from 1 to n.
    
    Args:
        n: Integer representing the upper limit
        
    Returns:
        List of strings following FizzBuzz rules
    """
    result = []
    
    for i in range(1, n + 1):
        # Check divisibility by both 3 and 5 first
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        # Check divisibility by 3
        elif i % 3 == 0:
            result.append("Fizz")
        # Check divisibility by 5
        elif i % 5 == 0:
            result.append("Buzz")
        # Not divisible by 3 or 5
        else:
            result.append(str(i))
    
    return result


# Alternative more concise solution
def fizzbuzz_concise(n):
    """
    Generate FizzBuzz sequence using string concatenation.
    
    Args:
        n: Integer representing the upper limit
        
    Returns:
        List of strings following FizzBuzz rules
    """
    result = []
    
    for i in range(1, n + 1):
        # Build the string based on divisibility
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        
        # If output is empty, use the number
        result.append(output or str(i))
    
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1
    n1 = 3
    print(f"Input: n = {n1}")
    print(f"Output: {fizzbuzz(n1)}")
    print()
    
    # Test case 2
    n2 = 5
    print(f"Input: n = {n2}")
    print(f"Output: {fizzbuzz(n2)}")
    print()
    
    # Test case 3
    n3 = 15
    print(f"Input: n = {n3}")
    print(f"Output: {fizzbuzz(n3)}")
    print()
    
    # Test case 4: Using concise approach
    n4 = 15
    print(f"Input: n = {n4} (concise approach)")
    print(f"Output: {fizzbuzz_concise(n4)}")
