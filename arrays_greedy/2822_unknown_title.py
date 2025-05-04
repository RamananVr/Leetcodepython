"""
LeetCode Question #2822: Create Maximum Number

Problem Statement:
You are given two integer arrays nums1 and nums2 of lengths m and n respectively. 
You are tasked to create the maximum number of length k <= m + n from digits of the two arrays. 
The result should be an array of integers of length k representing the maximum number.

The relative order of the digits from the same array must be preserved. 
In other words, you can only take digits from nums1 in the order they appear in nums1, 
and similarly for nums2. The digits from nums1 and nums2 can be interleaved freely.

You need to maximize the number represented by the resulting array.

Example:
Input: nums1 = [3, 4, 6, 5], nums2 = [9, 1, 2, 5, 8, 3], k = 5
Output: [9, 8, 6, 5, 3]

Constraints:
- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 9
- 1 <= k <= nums1.length + nums2.length
"""

# Solution
from typing import List

def createMaximumNumber(nums1: List[int], nums2: List[int], k: int) -> List[int]:
    def max_single_number(nums, select_count):
        """Find the maximum number of length select_count from nums."""
        stack = []
        drop = len(nums) - select_count
        for num in nums:
            while stack and drop > 0 and stack[-1] < num:
                stack.pop()
                drop -= 1
            stack.append(num)
        return stack[:select_count]

    def merge(nums1, nums2):
        """Merge two arrays to form the maximum number."""
        return [max(nums1, nums2).pop(0) for _ in range(len(nums1) + len(nums2))]

    max_number = []
    for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
        candidate = merge(max_single_number(nums1, i), max_single_number(nums2, k - i))
        max_number = max(max_number, candidate)
    return max_number

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    k = 5
    print(createMaximumNumber(nums1, nums2, k))  # Output: [9, 8, 6, 5, 3]

    # Test Case 2
    nums1 = [6, 7]
    nums2 = [6, 0, 4]
    k = 5
    print(createMaximumNumber(nums1, nums2, k))  # Output: [6, 7, 6, 0, 4]

    # Test Case 3
    nums1 = [3, 9]
    nums2 = [8, 9]
    k = 3
    print(createMaximumNumber(nums1, nums2, k))  # Output: [9, 8, 9]

# Time and Space Complexity Analysis
"""
Time Complexity:
- max_single_number: O(n) for each call, where n is the length of the input array.
- merge: O(k) for each call, where k is the total length of the merged array.
- The outer loop iterates up to min(len(nums1), k) times.
- Overall complexity: O(k * (m + n)), where m = len(nums1) and n = len(nums2).

Space Complexity:
- max_single_number uses a stack of size O(select_count).
- merge uses a temporary list of size O(k).
- Overall space complexity: O(k).
"""

# Topic: Arrays, Greedy