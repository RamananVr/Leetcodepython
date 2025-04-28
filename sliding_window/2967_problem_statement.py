"""
LeetCode Question #2967: Problem Statement

You are given a 0-indexed integer array nums of length n. You are tasked with finding the maximum sum of a subarray 
of nums such that the subarray contains at most k distinct integers.

A subarray is a contiguous non-empty sequence of elements within an array.

Return the maximum sum of such a subarray.

Example:
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: The subarray [2,1,2] contains at most 2 distinct integers and has the maximum sum of 7.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
- 1 <= k <= nums.length
"""

# Solution
from collections import defaultdict

def maxSumWithKDistinct(nums, k):
    """
    Finds the maximum sum of a subarray with at most k distinct integers.

    :param nums: List[int] - The input array of integers.
    :param k: int - The maximum number of distinct integers allowed in the subarray.
    :return: int - The maximum sum of such a subarray.
    """
    n = len(nums)
    left = 0
    max_sum = 0
    current_sum = 0
    freq = defaultdict(int)

    for right in range(n):
        # Add the current number to the frequency map and update the current sum
        freq[nums[right]] += 1
        current_sum += nums[right]

        # If the number of distinct integers exceeds k, shrink the window
        while len(freq) > k:
            freq[nums[left]] -= 1
            current_sum -= nums[left]
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1

        # Update the maximum sum
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [1, 2, 1, 2, 3]
    k = 2
    print(maxSumWithKDistinct(nums, k))  # Output: 7

    # Test Case 2
    nums = [4, 4, 4, 4]
    k = 1
    print(maxSumWithKDistinct(nums, k))  # Output: 16

    # Test Case 3
    nums = [1, 2, 3, 4, 5]
    k = 3
    print(maxSumWithKDistinct(nums, k))  # Output: 12

    # Test Case 4
    nums = [1, 2, 1, 3, 4, 2, 1]
    k = 3
    print(maxSumWithKDistinct(nums, k))  # Output: 10

    # Test Case 5
    nums = [1]
    k = 1
    print(maxSumWithKDistinct(nums, k))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array once with the `right` pointer, and the `left` pointer moves only when the 
  number of distinct integers exceeds k. Thus, the overall time complexity is O(n), where n is the length of the array.

Space Complexity:
- The space complexity is O(k), as the frequency map stores at most k distinct integers at any given time.
"""

# Topic: Sliding Window