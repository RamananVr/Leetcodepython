"""
LeetCode Problem #1911: Maximum Alternating Subsequence Sum

Problem Statement:
The alternating subsequence of an array is a subsequence where the elements are alternately picked from odd and even indices. 
Given an array `nums`, find the maximum sum of any alternating subsequence of `nums`.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5

Example:
Input: nums = [4,2,5,3]
Output: 7
Explanation: The alternating subsequence [4,5] has the maximum sum 4 + 5 = 7.

Input: nums = [5,6,7,8]
Output: 8
Explanation: The alternating subsequence [8] has the maximum sum 8.

Input: nums = [6,2,1,2,4,5]
Output: 10
Explanation: The alternating subsequence [6,1,5] has the maximum sum 6 + 1 + 5 = 10.
"""

# Solution
def maxAlternatingSum(nums):
    """
    Function to calculate the maximum alternating subsequence sum.

    :param nums: List[int] - The input array of integers.
    :return: int - The maximum alternating subsequence sum.
    """
    # Initialize variables to track the maximum sum ending at an odd index and even index
    odd_sum = 0
    even_sum = 0

    # Iterate through the array
    for num in nums:
        # Update odd_sum and even_sum based on the current number
        odd_sum = max(odd_sum, even_sum + num)
        even_sum = max(even_sum, odd_sum - num)

    # Return the maximum sum ending at an odd index
    return odd_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 2, 5, 3]
    print(maxAlternatingSum(nums1))  # Output: 7

    # Test Case 2
    nums2 = [5, 6, 7, 8]
    print(maxAlternatingSum(nums2))  # Output: 8

    # Test Case 3
    nums3 = [6, 2, 1, 2, 4, 5]
    print(maxAlternatingSum(nums3))  # Output: 10

    # Test Case 4
    nums4 = [1]
    print(maxAlternatingSum(nums4))  # Output: 1

    # Test Case 5
    nums5 = [10, 20, 30, 40, 50]
    print(maxAlternatingSum(nums5))  # Output: 50

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The algorithm uses a constant amount of extra space to store the variables `odd_sum` and `even_sum`.
- Therefore, the space complexity is O(1).

Topic: Dynamic Programming
"""