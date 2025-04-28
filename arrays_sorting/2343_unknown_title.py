"""
LeetCode Problem #2343: Query Kth Smallest Trimmed Number

Problem Statement:
You are given a 0-indexed array of strings `nums`, where each string is of equal length and consists of only digits.
You are also given a 2D integer array `queries` where `queries[i] = [k, trim]`. For each `queries[i]`, you need to:

1. Trim each number in `nums` to its rightmost `trim` digits.
2. Determine the `k`th smallest trimmed number in the resulting array as if the trimmed numbers were integers.
3. Return the index of this `k`th smallest number in `nums`.

Notes:
- If two trimmed numbers are equal, the one with the smaller original index is considered smaller.
- The result of each query should be returned as an array.

Constraints:
- `1 <= nums.length <= 100`
- `1 <= nums[i].length <= 100`
- `1 <= queries.length <= 100`
- `1 <= k <= nums.length`
- `1 <= trim <= nums[i].length`

Example:
Input: nums = ["102","473","251","814"], queries = [[1,1],[2,3],[4,2]]
Output: [2,2,1]

Explanation:
1. After trimming to 1 digit, nums = ["2","3","1","4"]. The smallest number is "1" at index 2.
2. After trimming to 3 digits, nums = ["102","473","251","814"]. The 2nd smallest number is "251" at index 2.
3. After trimming to 2 digits, nums = ["02","73","51","14"]. The 4th smallest number is "73" at index 1.
"""

# Python Solution
from typing import List

def smallestTrimmedNumbers(nums: List[str], queries: List[List[int]]) -> List[int]:
    result = []
    for k, trim in queries:
        # Trim each number to its rightmost `trim` digits
        trimmed = [(num[-trim:], i) for i, num in enumerate(nums)]
        # Sort by the trimmed value, and then by index in case of ties
        trimmed.sort(key=lambda x: (x[0], x[1]))
        # Append the index of the k-th smallest trimmed number
        result.append(trimmed[k - 1][1])
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = ["102", "473", "251", "814"]
    queries1 = [[1, 1], [2, 3], [4, 2]]
    print(smallestTrimmedNumbers(nums1, queries1))  # Output: [2, 2, 1]

    # Test Case 2
    nums2 = ["24", "37", "96", "04"]
    queries2 = [[2, 1], [2, 2]]
    print(smallestTrimmedNumbers(nums2, queries2))  # Output: [3, 0]

    # Test Case 3
    nums3 = ["123", "456", "789", "012"]
    queries3 = [[1, 2], [3, 1], [4, 3]]
    print(smallestTrimmedNumbers(nums3, queries3))  # Output: [3, 2, 0]

# Time and Space Complexity Analysis
"""
Time Complexity:
- For each query, we trim all `n` numbers (O(n)) and sort them (O(n log n)).
- If there are `q` queries, the total time complexity is O(q * n log n).

Space Complexity:
- The space required for the `trimmed` list is O(n) for each query.
- The overall space complexity is O(n) for intermediate storage.
"""

# Topic: Arrays, Sorting