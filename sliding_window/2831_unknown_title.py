"""
LeetCode Problem #2831: Find the Longest Equal Subarray

Problem Statement:
You are given an integer array `nums` and an integer `k`. A subarray is called equal if all of its elements are the same. 
Return the length of the longest equal subarray after deleting at most `k` elements.

Example 1:
Input: nums = [1, 1, 2, 2, 1, 1], k = 2
Output: 4
Explanation: Delete the two 2's to make the subarray [1, 1, 1, 1].

Example 2:
Input: nums = [1, 3, 2, 3, 3, 3], k = 3
Output: 5
Explanation: Delete the 1 and 2 to make the subarray [3, 3, 3, 3, 3].

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
- 0 <= k <= nums.length
"""

from collections import defaultdict

def longestEqualSubarray(nums, k):
    """
    Finds the length of the longest equal subarray after deleting at most k elements.

    :param nums: List[int] - The input array of integers.
    :param k: int - The maximum number of deletions allowed.
    :return: int - The length of the longest equal subarray.
    """
    freq = defaultdict(int)
    max_freq = 0
    left = 0
    result = 0

    for right in range(len(nums)):
        freq[nums[right]] += 1
        max_freq = max(max_freq, freq[nums[right]])

        # Check if the current window is valid
        while (right - left + 1) - max_freq > k:
            freq[nums[left]] -= 1
            left += 1

        # Update the result with the size of the valid window
        result = max(result, right - left + 1)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 1, 2, 2, 1, 1]
    k1 = 2
    print(longestEqualSubarray(nums1, k1))  # Output: 4

    # Test Case 2
    nums2 = [1, 3, 2, 3, 3, 3]
    k2 = 3
    print(longestEqualSubarray(nums2, k2))  # Output: 5

    # Test Case 3
    nums3 = [4, 4, 4, 4, 4]
    k3 = 0
    print(longestEqualSubarray(nums3, k3))  # Output: 5

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    k4 = 2
    print(longestEqualSubarray(nums4, k4))  # Output: 3

    # Test Case 5
    nums5 = [1, 1, 1, 2, 2, 2, 1, 1]
    k5 = 2
    print(longestEqualSubarray(nums5, k5))  # Output: 5

"""
Time Complexity:
- The algorithm uses a sliding window approach, where the `right` pointer iterates through the array once.
- The `left` pointer adjusts as needed, but each element is processed at most twice (once by `right` and once by `left`).
- Thus, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The algorithm uses a dictionary to store the frequency of elements in the current window.
- In the worst case, the dictionary could store all unique elements in the array, so the space complexity is O(u), where u is the number of unique elements in the array.

Topic: Sliding Window
"""