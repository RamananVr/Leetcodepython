"""
LeetCode Problem #2962: Minimum Cost to Split an Array

Problem Statement:
You are given an integer array `nums` and an integer `k`. Split the array into some number of non-empty subarrays such that the sum of the cost of each subarray is minimized.

The cost of a subarray is defined as:
- The number of distinct elements in the subarray, plus `k`.

Return the minimum cost to split the array.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 100
- 1 <= k <= 1000
"""

from collections import defaultdict

def minCost(nums, k):
    """
    Function to calculate the minimum cost to split the array.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The additional cost for each subarray.

    Returns:
    int: The minimum cost to split the array.
    """
    n = len(nums)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        freq = defaultdict(int)
        distinct_count = 0
        for j in range(i, 0, -1):
            freq[nums[j - 1]] += 1
            if freq[nums[j - 1]] == 1:
                distinct_count += 1
            elif freq[nums[j - 1]] == 2:
                distinct_count -= 1
            dp[i] = min(dp[i], dp[j - 1] + distinct_count + k)

    return dp[n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 1, 2, 1, 3]
    k1 = 2
    print(minCost(nums1, k1))  # Expected Output: 8

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    k2 = 5
    print(minCost(nums2, k2))  # Expected Output: 9

    # Test Case 3
    nums3 = [1, 1, 1, 1]
    k3 = 3
    print(minCost(nums3, k3))  # Expected Output: 7

    # Test Case 4
    nums4 = [1, 2, 1, 2, 1]
    k4 = 1
    print(minCost(nums4, k4))  # Expected Output: 7

"""
Time Complexity Analysis:
- The outer loop runs `n` times, where `n` is the length of the array.
- The inner loop runs at most `n` times for each iteration of the outer loop.
- Thus, the overall time complexity is O(n^2).

Space Complexity Analysis:
- The space complexity is O(n) for the `dp` array and O(n) for the `freq` dictionary.
- Therefore, the total space complexity is O(n).

Topic: Dynamic Programming
"""