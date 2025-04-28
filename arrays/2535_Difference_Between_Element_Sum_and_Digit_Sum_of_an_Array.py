"""
LeetCode Problem #2535: Difference Between Element Sum and Digit Sum of an Array

Problem Statement:
You are given a positive integer array `nums`.

- The element sum is the sum of all the elements in `nums`.
- The digit sum is the sum of all the digits (not necessarily distinct) that appear in the elements of `nums`.

Return the absolute difference between the element sum and the digit sum of the array.

Example:
Input: nums = [123, 4, 56]
Output: 117
Explanation:
Element sum = 123 + 4 + 56 = 183
Digit sum = 1 + 2 + 3 + 4 + 5 + 6 = 21
Absolute difference = |183 - 21| = 117

Constraints:
- 1 <= nums.length <= 2000
- 1 <= nums[i] <= 2000
"""

# Python Solution
def differenceOfSum(nums):
    """
    Calculate the absolute difference between the element sum and the digit sum of an array.

    :param nums: List[int] - A list of positive integers
    :return: int - The absolute difference between the element sum and the digit sum
    """
    element_sum = sum(nums)
    digit_sum = sum(int(digit) for num in nums for digit in str(num))
    return abs(element_sum - digit_sum)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [123, 4, 56]
    print(differenceOfSum(nums1))  # Output: 117

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    print(differenceOfSum(nums2))  # Output: 0

    # Test Case 3
    nums3 = [10, 20, 30]
    print(differenceOfSum(nums3))  # Output: 60

    # Test Case 4
    nums4 = [999, 1000, 2000]
    print(differenceOfSum(nums4))  # Output: 4994

    # Test Case 5
    nums5 = [1]
    print(differenceOfSum(nums5))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the element sum takes O(n), where n is the length of the array.
- Calculating the digit sum involves iterating through each number and its digits. 
  In the worst case, each number has log10(max(nums[i])) digits, so the digit sum calculation takes O(n * d), 
  where d is the average number of digits per number.
- Overall time complexity: O(n * d).

Space Complexity:
- The space complexity is O(1) since we are only using a few variables to store intermediate results.
- The generator expression for the digit sum does not require additional space proportional to the input size.

Topic: Arrays
"""