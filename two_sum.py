"""
Problem Statement:
LeetCode Question #1: Two Sum

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9, so we return [0, 1].

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.
"""

def two_sum(nums, target):
    """
    Solves the Two Sum problem by using a hash map to store the indices of numbers
    as we iterate through the list. This allows for efficient lookup of the complement
    needed to reach the target.

    Args:
        nums (List[int]): List of integers.
        target (int): Target sum.

    Returns:
        List[int]: Indices of the two numbers that add up to the target.
    """
    # Create a dictionary to store the indices of numbers
    num_to_index = {}
    
    # Iterate through the list
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_to_index:
            # Return the indices of the current number and its complement
            return [num_to_index[complement], i]
        
        # Store the current number and its index in the dictionary
        num_to_index[num] = i
    
    # If no solution is found (shouldn't happen due to constraints), return an empty list
    return []

# Example test cases
if __name__ == "__main__":
    # Test case 1
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))  # Output: [0, 1]

    # Test case 2
    nums = [3, 2, 4]
    target = 6
    print(two_sum(nums, target))  # Output: [1, 2]

    # Test case 3
    nums = [3, 3]
    target = 6
    print(two_sum(nums, target))  # Output: [0, 1]

    # Test case 4
    nums = [1, 5, 7, 3]
    target = 8
    print(two_sum(nums, target))  # Output: [0, 3]