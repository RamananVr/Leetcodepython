"""
LeetCode Question #491: Non-decreasing Subsequences

Problem Statement:
Given an integer array `nums`, return all the different possible non-decreasing subsequences of the given array with at least two elements. 
You may return the answer in any order.

A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Constraints:
- 1 <= nums.length <= 15
- -100 <= nums[i] <= 100

Example:
Input: nums = [4, 6, 7, 7]
Output: [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]]

Input: nums = [4, 4, 3, 2, 1]
Output: [[4, 4]]
"""

# Solution
from typing import List

def findSubsequences(nums: List[int]) -> List[List[int]]:
    def dfs(start: int, path: List[int]):
        if len(path) >= 2:
            result.add(tuple(path))  # Use a set to avoid duplicates
        for i in range(start, len(nums)):
            if not path or nums[i] >= path[-1]:  # Ensure non-decreasing order
                dfs(i + 1, path + [nums[i]])

    result = set()
    dfs(0, [])
    return [list(seq) for seq in result]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 6, 7, 7]
    print("Input:", nums1)
    print("Output:", findSubsequences(nums1))
    # Expected Output: [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]]

    # Test Case 2
    nums2 = [4, 4, 3, 2, 1]
    print("Input:", nums2)
    print("Output:", findSubsequences(nums2))
    # Expected Output: [[4, 4]]

    # Test Case 3
    nums3 = [1, 2, 3, 4]
    print("Input:", nums3)
    print("Output:", findSubsequences(nums3))
    # Expected Output: [[1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 3], [1, 3, 4], [1, 4], [2, 3], [2, 3, 4], [2, 4], [3, 4]]

    # Test Case 4
    nums4 = [1]
    print("Input:", nums4)
    print("Output:", findSubsequences(nums4))
    # Expected Output: []

# Time and Space Complexity Analysis
"""
Time Complexity:
- The number of subsequences is bounded by 2^n (where n is the length of nums), as each element can either be included or excluded.
- For each subsequence, we perform a check to ensure non-decreasing order, which takes O(n) in the worst case.
- Thus, the overall time complexity is O(n * 2^n).

Space Complexity:
- The recursion stack can go as deep as O(n) in the worst case.
- Additionally, we use a set to store unique subsequences, which can contain up to 2^n subsequences, each of length O(n).
- Therefore, the space complexity is O(n * 2^n).
"""

# Topic: Backtracking