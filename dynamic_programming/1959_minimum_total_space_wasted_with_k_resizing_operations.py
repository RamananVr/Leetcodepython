"""
LeetCode Question #1959: Minimum Total Space Wasted With K Resizing Operations

Problem Statement:
You are given an integer array `nums` representing the sizes of files, and an integer `k`. You can perform the following operation up to `k` times:

- Choose any subarray of the array `nums` and resize it such that every element in this subarray is equal to the maximum value of that subarray.

The space wasted in this operation is defined as the sum of the difference between the resized array and the original array. Return the minimum total space wasted with at most `k` resizing operations. If it is impossible to resize the array within the given constraints, return -1.

Example 1:
Input: nums = [10, 20, 30], k = 1
Output: 10
Explanation: The optimal way is to resize the subarray [20, 30] to [30, 30]. The total space wasted is (30 - 20) + (30 - 30) = 10.

Example 2:
Input: nums = [10, 20, 15, 30, 20], k = 2
Output: 15
Explanation: The optimal way is to resize the subarray [20, 15] to [20, 20] and the subarray [30, 20] to [30, 30]. The total space wasted is (20 - 15) + (30 - 20) = 15.

Constraints:
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 10^6
- 0 <= k <= nums.length - 1
"""

# Python Solution
from functools import lru_cache

def minSpaceWastedKResizing(nums, k):
    n = len(nums)
    
    # Precompute the maximum and sum for all subarrays
    max_in_subarray = [[0] * n for _ in range(n)]
    sum_in_subarray = [[0] * n for _ in range(n)]
    
    for i in range(n):
        max_in_subarray[i][i] = nums[i]
        sum_in_subarray[i][i] = nums[i]
        for j in range(i + 1, n):
            max_in_subarray[i][j] = max(max_in_subarray[i][j - 1], nums[j])
            sum_in_subarray[i][j] = sum_in_subarray[i][j - 1] + nums[j]
    
    # Memoization using lru_cache
    @lru_cache(None)
    def dp(index, k):
        if index == n:
            return 0
        if k < 0:
            return float('inf')
        
        result = float('inf')
        for j in range(index, n):
            max_val = max_in_subarray[index][j]
            sum_val = sum_in_subarray[index][j]
            wasted_space = max_val * (j - index + 1) - sum_val
            result = min(result, wasted_space + dp(j + 1, k - 1))
        
        return result
    
    # Start the DP from index 0 with k resizing operations
    answer = dp(0, k)
    return answer if answer != float('inf') else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [10, 20, 30]
    k1 = 1
    print(minSpaceWastedKResizing(nums1, k1))  # Output: 10

    # Test Case 2
    nums2 = [10, 20, 15, 30, 20]
    k2 = 2
    print(minSpaceWastedKResizing(nums2, k2))  # Output: 15

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    k3 = 0
    print(minSpaceWastedKResizing(nums3, k3))  # Output: 10

    # Test Case 4
    nums4 = [1, 1, 1, 1, 1]
    k4 = 2
    print(minSpaceWastedKResizing(nums4, k4))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Precomputing the maximum and sum for all subarrays takes O(n^2).
- The DP function iterates over all possible subarrays and uses memoization, resulting in O(n^2 * k) complexity.
- Overall time complexity: O(n^2 + n^2 * k) = O(n^2 * k).

Space Complexity:
- The `max_in_subarray` and `sum_in_subarray` arrays take O(n^2) space.
- The memoization cache for the DP function takes O(n * k) space.
- Overall space complexity: O(n^2 + n * k).

Topic: Dynamic Programming
"""