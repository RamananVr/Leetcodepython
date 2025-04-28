"""
LeetCode Problem #1685: Sum of Absolute Differences in a Sorted Array

Problem Statement:
You are given an integer array `nums` sorted in non-decreasing order.

Build and return an integer array `result` with the same length as `nums` such that `result[i]` is equal to the sum of absolute differences between `nums[i]` and all the other elements in the array.

In other words:
result[i] = |nums[i] - nums[0]| + |nums[i] - nums[1]| + ... + |nums[i] - nums[nums.length - 1]|

Example 1:
Input: nums = [2,3,5]
Output: [4,3,5]
Explanation: 
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5

Example 2:
Input: nums = [1,4,6,8,10]
Output: [24,15,13,15,21]

Constraints:
- 2 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
- nums is sorted in non-decreasing order.
"""

# Python Solution
def getSumAbsoluteDifferences(nums):
    """
    Calculate the sum of absolute differences for each element in the sorted array.

    Args:
    nums (List[int]): A sorted list of integers.

    Returns:
    List[int]: A list of integers representing the sum of absolute differences.
    """
    n = len(nums)
    result = [0] * n
    total_sum = sum(nums)
    prefix_sum = 0

    for i in range(n):
        left_count = i
        right_count = n - i - 1
        result[i] = (nums[i] * left_count - prefix_sum) + (total_sum - prefix_sum - nums[i] * (right_count + 1))
        prefix_sum += nums[i]

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 5]
    print(getSumAbsoluteDifferences(nums1))  # Output: [4, 3, 5]

    # Test Case 2
    nums2 = [1, 4, 6, 8, 10]
    print(getSumAbsoluteDifferences(nums2))  # Output: [24, 15, 13, 15, 21]

    # Test Case 3
    nums3 = [1, 2, 3, 4]
    print(getSumAbsoluteDifferences(nums3))  # Output: [6, 4, 4, 6]

    # Test Case 4
    nums4 = [1, 1, 1, 1]
    print(getSumAbsoluteDifferences(nums4))  # Output: [0, 0, 0, 0]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Calculating the total sum of the array is O(n).
- Overall time complexity: O(n).

Space Complexity:
- The algorithm uses O(1) additional space for variables like `prefix_sum` and `total_sum`.
- The result array takes O(n) space.
- Overall space complexity: O(n).
"""

# Topic: Arrays