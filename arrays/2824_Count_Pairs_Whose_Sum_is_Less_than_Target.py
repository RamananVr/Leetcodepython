"""
LeetCode Problem #2824: Count Pairs Whose Sum is Less than Target

Problem Statement:
Given a 0-indexed integer array `nums` of length `n` and an integer `target`, 
return the number of pairs `(i, j)` where `0 <= i < j < n` and `nums[i] + nums[j] < target`.

Example:
Input: nums = [1, 2, 3, 4, 5], target = 8
Output: 7
Explanation: The pairs are:
- (0, 1): nums[0] + nums[1] = 1 + 2 = 3 < 8
- (0, 2): nums[0] + nums[2] = 1 + 3 = 4 < 8
- (0, 3): nums[0] + nums[3] = 1 + 4 = 5 < 8
- (0, 4): nums[0] + nums[4] = 1 + 5 = 6 < 8
- (1, 2): nums[1] + nums[2] = 2 + 3 = 5 < 8
- (1, 3): nums[1] + nums[3] = 2 + 4 = 6 < 8
- (1, 4): nums[1] + nums[4] = 2 + 5 = 7 < 8

Constraints:
- 2 <= nums.length <= 100
- -1000 <= nums[i] <= 1000
- -1000 <= target <= 1000
"""

def count_pairs(nums, target):
    """
    Counts the number of pairs (i, j) where 0 <= i < j < len(nums) and nums[i] + nums[j] < target.

    :param nums: List[int] - The input array of integers.
    :param target: int - The target sum.
    :return: int - The count of valid pairs.
    """
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] < target:
                count += 1
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5]
    target1 = 8
    print(count_pairs(nums1, target1))  # Output: 7

    # Test Case 2
    nums2 = [-1, 0, 2, 3]
    target2 = 3
    print(count_pairs(nums2, target2))  # Output: 4

    # Test Case 3
    nums3 = [5, 1, 2, 3]
    target3 = 6
    print(count_pairs(nums3, target3))  # Output: 4

    # Test Case 4
    nums4 = [0, 0, 0, 0]
    target4 = 1
    print(count_pairs(nums4, target4))  # Output: 6

    # Test Case 5
    nums5 = [10, 20, 30]
    target5 = 15
    print(count_pairs(nums5, target5))  # Output: 0

"""
Time Complexity:
- The solution uses a nested loop to iterate over all pairs of indices (i, j) where i < j.
- The outer loop runs `n` times, and the inner loop runs approximately `n-1` times on average.
- Therefore, the time complexity is O(n^2), where n is the length of the input array `nums`.

Space Complexity:
- The solution uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""