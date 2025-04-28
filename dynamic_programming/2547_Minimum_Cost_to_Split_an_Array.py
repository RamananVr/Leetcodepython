"""
LeetCode Problem #2547: Minimum Cost to Split an Array

Problem Statement:
You are given an integer array `nums` and an integer `k`. Split the array into some number of non-empty subarrays such that the sum of the cost of each subarray is minimized.

The cost of a subarray is defined as:
- The number of distinct elements in the subarray, plus
- `k` (a fixed cost for splitting).

Return the minimum cost to split the array.

A subarray is a contiguous part of the array.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 100
- 1 <= k <= 1000
"""

# Solution
def minCost(nums, k):
    """
    Function to calculate the minimum cost to split the array.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The fixed cost for splitting.

    Returns:
    int: The minimum cost to split the array.
    """
    from collections import Counter
    from functools import lru_cache

    n = len(nums)

    # Precompute the cost of each subarray
    subarray_cost = [[0] * n for _ in range(n)]
    for i in range(n):
        freq = Counter()
        duplicates = 0
        for j in range(i, n):
            freq[nums[j]] += 1
            if freq[nums[j]] == 2:
                duplicates += 1
            elif freq[nums[j]] > 2:
                duplicates += 1
            subarray_cost[i][j] = k + (j - i + 1) - duplicates

    # Use dynamic programming to find the minimum cost
    @lru_cache(None)
    def dp(i):
        if i == n:
            return 0
        min_cost = float('inf')
        for j in range(i, n):
            min_cost = min(min_cost, subarray_cost[i][j] + dp(j + 1))
        return min_cost

    return dp(0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 1, 2, 1, 3]
    k1 = 2
    print(minCost(nums1, k1))  # Expected Output: 8

    # Test Case 2
    nums2 = [1, 2, 1, 2, 1]
    k2 = 5
    print(minCost(nums2, k2))  # Expected Output: 10

    # Test Case 3
    nums3 = [1, 1, 1, 1]
    k3 = 3
    print(minCost(nums3, k3))  # Expected Output: 7

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    k4 = 1
    print(minCost(nums4, k4))  # Expected Output: 6

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Precomputing the `subarray_cost` matrix takes O(n^2) time, where `n` is the length of the array.
   - The dynamic programming function `dp` explores all possible splits, which also takes O(n^2) time in the worst case.
   - Overall time complexity: O(n^2).

2. Space Complexity:
   - The `subarray_cost` matrix takes O(n^2) space.
   - The `lru_cache` for memoization takes O(n) space for the recursion stack and memoized results.
   - Overall space complexity: O(n^2).

Topic: Dynamic Programming
"""