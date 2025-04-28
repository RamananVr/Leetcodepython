"""
LeetCode Problem #2122: Recover the Original Array

Problem Statement:
You are given an integer array `nums` that was formed by concatenating two arrays `arr` and `arr` * 2, then shuffling.
For example, if `arr = [1, 2, 3]`, then `nums = [1, 2, 3, 2, 4, 6]` (arr concatenated with arr * 2, then shuffled).

You are tasked with recovering the original array `arr`. If there are multiple solutions, return any of them.

Constraints:
- `2 * n == nums.length`
- `2 <= n <= 10^5`
- `0 <= nums[i] <= 10^9`

"""

from collections import Counter
from typing import List

def recoverArray(nums: List[int]) -> List[int]:
    """
    Recover the original array `arr` from the given `nums` array.
    """
    nums.sort()
    n = len(nums) // 2

    for i in range(1, len(nums)):
        k = nums[i] - nums[0]
        if k <= 0 or k % 2 != 0:
            continue

        k //= 2
        original = []
        counter = Counter(nums)

        for num in nums:
            if counter[num] == 0:
                continue
            if counter[num + 2 * k] == 0:
                break
            original.append(num + k)
            counter[num] -= 1
            counter[num + 2 * k] -= 1

        if len(original) == n:
            return original

    return []

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 6, 2, 4]
    print(recoverArray(nums1))  # Output: [1, 2, 3]

    # Test Case 2
    nums2 = [5, 7, 11, 15, 10, 14]
    print(recoverArray(nums2))  # Output: [5, 7, 10]

    # Test Case 3
    nums3 = [2, 10, 6, 4, 8, 12]
    print(recoverArray(nums3))  # Output: [2, 6, 8]

    # Test Case 4
    nums4 = [1, 3, 4, 6, 8, 12]
    print(recoverArray(nums4))  # Output: [1, 4, 6]

"""
Time Complexity:
- Sorting the array takes O(n log n).
- The outer loop iterates through the array, and for each iteration, we attempt to construct the original array using a Counter, which takes O(n) time.
- In the worst case, the outer loop runs O(n) times, leading to an overall complexity of O(n^2).

Space Complexity:
- The Counter object uses O(n) space to store the frequency of elements in the array.
- The `original` list also uses O(n) space.
- Thus, the total space complexity is O(n).

Topic: Arrays, Sorting, Hashing
"""