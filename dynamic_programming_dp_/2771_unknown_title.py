"""
LeetCode Problem #2771: Longest Non-Decreasing Subarray From Two Arrays

Problem Statement:
You are given two integer arrays `nums1` and `nums2`, both of length `n`. You can choose any one of the arrays and start traversing it from any index `i` (0 <= i < n). From that index, you can continue traversing the same array or switch to the other array at any point, but you can only move to the next index in either array.

Your task is to find the length of the longest non-decreasing subarray you can obtain by following the above rules.

Constraints:
- `1 <= n <= 10^5`
- `1 <= nums1[i], nums2[i] <= 10^9`

Example:
Input: nums1 = [2, 3, 1], nums2 = [1, 2, 1]
Output: 2
Explanation: You can start at index 0 in nums1 and switch to nums2 at index 1. The subarray [2, 2] is non-decreasing.

Follow-up:
Can you solve this problem in O(n) time complexity?
"""

def maxNonDecreasingLength(nums1, nums2):
    """
    Function to find the length of the longest non-decreasing subarray
    that can be formed by switching between nums1 and nums2.

    Args:
    nums1 (List[int]): First array of integers.
    nums2 (List[int]): Second array of integers.

    Returns:
    int: Length of the longest non-decreasing subarray.
    """
    n = len(nums1)
    dp1, dp2 = 1, 1  # dp1: max length ending in nums1, dp2: max length ending in nums2
    max_length = 1

    for i in range(1, n):
        new_dp1 = new_dp2 = 1

        # Update dp1: Continue from nums1[i-1] or nums2[i-1]
        if nums1[i] >= nums1[i - 1]:
            new_dp1 = max(new_dp1, dp1 + 1)
        if nums1[i] >= nums2[i - 1]:
            new_dp1 = max(new_dp1, dp2 + 1)

        # Update dp2: Continue from nums2[i-1] or nums1[i-1]
        if nums2[i] >= nums2[i - 1]:
            new_dp2 = max(new_dp2, dp2 + 1)
        if nums2[i] >= nums1[i - 1]:
            new_dp2 = max(new_dp2, dp1 + 1)

        dp1, dp2 = new_dp1, new_dp2
        max_length = max(max_length, dp1, dp2)

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 1]
    nums2 = [1, 2, 1]
    print(maxNonDecreasingLength(nums1, nums2))  # Output: 2

    # Test Case 2
    nums1 = [1, 2, 3, 4]
    nums2 = [4, 3, 2, 1]
    print(maxNonDecreasingLength(nums1, nums2))  # Output: 4

    # Test Case 3
    nums1 = [1, 1, 1, 1]
    nums2 = [1, 1, 1, 1]
    print(maxNonDecreasingLength(nums1, nums2))  # Output: 4

    # Test Case 4
    nums1 = [10, 20, 30]
    nums2 = [5, 15, 25]
    print(maxNonDecreasingLength(nums1, nums2))  # Output: 3

    # Test Case 5
    nums1 = [5, 6, 7, 8]
    nums2 = [1, 2, 3, 4]
    print(maxNonDecreasingLength(nums1, nums2))  # Output: 4

"""
Time Complexity:
- The solution iterates through the arrays once, performing constant-time operations for each index.
- Therefore, the time complexity is O(n), where n is the length of the arrays.

Space Complexity:
- The solution uses a constant amount of extra space (dp1, dp2, and a few variables).
- Therefore, the space complexity is O(1).

Topic: Dynamic Programming (DP)
"""