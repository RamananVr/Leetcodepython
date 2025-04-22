"""
LeetCode Problem #813: Largest Sum of Averages

Problem Statement:
You are given an integer array `nums` and an integer `k`. You want to divide the array into `k` non-empty contiguous subarrays, 
such that the sum of averages of these subarrays is maximized.

Return the maximum sum of averages that can be achieved.

Note:
- The average of a subarray is the sum of the elements in the subarray divided by the number of elements in the subarray.
- You may assume that the answer is always a floating-point number and can be represented with at least two decimal places.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 10^4
- 1 <= k <= nums.length
"""

# Solution
def largestSumOfAverages(nums, k):
    """
    Function to calculate the largest sum of averages by dividing the array into k subarrays.

    :param nums: List[int] - The input array of integers.
    :param k: int - The number of subarrays to divide into.
    :return: float - The maximum sum of averages.
    """
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    
    # Compute prefix sums for efficient range sum calculation
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    # dp[i][j] represents the maximum sum of averages for the first i elements divided into j subarrays
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Base case: When k = 1, the entire array is one subarray
    for i in range(1, n + 1):
        dp[i][1] = prefix_sum[i] / i
    
    # Fill the DP table for k > 1
    for j in range(2, k + 1):  # Number of subarrays
        for i in range(1, n + 1):  # Consider the first i elements
            for p in range(1, i):  # Partition point
                dp[i][j] = max(dp[i][j], dp[p][j - 1] + (prefix_sum[i] - prefix_sum[p]) / (i - p))
    
    return dp[n][k]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [9, 1, 2, 3, 9]
    k1 = 3
    print(f"Test Case 1: {largestSumOfAverages(nums1, k1)}")  # Expected Output: 20.0

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5, 6, 7]
    k2 = 4
    print(f"Test Case 2: {largestSumOfAverages(nums2, k2)}")  # Expected Output: 20.5

    # Test Case 3
    nums3 = [4, 1, 7, 5, 6, 2, 3]
    k3 = 2
    print(f"Test Case 3: {largestSumOfAverages(nums3, k3)}")  # Expected Output: 18.166666666666668

# Time and Space Complexity Analysis
"""
Time Complexity:
- Computing prefix sums takes O(n).
- The DP table has dimensions (n+1) x (k+1), and for each cell, we iterate over all possible partition points (up to n).
- Thus, the overall time complexity is O(n^2 * k).

Space Complexity:
- The space complexity is dominated by the DP table and the prefix sum array, both of which require O(n * k) and O(n) space respectively.
- Therefore, the overall space complexity is O(n * k).
"""

# Topic: Dynamic Programming