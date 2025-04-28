"""
LeetCode Problem #2786: Visit Array Positions to Maximize Score

Problem Statement:
You are given a 0-indexed integer array `nums` and a positive integer `x`.

You are initially at position `0` in the array and you can visit other positions according to the following rules:
1. If you are currently at position `i`, then you can move to any position `j` such that `j > i`.
2. You get a score equal to `nums[j]` if `nums[j]` and `nums[i]` have the same parity (even or odd). Otherwise, you lose `x` points.

Return the maximum score you can achieve if you visit the positions optimally. The score you start with is `nums[0]`.

Constraints:
- `1 <= nums.length <= 10^5`
- `1 <= nums[i], x <= 10^6`
"""

from collections import deque

def maxScore(nums, x):
    """
    Function to calculate the maximum score achievable by visiting array positions optimally.

    :param nums: List[int] - The input array of integers.
    :param x: int - The penalty for visiting a position with a different parity.
    :return: int - The maximum score achievable.
    """
    n = len(nums)
    
    # Initialize dp arrays for even and odd indices
    even_dp = float('-inf')  # Maximum score ending at an even index
    odd_dp = float('-inf')   # Maximum score ending at an odd index
    
    # Start with the first element
    if nums[0] % 2 == 0:
        even_dp = nums[0]
    else:
        odd_dp = nums[0]
    
    # Iterate through the array
    for i in range(1, n):
        if nums[i] % 2 == 0:  # Current number is even
            even_dp = max(even_dp, odd_dp - x) + nums[i]
        else:  # Current number is odd
            odd_dp = max(odd_dp, even_dp - x) + nums[i]
    
    # The result is the maximum score achievable at the last position
    return max(even_dp, odd_dp)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 6, 1, 9, 2]
    x1 = 5
    print(maxScore(nums1, x1))  # Expected Output: 13

    # Test Case 2
    nums2 = [2, 4, 6, 8]
    x2 = 3
    print(maxScore(nums2, x2))  # Expected Output: 20

    # Test Case 3
    nums3 = [1, 3, 5, 7]
    x3 = 2
    print(maxScore(nums3, x3))  # Expected Output: 16

    # Test Case 4
    nums4 = [10, 15, 20, 25, 30]
    x4 = 10
    print(maxScore(nums4, x4))  # Expected Output: 55

"""
Time Complexity Analysis:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space for the `even_dp` and `odd_dp` variables.
- Therefore, the space complexity is O(1).

Topic: Dynamic Programming (DP)
"""