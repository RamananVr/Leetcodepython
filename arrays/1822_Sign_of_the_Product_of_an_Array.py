"""
LeetCode Problem #1822: Sign of the Product of an Array

Problem Statement:
There is a function `signFunc(x)` that returns:
- 1 if `x` is positive.
- -1 if `x` is negative.
- 0 if `x` is equal to 0.

You are given an integer array `nums`. Let `product` be the product of all values in the array `nums`.
Return `signFunc(product)`.

Example 1:
Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values is 144, and signFunc(144) = 1.

Example 2:
Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values is 0, and signFunc(0) = 0.

Example 3:
Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values is -1, and signFunc(-1) = -1.

Constraints:
- 1 <= nums.length <= 1000
- -100 <= nums[i] <= 100
"""

# Python Solution
def arraySign(nums):
    """
    Determines the sign of the product of an array using the sign function.

    :param nums: List[int] - The input array of integers.
    :return: int - The sign of the product of the array.
    """
    sign = 1
    for num in nums:
        if num == 0:
            return 0
        elif num < 0:
            sign *= -1
    return sign

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [-1, -2, -3, -4, 3, 2, 1]
    print(arraySign(nums1))  # Output: 1

    # Test Case 2
    nums2 = [1, 5, 0, 2, -3]
    print(arraySign(nums2))  # Output: 0

    # Test Case 3
    nums3 = [-1, 1, -1, 1, -1]
    print(arraySign(nums3))  # Output: -1

    # Test Case 4
    nums4 = [1, 2, 3, 4]
    print(arraySign(nums4))  # Output: 1

    # Test Case 5
    nums5 = [-1, -1, -1]
    print(arraySign(nums5))  # Output: -1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the array once, so the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The function uses a constant amount of extra space (the `sign` variable), so the space complexity is O(1).
"""

# Topic: Arrays