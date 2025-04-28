"""
LeetCode Question #2444: Count Subarrays With Fixed Bounds

Problem Statement:
You are given an integer array `nums` and two integers `minK` and `maxK`.

A fixed-bound subarray of `nums` is a subarray that satisfies the following conditions:
1. The minimum value in the subarray is equal to `minK`.
2. The maximum value in the subarray is equal to `maxK`.

Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

Constraints:
- 2 <= nums.length <= 10^5
- -10^6 <= nums[i], minK, maxK <= 10^6
"""

def countSubarrays(nums, minK, maxK):
    """
    Count the number of fixed-bound subarrays in the given array.

    :param nums: List[int] - The input array of integers.
    :param minK: int - The minimum bound.
    :param maxK: int - The maximum bound.
    :return: int - The count of fixed-bound subarrays.
    """
    n = len(nums)
    min_pos = max_pos = left_bound = -1
    count = 0

    for i in range(n):
        # If the current element is out of bounds, reset the left bound
        if nums[i] < minK or nums[i] > maxK:
            left_bound = i

        # Update the position of the most recent minK and maxK
        if nums[i] == minK:
            min_pos = i
        if nums[i] == maxK:
            max_pos = i

        # Count subarrays ending at index i
        count += max(0, min(min_pos, max_pos) - left_bound)

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 5, 2, 7, 5]
    minK1 = 1
    maxK1 = 5
    print(countSubarrays(nums1, minK1, maxK1))  # Expected Output: 2

    # Test Case 2
    nums2 = [1, 1, 1, 1]
    minK2 = 1
    maxK2 = 1
    print(countSubarrays(nums2, minK2, maxK2))  # Expected Output: 10

    # Test Case 3
    nums3 = [2, 4, 2, 4, 2]
    minK3 = 2
    maxK3 = 4
    print(countSubarrays(nums3, minK3, maxK3))  # Expected Output: 7

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    minK4 = 2
    maxK4 = 4
    print(countSubarrays(nums4, minK4, maxK4))  # Expected Output: 3

"""
Time Complexity Analysis:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space for variables (min_pos, max_pos, left_bound, count).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""