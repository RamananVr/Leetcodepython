"""
LeetCode Problem #1085: Sum of Digits in the Minimum Number

Problem Statement:
Given an array `nums` of positive integers, return 1 if the sum of the digits of the minimum number in `nums` is odd, and return 0 otherwise.

Example 1:
Input: nums = [34, 23, 1, 24, 75, 33, 54, 8]
Output: 0
Explanation: The minimum number is 1, and the sum of its digits is 1, which is odd.

Example 2:
Input: nums = [99, 77, 33, 66, 55]
Output: 1
Explanation: The minimum number is 33, and the sum of its digits is 3 + 3 = 6, which is even.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""

# Python Solution
def sumOfDigits(nums):
    """
    Function to determine if the sum of the digits of the minimum number in the array is odd or even.
    
    Args:
    nums (List[int]): List of positive integers.

    Returns:
    int: 1 if the sum of the digits of the minimum number is odd, 0 otherwise.
    """
    # Find the minimum number in the array
    min_num = min(nums)
    
    # Calculate the sum of its digits
    digit_sum = sum(int(digit) for digit in str(min_num))
    
    # Return 1 if the sum is even, otherwise return 0
    return 1 if digit_sum % 2 == 0 else 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [34, 23, 1, 24, 75, 33, 54, 8]
    print(sumOfDigits(nums1))  # Output: 0

    # Test Case 2
    nums2 = [99, 77, 33, 66, 55]
    print(sumOfDigits(nums2))  # Output: 1

    # Test Case 3
    nums3 = [10, 20, 30, 40]
    print(sumOfDigits(nums3))  # Output: 1

    # Test Case 4
    nums4 = [5]
    print(sumOfDigits(nums4))  # Output: 0

    # Test Case 5
    nums5 = [12, 34, 56, 78, 90]
    print(sumOfDigits(nums5))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Finding the minimum number in the array takes O(n), where n is the length of the array.
- Calculating the sum of the digits of the minimum number takes O(d), where d is the number of digits in the minimum number.
- Overall, the time complexity is O(n + d). Since d is a small constant (at most 3 for numbers <= 100), the time complexity is effectively O(n).

Space Complexity:
- The space complexity is O(1) as we are using a constant amount of extra space.
"""

# Topic: Arrays