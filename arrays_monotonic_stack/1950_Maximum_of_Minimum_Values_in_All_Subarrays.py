"""
LeetCode Problem #1950: Maximum of Minimum Values in All Subarrays

Problem Statement:
You are given an integer array `nums` of size `n`. Consider all the non-empty subarrays of `nums`. 
For each subarray, find the minimum value in that subarray. Among all these minimum values, find the maximum.

Return an integer array `answer` of size `n` such that `answer[i]` is the maximum of the minimum values of all subarrays 
of size `i + 1` in `nums`.

Example:
Input: nums = [0,1,2,4]
Output: [4,2,1,0]

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
"""

from typing import List

def findMaximums(nums: List[int]) -> List[int]:
    """
    Function to find the maximum of minimum values in all subarrays of size i+1.
    """
    n = len(nums)
    left = [-1] * n  # Nearest smaller element to the left
    right = [n] * n  # Nearest smaller element to the right
    stack = []

    # Compute the nearest smaller element to the left
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)

    stack = []

    # Compute the nearest smaller element to the right
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)

    # Result array to store the maximum of minimums for each window size
    result = [0] * n
    window = [0] * (n + 1)

    # Calculate the maximum of minimums for each window size
    for i in range(n):
        length = right[i] - left[i] - 1
        window[length] = max(window[length], nums[i])

    # Fill the result array by propagating the maximum values
    for i in range(n - 1, 0, -1):
        window[i] = max(window[i], window[i + 1])

    return window[1:]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [0, 1, 2, 4]
    print(findMaximums(nums))  # Output: [4, 2, 1, 0]

    # Test Case 2
    nums = [10, 20, 50, 10]
    print(findMaximums(nums))  # Output: [50, 20, 10, 10]

    # Test Case 3
    nums = [1, 2, 3, 4, 5]
    print(findMaximums(nums))  # Output: [5, 4, 3, 2, 1]

    # Test Case 4
    nums = [5, 4, 3, 2, 1]
    print(findMaximums(nums))  # Output: [5, 4, 3, 2, 1]

"""
Time Complexity:
- The algorithm involves two passes to compute the nearest smaller elements to the left and right, 
  which takes O(n) time. Additionally, filling the result array also takes O(n) time.
- Overall time complexity: O(n).

Space Complexity:
- The algorithm uses three auxiliary arrays (`left`, `right`, and `window`) of size n, 
  and a stack that can grow up to size n in the worst case.
- Overall space complexity: O(n).

Topic: Arrays, Monotonic Stack
"""