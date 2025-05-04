import math
from typing import List

"""
LeetCode Problem #2908: Minimum Sum of Mountain Triplets I

Problem Statement:
You are given a 0-indexed array `nums` of integers.
A triplet `(i, j, k)` is a **mountain** if:
1. `i < j < k`
2. `nums[i] < nums[j]` and `nums[k] < nums[j]`

Return the **minimum possible sum** of a mountain triplet `nums[i] + nums[j] + nums[k]`. If no such triplet exists, return -1.

Example 1:
Input: nums = [8,6,1,5,3]
Output: 9
Explanation: Triplet (2, 3, 4) with values (1, 5, 3) is a mountain triplet. sum = 1 + 5 + 3 = 9. It's the minimum possible sum.

Example 2:
Input: nums = [5,4,8,7,10,2]
Output: 13
Explanation: Triplet (1, 3, 5) with values (4, 7, 2) is a mountain triplet. sum = 4 + 7 + 2 = 13. It's the minimum possible sum.

Example 3:
Input: nums = [6,5,4,3,4,5]
Output: -1
Explanation: No mountain triplets exist.

Constraints:
- 3 <= nums.length <= 50
- 1 <= nums[i] <= 50
"""

def minimumSum(nums: List[int]) -> int:
    """
    Finds the minimum sum of a mountain triplet (i, j, k) where i < j < k,
    nums[i] < nums[j], and nums[k] < nums[j].

    Args:
        nums: A list of integers.

    Returns:
        The minimum sum of a mountain triplet, or -1 if none exists.
    """
    n = len(nums)
    min_total_sum = float('inf')
    found_mountain = False

    # Iterate through each potential peak j (index 1 to n-2)
    for j in range(1, n - 1):
        min_left = float('inf')
        min_right = float('inf')

        # Find the minimum element to the left of j that is smaller than nums[j]
        for i in range(j):
            if nums[i] < nums[j]:
                min_left = min(min_left, nums[i])

        # Find the minimum element to the right of j that is smaller than nums[j]
        for k in range(j + 1, n):
            if nums[k] < nums[j]:
                min_right = min(min_right, nums[k])

        # If a valid left and right element were found for this peak j
        if min_left != float('inf') and min_right != float('inf'):
            current_sum = min_left + nums[j] + min_right
            min_total_sum = min(min_total_sum, current_sum)
            found_mountain = True

    return min_total_sum if found_mountain else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [8, 6, 1, 5, 3]
    expected1 = 9
    result1 = minimumSum(nums1)
    assert result1 == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {result1}"
    print(f"Test Case 1 (nums={nums1}): Result = {result1}")

    # Test Case 2
    nums2 = [5, 4, 8, 7, 10, 2]
    expected2 = 13 # (4, 7, 2) -> j=3
    result2 = minimumSum(nums2)
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {result2}"
    print(f"Test Case 2 (nums={nums2}): Result = {result2}")

    # Test Case 3
    nums3 = [6, 5, 4, 3, 4, 5]
    expected3 = -1
    result3 = minimumSum(nums3)
    assert result3 == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {result3}"
    print(f"Test Case 3 (nums={nums3}): Result = {result3}")

    # Test Case 4: Only one possible mountain
    nums4 = [1, 10, 2]
    expected4 = 13 # (1, 10, 2) -> j=1
    result4 = minimumSum(nums4)
    assert result4 == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {result4}"
    print(f"Test Case 4 (nums={nums4}): Result = {result4}")

    # Test Case 5: Minimum is not the first found
    nums5 = [50, 40, 30, 20, 25, 10] # (30, 25, 10) -> 65; (20, 25, 10) -> 55
    expected5 = 55 # j=4, nums[j]=25. left_min=20 (idx 3), right_min=10 (idx 5)
    result5 = minimumSum(nums5)
    assert result5 == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {result5}"
    print(f"Test Case 5 (nums={nums5}): Result = {result5}")

    print("\nAll provided test cases passed!")

"""
Time and Space Complexity Analysis:

Time Complexity: O(N^2)
- The outer loop iterates through potential peaks `j` from 1 to n-2 (O(N)).
- Inside the loop, we have two separate inner loops:
    - One iterates from 0 to j-1 (at most O(N)).
    - The other iterates from j+1 to n-1 (at most O(N)).
- The total time complexity is O(N * (N + N)) = O(N^2).
- Given the constraint N <= 50, O(N^2) is acceptable (approx 2500 operations).
- (Note: An O(N) solution exists using prefix/suffix minimums, but O(N^2) is sufficient here).

Space Complexity: O(1)
- We only use a few variables (`min_total_sum`, `found_mountain`, `min_left`, `min_right`, `current_sum`, loop indices) to store intermediate values.
- The space used does not depend on the size of the input array `nums`.

Topic: Array, Brute Force
"""