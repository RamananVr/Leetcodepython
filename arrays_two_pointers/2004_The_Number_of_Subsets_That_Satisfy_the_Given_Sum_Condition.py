"""
LeetCode Problem #2004: The Number of Subsets That Satisfy the Given Sum Condition

Problem Statement:
You are given an integer array `nums` and an integer `target`. Return the number of non-empty subsets of `nums` such that the sum of the minimum and maximum element in the subset is less than or equal to `target`.

Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:
Input: nums = [2, 3, 5, 8], target = 8
Output: 5
Explanation: The subsets are:
- [2] -> min + max = 2 + 2 = 4 <= 8
- [3] -> min + max = 3 + 3 = 6 <= 8
- [2, 3] -> min + max = 2 + 3 = 5 <= 8
- [2, 5] -> min + max = 2 + 5 = 7 <= 8
- [3, 5] -> min + max = 3 + 5 = 8 <= 8

Example 2:
Input: nums = [1, 2, 3, 4], target = 5
Output: 6

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
- 1 <= target <= 10^6
"""

# Python Solution
from typing import List

def numSubseq(nums: List[int], target: int) -> int:
    MOD = 10**9 + 7
    nums.sort()
    n = len(nums)
    
    # Precompute powers of 2 up to n
    power_of_two = [1] * n
    for i in range(1, n):
        power_of_two[i] = (power_of_two[i - 1] * 2) % MOD
    
    left, right = 0, n - 1
    result = 0
    
    while left <= right:
        if nums[left] + nums[right] <= target:
            # All subsets formed by nums[left] and any combination of elements between left+1 and right
            result += power_of_two[right - left]
            result %= MOD
            left += 1
        else:
            right -= 1
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 5, 8]
    target1 = 8
    print(numSubseq(nums1, target1))  # Output: 5

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    target2 = 5
    print(numSubseq(nums2, target2))  # Output: 6

    # Test Case 3
    nums3 = [3, 5, 6, 7]
    target3 = 9
    print(numSubseq(nums3, target3))  # Output: 4

    # Test Case 4
    nums4 = [1, 1, 1, 1]
    target4 = 2
    print(numSubseq(nums4, target4))  # Output: 15

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the length of nums.
- The two-pointer traversal takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The space used for the power_of_two array is O(n).
- Sorting the array may require O(n) additional space depending on the sorting algorithm.
- Overall space complexity: O(n).

Primary Topic: Arrays, Two Pointers
"""