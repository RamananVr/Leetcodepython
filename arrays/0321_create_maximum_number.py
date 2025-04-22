"""
LeetCode Question #321: Create Maximum Number

Problem Statement:
You are given two integer arrays nums1 and nums2 of lengths m and n respectively. 
You are tasked to create the maximum number of length k <= m + n from digits of the two arrays. 
The relative order of the digits from the same array must be preserved. 
Return an array of the k digits.

Note: You should try to maximize the number formed.

Example 1:
Input: nums1 = [3, 4, 6, 5], nums2 = [9, 1, 2, 5, 8, 3], k = 5
Output: [9, 8, 6, 5, 3]

Example 2:
Input: nums1 = [6, 7], nums2 = [6, 0, 4], k = 5
Output: [6, 7, 6, 0, 4]

Example 3:
Input: nums1 = [3, 9], nums2 = [8, 9], k = 3
Output: [9, 8, 9]

Constraints:
- m == nums1.length
- n == nums2.length
- 1 <= m, n <= 1000
- 1 <= k <= m + n
- 0 <= nums1[i], nums2[i] <= 9
"""

# Python Solution
from typing import List

def maxNumber(nums1: List[int], nums2: List[int], k: int) -> List[int]:
    def maxSingleNumber(nums: List[int], k: int) -> List[int]:
        """Find the maximum number of length k from a single array."""
        stack = []
        drop = len(nums) - k
        for num in nums:
            while stack and drop > 0 and stack[-1] < num:
                stack.pop()
                drop -= 1
            stack.append(num)
        return stack[:k]

    def merge(nums1: List[int], nums2: List[int]) -> List[int]:
        """Merge two arrays to form the largest number."""
        return [max(nums1, nums2).pop(0) for _ in range(len(nums1) + len(nums2))]

    max_result = []
    for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
        part1 = maxSingleNumber(nums1, i)
        part2 = maxSingleNumber(nums2, k - i)
        max_result = max(max_result, merge(part1, part2))
    return max_result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    k = 5
    print(maxNumber(nums1, nums2, k))  # Output: [9, 8, 6, 5, 3]

    # Test Case 2
    nums1 = [6, 7]
    nums2 = [6, 0, 4]
    k = 5
    print(maxNumber(nums1, nums2, k))  # Output: [6, 7, 6, 0, 4]

    # Test Case 3
    nums1 = [3, 9]
    nums2 = [8, 9]
    k = 3
    print(maxNumber(nums1, nums2, k))  # Output: [9, 8, 9]

# Time and Space Complexity Analysis
"""
Time Complexity:
- maxSingleNumber: O(n) for each array, where n is the length of the array.
- merge: O(k), where k is the total length of the merged array.
- The outer loop iterates up to min(len(nums1), k) times.
Overall complexity: O(k * (m + n)), where m and n are the lengths of nums1 and nums2.

Space Complexity:
- maxSingleNumber uses a stack of size O(k).
- merge uses temporary space proportional to the merged array size O(k).
Overall space complexity: O(k).
"""

# Topic: Arrays