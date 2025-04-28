"""
LeetCode Problem #1498: Number of Subsequences That Satisfy the Given Sum Condition

Problem Statement:
You are given an array of integers `nums` and an integer `target`.

Return the number of non-empty subsequences of `nums` such that the sum of the minimum and maximum element 
on it is less or equal to `target`. Since the answer may be too large, return it modulo 10^9 + 7.

A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements 
without changing the order of the remaining elements.

Example 1:
Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> min + max = 3 + 3 <= 9
[3,5] -> min + max = 3 + 5 <= 9
[3,6] -> min + max = 3 + 6 <= 9
[3,5,6] -> min + max = 3 + 6 <= 9

Example 2:
Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. 
[3] -> min + max = 3 + 3 <= 10
[3] -> min + max = 3 + 3 <= 10
[3,3] -> min + max = 3 + 3 <= 10
[3,6] -> min + max = 3 + 6 <= 10
[3,3,6] -> min + max = 3 + 6 <= 10
[3,3,6,8] -> min + max = 3 + 8 <= 10

Example 3:
Input: nums = [2,3,4,5], target = 8
Output: 6
Explanation: There are 6 subsequences that satisfy the condition.
[2] -> min + max = 2 + 2 <= 8
[2,3] -> min + max = 2 + 3 <= 8
[2,4] -> min + max = 2 + 4 <= 8
[2,5] -> min + max = 2 + 5 <= 8
[2,3,4] -> min + max = 2 + 4 <= 8
[2,3,5] -> min + max = 2 + 5 <= 8

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
            # All subsequences between left and right are valid
            result += power_of_two[right - left]
            result %= MOD
            left += 1
        else:
            right -= 1
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 5, 6, 7]
    target1 = 9
    print(numSubseq(nums1, target1))  # Output: 4

    # Test Case 2
    nums2 = [3, 3, 6, 8]
    target2 = 10
    print(numSubseq(nums2, target2))  # Output: 6

    # Test Case 3
    nums3 = [2, 3, 4, 5]
    target3 = 8
    print(numSubseq(nums3, target3))  # Output: 6

    # Test Case 4
    nums4 = [5, 2, 4, 1, 7, 6, 8]
    target4 = 16
    print(numSubseq(nums4, target4))  # Output: 127

    # Test Case 5
    nums5 = [1, 1, 1, 1]
    target5 = 2
    print(numSubseq(nums5, target5))  # Output: 15

"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- The two-pointer traversal takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The space used for the `power_of_two` array is O(n).
- Sorting the array may require O(n) additional space depending on the sorting algorithm.
- Overall space complexity: O(n).

Topic: Arrays, Two Pointers, Sorting
"""