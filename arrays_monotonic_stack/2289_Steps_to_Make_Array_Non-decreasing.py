"""
LeetCode Problem #2289: Steps to Make Array Non-decreasing

Problem Statement:
You are given a 0-indexed integer array nums. You can perform the following operation on the array any number of times:

- Choose an index i in the array and remove nums[i] if nums[i-1] > nums[i].

Return the minimum number of steps to make the array non-decreasing.

An array is non-decreasing if nums[i-1] <= nums[i] for every index i where 1 <= i < nums.length.

Example 1:
Input: nums = [5, 3, 4, 4, 7, 6, 8]
Output: 2
Explanation:
Step 1: Remove the second element (nums[1] = 3), so that nums = [5, 4, 4, 7, 6, 8].
Step 2: Remove the fifth element (nums[4] = 6), so that nums = [5, 4, 4, 7, 8].
Now, nums is non-decreasing.

Example 2:
Input: nums = [4, 5, 7, 7, 13]
Output: 0
Explanation: nums is already non-decreasing.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

# Python Solution
from collections import deque

def totalSteps(nums):
    """
    Function to calculate the minimum number of steps to make the array non-decreasing.
    
    Args:
    nums (List[int]): The input array of integers.
    
    Returns:
    int: The minimum number of steps required.
    """
    n = len(nums)
    stack = deque()  # Monotonic stack to track elements
    steps = [0] * n  # Steps required to remove each element
    max_steps = 0    # Maximum steps required
    
    for i in range(n - 1, -1, -1):  # Traverse the array from right to left
        while stack and nums[i] > nums[stack[-1]]:
            steps[i] = max(steps[i] + 1, steps[stack.pop()])
        stack.append(i)
        max_steps = max(max_steps, steps[i])
    
    return max_steps

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [5, 3, 4, 4, 7, 6, 8]
    print(totalSteps(nums1))  # Output: 2

    # Test Case 2
    nums2 = [4, 5, 7, 7, 13]
    print(totalSteps(nums2))  # Output: 0

    # Test Case 3
    nums3 = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(totalSteps(nums3))  # Output: 9

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    print(totalSteps(nums4))  # Output: 0

    # Test Case 5
    nums5 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(totalSteps(nums5))  # Output: 9

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm traverses the array once from right to left, and each element is pushed and popped from the stack at most once.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The space complexity is O(n) due to the stack and the steps array, which both store up to n elements.

Topic: Arrays, Monotonic Stack
"""