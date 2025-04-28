"""
LeetCode Problem #1979: Find Greatest Common Divisor of Array

Problem Statement:
Given an integer array `nums`, return the greatest common divisor (GCD) of the smallest number and largest number in `nums`.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

Example 1:
Input: nums = [2,5,6,9,10]
Output: 2
Explanation: The smallest number in nums is 2, and the largest number is 10. The GCD of 2 and 10 is 2.

Example 2:
Input: nums = [7,5,6,8,3]
Output: 1
Explanation: The smallest number in nums is 3, and the largest number is 8. The GCD of 3 and 8 is 1.

Example 3:
Input: nums = [3,3]
Output: 3
Explanation: The smallest number in nums is 3, and the largest number is 3. The GCD of 3 and 3 is 3.

Constraints:
- 2 <= nums.length <= 1000
- 1 <= nums[i] <= 1000
"""

from math import gcd
from typing import List

def findGCD(nums: List[int]) -> int:
    """
    Finds the greatest common divisor (GCD) of the smallest and largest numbers in the array.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The GCD of the smallest and largest numbers in the array.
    """
    smallest = min(nums)
    largest = max(nums)
    return gcd(smallest, largest)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 5, 6, 9, 10]
    print(findGCD(nums1))  # Output: 2

    # Test Case 2
    nums2 = [7, 5, 6, 8, 3]
    print(findGCD(nums2))  # Output: 1

    # Test Case 3
    nums3 = [3, 3]
    print(findGCD(nums3))  # Output: 3

    # Additional Test Case 4
    nums4 = [12, 15, 18, 21, 24]
    print(findGCD(nums4))  # Output: 3

    # Additional Test Case 5
    nums5 = [100, 200, 300, 400, 500]
    print(findGCD(nums5))  # Output: 100

"""
Time Complexity Analysis:
- Finding the smallest and largest numbers in the array takes O(n), where n is the length of the array.
- Calculating the GCD using the `gcd` function from the `math` module is O(log(min(a, b))), where a and b are the two numbers.
- Overall time complexity: O(n + log(min(a, b))), which simplifies to O(n) for large arrays.

Space Complexity Analysis:
- The space complexity is O(1) since we are using a constant amount of extra space.

Topic: Arrays, Math
"""