"""
LeetCode Problem #2393: Count Strictly Increasing Subarrays

Problem Statement:
You are given an integer array `nums` consisting of `n` integers. A subarray is called strictly increasing if its elements are in strictly increasing order.

Return the number of strictly increasing subarrays in `nums`.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1, 2, 3, 4]
Output: 10
Explanation: There are 10 strictly increasing subarrays:
- [1], [2], [3], [4], [1, 2], [2, 3], [3, 4], [1, 2, 3], [2, 3, 4], [1, 2, 3, 4].

Example 2:
Input: nums = [1, 2, 2, 4]
Output: 4
Explanation: There are 4 strictly increasing subarrays:
- [1], [2], [2], [4], [1, 2], [4].

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

def countIncreasing(nums):
    """
    Function to count the number of strictly increasing subarrays in the given array.

    :param nums: List[int] - The input array of integers.
    :return: int - The number of strictly increasing subarrays.
    """
    n = len(nums)
    count = 0
    length = 1  # Length of the current strictly increasing subarray

    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            length += 1
        else:
            count += (length * (length + 1)) // 2
            length = 1

    # Add the last increasing subarray count
    count += (length * (length + 1)) // 2

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    print(countIncreasing(nums1))  # Output: 10

    # Test Case 2
    nums2 = [1, 2, 2, 4]
    print(countIncreasing(nums2))  # Output: 4

    # Test Case 3
    nums3 = [5, 1, 2, 3, 1, 2]
    print(countIncreasing(nums3))  # Output: 8

    # Test Case 4
    nums4 = [1]
    print(countIncreasing(nums4))  # Output: 1

    # Test Case 5
    nums5 = [1, 3, 5, 4, 6, 7]
    print(countIncreasing(nums5))  # Output: 10

"""
Time Complexity Analysis:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space, regardless of the input size.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""