"""
LeetCode Problem #2584: Split the Array to Make Coprime Products

Problem Statement:
You are given an integer array nums of length n. You are tasked to split the array into two non-empty subarrays, 
left and right, such that:

- Every element in left is relatively prime (coprime) with every element in right.
- left and right are non-empty.

Return the number of ways to split nums such that the above conditions are satisfied.

Two integers a and b are relatively prime if gcd(a, b) == 1, where gcd is the greatest common divisor.

Constraints:
- 2 <= nums.length <= 10^4
- 1 <= nums[i] <= 10^6
"""

from math import gcd
from functools import reduce

def splitArray(nums):
    """
    Function to count the number of ways to split the array into two subarrays such that
    every element in the left subarray is coprime with every element in the right subarray.
    
    :param nums: List[int] - The input array of integers.
    :return: int - The number of valid splits.
    """
    n = len(nums)
    
    # Compute prefix and suffix gcd arrays
    prefix_gcd = [0] * n
    suffix_gcd = [0] * n
    
    prefix_gcd[0] = nums[0]
    for i in range(1, n):
        prefix_gcd[i] = gcd(prefix_gcd[i - 1], nums[i])
    
    suffix_gcd[n - 1] = nums[n - 1]
    for i in range(n - 2, -1, -1):
        suffix_gcd[i] = gcd(suffix_gcd[i + 1], nums[i])
    
    # Count valid splits
    valid_splits = 0
    for i in range(n - 1):
        if gcd(prefix_gcd[i], suffix_gcd[i + 1]) == 1:
            valid_splits += 1
    
    return valid_splits

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 4, 5]
    print(splitArray(nums1))  # Expected Output: 2
    
    # Test Case 2
    nums2 = [6, 10, 15]
    print(splitArray(nums2))  # Expected Output: 0
    
    # Test Case 3
    nums3 = [7, 11, 13, 17]
    print(splitArray(nums3))  # Expected Output: 3
    
    # Test Case 4
    nums4 = [2, 3]
    print(splitArray(nums4))  # Expected Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Computing prefix_gcd takes O(n) time.
- Computing suffix_gcd takes O(n) time.
- Iterating through the array to count valid splits takes O(n) time.
- Overall time complexity: O(n).

Space Complexity:
- The prefix_gcd and suffix_gcd arrays each take O(n) space.
- Overall space complexity: O(n).

Topic: Arrays, Math (GCD)
"""