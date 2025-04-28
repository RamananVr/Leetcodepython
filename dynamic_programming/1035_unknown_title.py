"""
LeetCode Problem #1035: Uncrossed Lines

Problem Statement:
We are given two integer arrays nums1 and nums2. A "line" is a pair of indices (i, j) such that:
- nums1[i] == nums2[j], and
- the line connecting nums1[i] and nums2[j] does not intersect any other connecting lines.

Return the maximum number of connecting lines we can draw in this way.

Constraints:
- 1 <= nums1.length, nums2.length <= 500
- 1 <= nums1[i], nums2[j] <= 2000
"""

def maxUncrossedLines(nums1, nums2):
    """
    Dynamic Programming solution to find the maximum number of uncrossed lines.
    This is similar to finding the Longest Common Subsequence (LCS) of two arrays.
    
    :param nums1: List[int] - First array of integers
    :param nums2: List[int] - Second array of integers
    :return: int - Maximum number of uncrossed lines
    """
    m, n = len(nums1), len(nums2)
    # Create a DP table with dimensions (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 4, 2]
    nums2 = [1, 2, 4]
    print(maxUncrossedLines(nums1, nums2))  # Output: 2

    # Test Case 2
    nums1 = [2, 5, 1, 2, 5]
    nums2 = [10, 5, 2, 1, 5, 2]
    print(maxUncrossedLines(nums1, nums2))  # Output: 3

    # Test Case 3
    nums1 = [1, 3, 7, 1, 7, 5]
    nums2 = [1, 9, 2, 5, 1]
    print(maxUncrossedLines(nums1, nums2))  # Output: 2

"""
Time Complexity:
- The solution uses a nested loop to fill a DP table of size (m+1) x (n+1), where m = len(nums1) and n = len(nums2).
- Therefore, the time complexity is O(m * n).

Space Complexity:
- The DP table requires O(m * n) space to store intermediate results.
- Thus, the space complexity is O(m * n).

Topic: Dynamic Programming
"""