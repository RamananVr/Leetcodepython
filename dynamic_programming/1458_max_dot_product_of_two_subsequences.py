"""
LeetCode Question #1458: Max Dot Product of Two Subsequences

Problem Statement:
Given two arrays `nums1` and `nums2`, return the maximum dot product between 
non-empty subsequences of the two arrays.

A subsequence of a sequence is a new sequence generated from the original 
sequence with some elements (can be none) deleted without changing the 
relative order of the remaining elements. For example, [2,3] is a subsequence 
of [1,2,3,4].

The dot product of two arrays is the sum of their element-wise multiplication.

Constraints:
- 1 <= nums1.length, nums2.length <= 500
- -1000 <= nums1[i], nums2[i] <= 1000
"""

# Solution
def maxDotProduct(nums1, nums2):
    """
    Dynamic Programming solution to find the maximum dot product of two subsequences.
    """
    m, n = len(nums1), len(nums2)
    # Initialize a DP table with very small values (negative infinity)
    dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Calculate the dot product of the current elements
            current_product = nums1[i - 1] * nums2[j - 1]
            # Update the DP table with the maximum of:
            # 1. Including the current pair in the dot product
            # 2. Continuing without including the current pair
            # 3. Starting a new subsequence with the current pair
            dp[i][j] = max(
                dp[i - 1][j],  # Skip nums1[i-1]
                dp[i][j - 1],  # Skip nums2[j-1]
                dp[i - 1][j - 1] + current_product,  # Include current pair
                current_product  # Start a new subsequence with the current pair
            )

    # The result is stored in dp[m][n]
    return dp[m][n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 1, -2, 5]
    nums2 = [3, 0, -6]
    print(maxDotProduct(nums1, nums2))  # Expected Output: 18

    # Test Case 2
    nums1 = [3, -2]
    nums2 = [2, -6, 7]
    print(maxDotProduct(nums1, nums2))  # Expected Output: 21

    # Test Case 3
    nums1 = [-1, -1]
    nums2 = [1, 1]
    print(maxDotProduct(nums1, nums2))  # Expected Output: -1

    # Test Case 4
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    print(maxDotProduct(nums1, nums2))  # Expected Output: 32

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution uses a nested loop to fill a DP table of size m x n, where m is the length of nums1 and n is the length of nums2.
- Therefore, the time complexity is O(m * n).

Space Complexity:
- The DP table requires O(m * n) space to store intermediate results.
- Thus, the space complexity is O(m * n).
"""

# Topic: Dynamic Programming