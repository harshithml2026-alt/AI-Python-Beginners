"""
LeetCode Problem #1: Two Sum

Problem Description:
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Time Complexity: O(n)
Space Complexity: O(n)
"""


def two_sum(nums, target):
    """
    Find two numbers in the array that sum to the target value.
    
    Args:
        nums: List of integers
        target: Target sum value
        
    Returns:
        List containing the indices of the two numbers
    """
    # Dictionary to store value -> index mapping
    seen = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate what number we need to find
        complement = target - num
        
        # Check if we've seen the complement before
        if complement in seen:
            # Return the indices
            return [seen[complement], i]
        
        # Store the current number and its index
        seen[num] = i
    
    # No solution found (shouldn't happen based on problem constraints)
    return []


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {two_sum(nums1, target1)}")
    print()
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {two_sum(nums2, target2)}")
    print()
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {two_sum(nums3, target3)}")
