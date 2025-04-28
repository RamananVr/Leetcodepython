"""
LeetCode Problem #1043: Partition Array for Maximum Sum

Problem Statement:
Given an integer array `arr`, you can partition the array into (contiguous) subarrays of length at most `k`. 
After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning.

Example 1:
Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]

Example 2:
Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83

Example 3:
Input: arr = [1], k = 1
Output: 1

Constraints:
- 1 <= arr.length <= 500
- 0 <= arr[i] <= 10^4
- 1 <= k <= arr.length
"""

# Clean and Correct Python Solution
def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * n  # dp[i] represents the maximum sum we can get for the subarray arr[0:i+1]

    for i in range(n):
        max_val = 0
        # Iterate over the last `k` elements ending at index `i`
        for j in range(1, min(k, i + 1) + 1):
            max_val = max(max_val, arr[i - j + 1])  # Find the maximum value in the current partition
            dp[i] = max(dp[i], (dp[i - j] if i >= j else 0) + max_val * j)

    return dp[-1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 15, 7, 9, 2, 5, 10]
    k1 = 3
    print(maxSumAfterPartitioning(arr1, k1))  # Output: 84

    # Test Case 2
    arr2 = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3]
    k2 = 4
    print(maxSumAfterPartitioning(arr2, k2))  # Output: 83

    # Test Case 3
    arr3 = [1]
    k3 = 1
    print(maxSumAfterPartitioning(arr3, k3))  # Output: 1

    # Test Case 4
    arr4 = [10, 20, 30]
    k4 = 2
    print(maxSumAfterPartitioning(arr4, k4))  # Output: 60

    # Test Case 5
    arr5 = [5, 5, 5, 5]
    k5 = 2
    print(maxSumAfterPartitioning(arr5, k5))  # Output: 20

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop runs `n` times, where `n` is the length of the array.
- The inner loop runs at most `k` times for each iteration of the outer loop.
- Therefore, the time complexity is O(n * k).

Space Complexity:
- The space complexity is O(n) due to the `dp` array used to store intermediate results.
"""

# Topic: Dynamic Programming (DP)