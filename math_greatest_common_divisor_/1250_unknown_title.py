"""
LeetCode Problem #1250: Check If It Is a Good Array

Problem Statement:
Given an array nums of positive integers, return true if and only if you can choose a subset of nums such that the greatest common divisor (GCD) of the subset is 1.

Constraints:
- 1 <= nums.length <= 10^4
- 1 <= nums[i] <= 10^9
"""

from math import gcd
from functools import reduce

def isGoodArray(nums):
    """
    Determines if the given array is a 'good array' by checking if the GCD of all elements is 1.

    Args:
    nums (List[int]): A list of positive integers.

    Returns:
    bool: True if the array is a good array, False otherwise.
    """
    # Compute the GCD of all elements in the array
    return reduce(gcd, nums) == 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: GCD of the entire array is 1
    nums1 = [3, 6, 9, 12, 5]
    print(isGoodArray(nums1))  # Expected output: True

    # Test Case 2: GCD of the entire array is not 1
    nums2 = [4, 8, 16]
    print(isGoodArray(nums2))  # Expected output: False

    # Test Case 3: Single element array with value 1
    nums3 = [1]
    print(isGoodArray(nums3))  # Expected output: True

    # Test Case 4: Single element array with value greater than 1
    nums4 = [7]
    print(isGoodArray(nums4))  # Expected output: False

    # Test Case 5: Array with multiple elements where GCD is 1
    nums5 = [10, 15, 35]
    print(isGoodArray(nums5))  # Expected output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The `reduce(gcd, nums)` operation computes the GCD of all elements in the array.
- The GCD computation for two numbers is O(log(min(a, b))), where a and b are the two numbers.
- Since we compute the GCD iteratively for all elements in the array, the overall time complexity is O(n * log(max(nums))), where n is the length of the array and max(nums) is the largest number in the array.

Space Complexity:
- The space complexity is O(1) as we are not using any additional data structures and the GCD computation is done in constant space.

Topic: Math (Greatest Common Divisor)
"""