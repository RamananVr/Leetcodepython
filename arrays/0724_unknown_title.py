"""
LeetCode Problem #724: Find Pivot Index

Problem Statement:
Given an array of integers `nums`, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the right of the index.

If no such index exists, return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

Example 1:
Input: nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
Input: nums = [1, 2, 3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Example 3:
Input: nums = [2, 1, -1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + (-1) = 0

Constraints:
- 1 <= nums.length <= 10^4
- -1000 <= nums[i] <= 1000
"""

def pivotIndex(nums):
    """
    Finds the pivot index in the given array.

    :param nums: List[int] - The input array of integers.
    :return: int - The pivot index or -1 if no such index exists.
    """
    total_sum = sum(nums)
    left_sum = 0

    for i in range(len(nums)):
        # Check if left sum equals right sum
        if left_sum == total_sum - left_sum - nums[i]:
            return i
        # Update left sum
        left_sum += nums[i]

    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 7, 3, 6, 5, 6]
    print(pivotIndex(nums1))  # Output: 3

    # Test Case 2
    nums2 = [1, 2, 3]
    print(pivotIndex(nums2))  # Output: -1

    # Test Case 3
    nums3 = [2, 1, -1]
    print(pivotIndex(nums3))  # Output: 0

    # Test Case 4
    nums4 = [0, 0, 0, 0, 0]
    print(pivotIndex(nums4))  # Output: 0

    # Test Case 5
    nums5 = [-1, -1, -1, 0, 1, 1]
    print(pivotIndex(nums5))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution iterates through the array once to calculate the total sum (O(n)).
- Then, it iterates through the array again to find the pivot index (O(n)).
- Overall, the time complexity is O(n).

Space Complexity:
- The solution uses a constant amount of extra space (O(1)).
- The variables `total_sum` and `left_sum` are scalars, and no additional data structures are used.

Topic: Arrays
"""