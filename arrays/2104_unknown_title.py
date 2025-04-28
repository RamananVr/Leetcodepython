"""
LeetCode Problem #2104: Sum of Subarray Ranges

Problem Statement:
You are given an integer array `nums`. The range of a subarray of `nums` is the difference between the maximum and minimum element in the subarray.

Return the sum of all subarray ranges of `nums`.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = max - min = 1 - 1 = 0 
[2], range = max - min = 2 - 2 = 0
[3], range = max - min = 3 - 3 = 0
[1,2], range = max - min = 2 - 1 = 1
[2,3], range = max - min = 3 - 2 = 1
[1,2,3], range = max - min = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

Example 2:
Input: nums = [1,3,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = max - min = 1 - 1 = 0
[3], range = max - min = 3 - 3 = 0
[3], range = max - min = 3 - 3 = 0
[1,3], range = max - min = 3 - 1 = 2
[3,3], range = max - min = 3 - 3 = 0
[1,3,3], range = max - min = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.

Example 3:
Input: nums = [4,-2,-3,4,1]
Output: 59

Constraints:
- 1 <= nums.length <= 1000
- -10^9 <= nums[i] <= 10^9
"""

# Clean and Correct Python Solution
def subArrayRanges(nums):
    """
    Calculate the sum of all subarray ranges in the given array.

    :param nums: List[int] - The input array
    :return: int - The sum of all subarray ranges
    """
    n = len(nums)
    total_sum = 0

    for i in range(n):
        min_val = float('inf')
        max_val = float('-inf')
        for j in range(i, n):
            min_val = min(min_val, nums[j])
            max_val = max(max_val, nums[j])
            total_sum += max_val - min_val

    return total_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    print(subArrayRanges(nums1))  # Output: 4

    # Test Case 2
    nums2 = [1, 3, 3]
    print(subArrayRanges(nums2))  # Output: 4

    # Test Case 3
    nums3 = [4, -2, -3, 4, 1]
    print(subArrayRanges(nums3))  # Output: 59

    # Test Case 4
    nums4 = [1]
    print(subArrayRanges(nums4))  # Output: 0

    # Test Case 5
    nums5 = [10, 20, 30]
    print(subArrayRanges(nums5))  # Output: 60

"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop runs `n` times, where `n` is the length of the array.
- The inner loop runs up to `n` times for each iteration of the outer loop.
- Therefore, the overall time complexity is O(n^2).

Space Complexity:
- The algorithm uses a constant amount of extra space (for variables like `min_val`, `max_val`, and `total_sum`).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""