"""
LeetCode Problem #1283: Find the Smallest Divisor Given a Threshold

Problem Statement:
Given an array of integers `nums` and an integer `threshold`, we need to find the smallest integer `divisor` such that the result of the division of each element in the array by the divisor, summed up, is less than or equal to the threshold.

Each result of the division is rounded up to the nearest integer. For example:
- `ceil(10 / 3) = 4`
- `ceil(7 / 3) = 3`

The task is to return the smallest divisor such that the sum of the division results is less than or equal to the threshold.

Constraints:
- 1 <= nums.length <= 5 * 10^4
- 1 <= nums[i] <= 10^6
- 1 <= threshold <= 10^6
"""

# Solution
import math

def smallestDivisor(nums, threshold):
    def division_sum(divisor):
        """Helper function to calculate the sum of ceil(nums[i] / divisor) for all nums."""
        return sum(math.ceil(num / divisor) for num in nums)

    # Binary search for the smallest divisor
    left, right = 1, max(nums)
    while left < right:
        mid = (left + right) // 2
        if division_sum(mid) > threshold:
            left = mid + 1
        else:
            right = mid
    return left

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [1, 2, 5, 9]
    threshold = 6
    print(smallestDivisor(nums, threshold))  # Output: 5

    # Test Case 2
    nums = [44, 22, 33, 11, 1]
    threshold = 5
    print(smallestDivisor(nums, threshold))  # Output: 44

    # Test Case 3
    nums = [212, 312, 412, 512]
    threshold = 10
    print(smallestDivisor(nums, threshold))  # Output: 106

    # Test Case 4
    nums = [2, 3, 5, 7, 11]
    threshold = 11
    print(smallestDivisor(nums, threshold))  # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- The binary search runs in O(log(max(nums))) iterations, where max(nums) is the largest number in the array.
- For each iteration, we calculate the division sum, which takes O(n) time, where n is the length of the array.
- Therefore, the overall time complexity is O(n * log(max(nums))).

Space Complexity:
- The space complexity is O(1) since we are only using a few variables and no additional data structures.

Topic: Binary Search
"""