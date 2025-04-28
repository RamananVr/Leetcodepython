"""
LeetCode Problem #1425: Constrained Subsequence Sum

Problem Statement:
Given an integer array `nums` and an integer `k`, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, `nums[i]` and `nums[j]`, where `i < j`, the condition `j - i <= k` is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length
"""

from collections import deque

def constrainedSubsetSum(nums, k):
    """
    Function to calculate the maximum sum of a constrained subsequence.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The maximum allowed distance between consecutive elements in the subsequence.

    Returns:
    int: The maximum sum of a constrained subsequence.
    """
    n = len(nums)
    dp = nums[:]  # dp[i] represents the maximum sum ending at index i
    dq = deque()  # Monotonic deque to store indices of `dp` in decreasing order

    for i in range(n):
        # If the deque is not empty, add the maximum value from the deque to dp[i]
        if dq:
            dp[i] += dp[dq[0]]

        # Maintain the monotonic property of the deque
        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()

        # Add the current index to the deque
        dq.append(i)

        # Remove indices that are out of the valid range (i - k)
        if dq[0] < i - k:
            dq.popleft()

    return max(dp)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [10, 2, -10, 5, 20]
    k1 = 2
    print(constrainedSubsetSum(nums1, k1))  # Expected Output: 37

    # Test Case 2
    nums2 = [-1, -2, -3]
    k2 = 1
    print(constrainedSubsetSum(nums2, k2))  # Expected Output: -1

    # Test Case 3
    nums3 = [10, -2, -10, -5, 20]
    k3 = 2
    print(constrainedSubsetSum(nums3, k3))  # Expected Output: 23

    # Test Case 4
    nums4 = [1, -1, -2, 4, -7, 3]
    k4 = 2
    print(constrainedSubsetSum(nums4, k4))  # Expected Output: 7

"""
Time Complexity Analysis:
- The loop iterates through the array once, so the time complexity is O(n).
- Each element is added to and removed from the deque at most once, so deque operations are O(n) in total.
- Overall time complexity: O(n).

Space Complexity Analysis:
- The `dp` array takes O(n) space.
- The deque can hold at most `k` elements at any time, so it takes O(k) space.
- Overall space complexity: O(n).

Topic: Dynamic Programming, Sliding Window, Monotonic Queue
"""