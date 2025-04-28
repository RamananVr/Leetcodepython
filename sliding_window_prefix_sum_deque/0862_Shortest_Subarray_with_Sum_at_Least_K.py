"""
LeetCode Problem #862: Shortest Subarray with Sum at Least K

Problem Statement:
Given an integer array `nums` and an integer `k`, return the length of the shortest non-empty subarray of `nums` with a sum of at least `k`. 
If there is no such subarray, return `-1`.

A subarray is a contiguous part of an array.

Constraints:
- 1 <= nums.length <= 10^5
- -10^5 <= nums[i] <= 10^5
- 1 <= k <= 10^9
"""

from collections import deque

def shortestSubarray(nums, k):
    """
    Finds the length of the shortest subarray with a sum of at least k.

    :param nums: List[int] - The input array of integers.
    :param k: int - The target sum.
    :return: int - The length of the shortest subarray with sum >= k, or -1 if no such subarray exists.
    """
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    
    # Compute prefix sums
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    # Deque to store indices of prefix sums
    dq = deque()
    min_length = float('inf')
    
    for i in range(n + 1):
        # Check if we can form a valid subarray
        while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
            min_length = min(min_length, i - dq.popleft())
        
        # Maintain deque in increasing order of prefix sums
        while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
            dq.pop()
        
        dq.append(i)
    
    return min_length if min_length != float('inf') else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1]
    k1 = 1
    print(shortestSubarray(nums1, k1))  # Output: 1

    # Test Case 2
    nums2 = [1, 2]
    k2 = 4
    print(shortestSubarray(nums2, k2))  # Output: -1

    # Test Case 3
    nums3 = [2, -1, 2]
    k3 = 3
    print(shortestSubarray(nums3, k3))  # Output: 3

    # Test Case 4
    nums4 = [84, -37, 32, 40, 95]
    k4 = 167
    print(shortestSubarray(nums4, k4))  # Output: 3

    # Test Case 5
    nums5 = [-28, 81, -20, 28, -29]
    k5 = 89
    print(shortestSubarray(nums5, k5))  # Output: 3

"""
Time Complexity:
- Computing the prefix sums takes O(n).
- Each index is added to and removed from the deque at most once, so the deque operations take O(n).
- Overall time complexity: O(n).

Space Complexity:
- The prefix_sum array takes O(n) space.
- The deque can hold at most O(n) indices.
- Overall space complexity: O(n).

Topic: Sliding Window, Prefix Sum, Deque
"""