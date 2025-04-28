"""
LeetCode Problem #2407: Longest Increasing Subsequence II

Problem Statement:
You are given an integer array `nums` and an integer `k`. Find the length of the longest subsequence of `nums` such that all the elements of the subsequence are sorted in strictly increasing order and the difference between adjacent elements in the subsequence is at most `k`.

Return the length of the longest subsequence.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i], k <= 10^5
"""

from sortedcontainers import SortedDict

def lengthOfLIS(nums, k):
    """
    Function to find the length of the longest increasing subsequence
    with a difference of at most k between adjacent elements.
    """
    dp = SortedDict()  # To store the maximum length of LIS ending at each value
    max_length = 0

    for num in nums:
        # Query the range [num - k, num - 1] to find the maximum LIS length in that range
        start = max(0, num - k)
        end = num - 1
        max_in_range = 0

        for key in dp.irange(start, end):
            max_in_range = max(max_in_range, dp[key])

        # Update the LIS length for the current number
        dp[num] = max(dp.get(num, 0), max_in_range + 1)

        # Update the global maximum length
        max_length = max(max_length, dp[num])

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 2, 1, 4, 3, 4, 5, 8, 15]
    k1 = 3
    print(lengthOfLIS(nums1, k1))  # Expected Output: 5

    # Test Case 2
    nums2 = [7, 4, 5, 1, 8, 12, 4, 7]
    k2 = 5
    print(lengthOfLIS(nums2, k2))  # Expected Output: 4

    # Test Case 3
    nums3 = [1, 2, 3, 4]
    k3 = 1
    print(lengthOfLIS(nums3, k3))  # Expected Output: 4

    # Test Case 4
    nums4 = [10, 9, 8, 7, 6, 5]
    k4 = 2
    print(lengthOfLIS(nums4, k4))  # Expected Output: 1

"""
Time Complexity Analysis:
- The loop iterates over all elements in `nums`, so the time complexity is O(n), where n is the length of `nums`.
- For each element, we query and update the `SortedDict`. The query and update operations in `SortedDict` take O(log m) time, where m is the number of unique keys in the dictionary.
- In the worst case, m can be equal to n (if all elements in `nums` are unique). Thus, the overall time complexity is O(n log n).

Space Complexity Analysis:
- The `SortedDict` stores at most n unique keys, so the space complexity is O(n).

Topic: Dynamic Programming (DP) with Data Structures
"""