"""
LeetCode Question #1: Two Sum

Problem Statement:
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
"""

def twoSum(nums, target):
    """
    Finds two indices in the array `nums` such that their values add up to `target`.

    Args:
    nums (List[int]): The list of integers.
    target (int): The target sum.

    Returns:
    List[int]: A list containing the indices of the two numbers that add up to `target`.
    """
    # Dictionary to store the value and its index
    num_to_index = {}
    
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_to_index:
            return [num_to_index[complement], i]
        
        # Store the current number and its index in the dictionary
        num_to_index[num] = i

# Example test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(twoSum(nums1, target1))  # Output: [0, 1]

    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(twoSum(nums2, target2))  # Output: [1, 2]

    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print(twoSum(nums3, target3))  # Output: [0, 1]

# Topic: Arrays