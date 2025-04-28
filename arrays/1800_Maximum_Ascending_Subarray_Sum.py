"""
LeetCode Problem #1800: Maximum Ascending Subarray Sum

Problem Statement:
Given an array of positive integers `nums`, return the maximum possible sum of an ascending subarray in `nums`.

A subarray is defined as a contiguous sequence of numbers in an array. An ascending subarray is defined as a subarray where each element is strictly greater than the preceding one.

Example:
Input: nums = [10, 20, 30, 5, 10, 50]
Output: 65
Explanation: [10, 20, 30] is the ascending subarray with the maximum sum.

Input: nums = [10, 20, 30, 40, 50]
Output: 150
Explanation: The entire array is an ascending subarray.

Input: nums = [12, 17, 15, 13, 10, 11, 12]
Output: 33
Explanation: [10, 11, 12] is the ascending subarray with the maximum sum.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 1000
"""

def maxAscendingSum(nums):
    """
    Function to calculate the maximum sum of an ascending subarray.

    :param nums: List[int] - List of positive integers
    :return: int - Maximum sum of an ascending subarray
    """
    max_sum = 0
    current_sum = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:  # Check if the current number is greater than the previous one
            current_sum += nums[i]
        else:
            max_sum = max(max_sum, current_sum)  # Update max_sum if needed
            current_sum = nums[i]  # Reset current_sum to the current number

    # Final check for the last subarray
    max_sum = max(max_sum, current_sum)

    return max_sum


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [10, 20, 30, 5, 10, 50]
    print(maxAscendingSum(nums1))  # Output: 65

    # Test Case 2
    nums2 = [10, 20, 30, 40, 50]
    print(maxAscendingSum(nums2))  # Output: 150

    # Test Case 3
    nums3 = [12, 17, 15, 13, 10, 11, 12]
    print(maxAscendingSum(nums3))  # Output: 33

    # Test Case 4
    nums4 = [100]
    print(maxAscendingSum(nums4))  # Output: 100

    # Test Case 5
    nums5 = [10, 5, 4, 3, 2, 1]
    print(maxAscendingSum(nums5))  # Output: 10


"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The function uses a constant amount of extra space for variables `max_sum` and `current_sum`.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""