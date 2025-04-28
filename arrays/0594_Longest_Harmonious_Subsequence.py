"""
LeetCode Problem #594: Longest Harmonious Subsequence

Problem Statement:
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array `nums`, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Example 2:
Input: nums = [1,2,3,4]
Output: 2

Example 3:
Input: nums = [1,1,1,1]
Output: 0

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -10^9 <= nums[i] <= 10^9
"""

# Solution
from collections import Counter

def findLHS(nums):
    """
    Finds the length of the longest harmonious subsequence in the given array.

    :param nums: List[int] - The input array of integers.
    :return: int - The length of the longest harmonious subsequence.
    """
    freq = Counter(nums)
    max_length = 0

    for num in freq:
        if num + 1 in freq:
            max_length = max(max_length, freq[num] + freq[num + 1])

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 2, 2, 5, 2, 3, 7]
    print(findLHS(nums1))  # Output: 5

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    print(findLHS(nums2))  # Output: 2

    # Test Case 3
    nums3 = [1, 1, 1, 1]
    print(findLHS(nums3))  # Output: 0

    # Test Case 4
    nums4 = [1, 2, 2, 1]
    print(findLHS(nums4))  # Output: 4

    # Test Case 5
    nums5 = [1]
    print(findLHS(nums5))  # Output: 0

"""
Time Complexity Analysis:
- Constructing the frequency counter takes O(n), where n is the length of the input array.
- Iterating through the keys of the frequency counter takes O(k), where k is the number of unique elements in the array.
- For each key, checking if `num + 1` exists in the counter is O(1).
- Overall, the time complexity is O(n), as k <= n.

Space Complexity Analysis:
- The space complexity is O(k), where k is the number of unique elements in the array, due to the storage of the frequency counter.
- In the worst case, k = n (all elements are unique), so the space complexity is O(n).

Topic: Arrays
"""