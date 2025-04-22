"""
LeetCode Question #53: Maximum Subarray

Problem Statement:
Given an integer array `nums`, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum = 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum = 23.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

Follow-up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

# Clean, Correct Python Solution
def maxSubArray(nums):
    """
    Finds the maximum sum of a contiguous subarray in the given array.

    :param nums: List[int] - The input array of integers.
    :return: int - The maximum sum of a contiguous subarray.
    """
    # Initialize variables to track the current sum and maximum sum
    current_sum = 0
    max_sum = float('-inf')  # Start with the smallest possible value
    
    for num in nums:
        # Update the current sum, either by adding the current number or starting fresh
        current_sum = max(num, current_sum + num)
        # Update the maximum sum if the current sum is greater
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(nums1))  # Output: 6

    # Test Case 2
    nums2 = [1]
    print(maxSubArray(nums2))  # Output: 1

    # Test Case 3
    nums3 = [5, 4, -1, 7, 8]
    print(maxSubArray(nums3))  # Output: 23

    # Test Case 4
    nums4 = [-1, -2, -3, -4]
    print(maxSubArray(nums4))  # Output: -1

    # Test Case 5
    nums5 = [1, 2, 3, 4, 5]
    print(maxSubArray(nums5))  # Output: 15

# Time and Space Complexity Analysis
"""
Time Complexity:
The algorithm iterates through the array once, performing constant-time operations for each element.
Thus, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
The algorithm uses a constant amount of extra space for variables `current_sum` and `max_sum`.
Thus, the space complexity is O(1).
"""

# Topic: Dynamic Programming (Kadane's Algorithm)