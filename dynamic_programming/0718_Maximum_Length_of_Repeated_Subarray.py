"""
LeetCode Problem #718: Maximum Length of Repeated Subarray

Problem Statement:
Given two integer arrays `nums1` and `nums2`, return the maximum length of a subarray that appears in both arrays.

Example 1:
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
Explanation: The repeated subarray with maximum length is [0,0,0,0,0].

Constraints:
- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 100
"""

# Solution
def findLength(nums1, nums2):
    """
    Finds the maximum length of a subarray that appears in both nums1 and nums2.

    :param nums1: List[int] - First input array
    :param nums2: List[int] - Second input array
    :return: int - Maximum length of repeated subarray
    """
    m, n = len(nums1), len(nums2)
    # Create a DP table with dimensions (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 2, 1]
    nums2 = [3, 2, 1, 4, 7]
    print(findLength(nums1, nums2))  # Output: 3

    # Test Case 2
    nums1 = [0, 0, 0, 0, 0]
    nums2 = [0, 0, 0, 0, 0]
    print(findLength(nums1, nums2))  # Output: 5

    # Test Case 3
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [5, 4, 3, 2, 1]
    print(findLength(nums1, nums2))  # Output: 1

    # Test Case 4
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, 2, 3, 4, 5]
    print(findLength(nums1, nums2))  # Output: 5

# Time and Space Complexity Analysis
"""
Time Complexity:
The solution uses a nested loop to fill the DP table. The outer loop runs for `m` iterations (length of nums1),
and the inner loop runs for `n` iterations (length of nums2). Therefore, the time complexity is O(m * n).

Space Complexity:
The solution uses a DP table of size (m+1) x (n+1). Hence, the space complexity is O(m * n).
"""

# Topic: Dynamic Programming