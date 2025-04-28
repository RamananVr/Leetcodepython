"""
LeetCode Problem #446: Arithmetic Slices II - Subsequence

Problem Statement:
Given an integer array nums, return the number of all the arithmetic subsequences of nums.

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

- For example, [1, 3, 5, 7, 9], [7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
- For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.

A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

- For example, [2, 5, 10] is a subsequence of [1, 2, 1, 2, 5, 10].

The test cases are generated such that the answer fits in a 32-bit integer.

Constraints:
- 1 <= nums.length <= 1000
- -2^31 <= nums[i] <= 2^31 - 1
"""

# Solution
def numberOfArithmeticSlices(nums):
    """
    Function to calculate the number of arithmetic subsequences in the given array.

    :param nums: List[int] - The input array of integers.
    :return: int - The number of arithmetic subsequences.
    """
    from collections import defaultdict

    n = len(nums)
    dp = [defaultdict(int) for _ in range(n)]
    total_count = 0

    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            count_at_j = dp[j][diff]
            dp[i][diff] += count_at_j + 1
            total_count += count_at_j

    return total_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 4, 6, 8, 10]
    print(numberOfArithmeticSlices(nums1))  # Expected Output: 7

    # Test Case 2
    nums2 = [7, 7, 7, 7]
    print(numberOfArithmeticSlices(nums2))  # Expected Output: 5

    # Test Case 3
    nums3 = [1, 3, 5, 7, 9, 11]
    print(numberOfArithmeticSlices(nums3))  # Expected Output: 16

    # Test Case 4
    nums4 = [1, 2, 3, 4]
    print(numberOfArithmeticSlices(nums4))  # Expected Output: 5

    # Test Case 5
    nums5 = [1, 1, 1, 1]
    print(numberOfArithmeticSlices(nums5))  # Expected Output: 5

"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop runs for `n` iterations, and the inner loop runs for up to `i` iterations.
- For each pair (i, j), we perform constant-time operations to update the dp table and count.
- Thus, the overall time complexity is O(n^2).

Space Complexity:
- We use a list of dictionaries (`dp`) to store the counts of arithmetic subsequences for each difference.
- Each dictionary can store up to `n` keys in the worst case, leading to a space complexity of O(n^2).

Topic: Dynamic Programming
"""