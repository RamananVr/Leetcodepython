"""
LeetCode Problem #2470: Number of Subarrays With LCM Equal to K

Problem Statement:
Given an integer array `nums` and an integer `k`, return the number of subarrays of `nums` where the least common multiple (LCM) of the subarray's elements is equal to `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

The LCM of two integers is the smallest positive integer that is divisible by both integers.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i], k <= 1000
"""

from math import gcd
from typing import List

def lcm(a: int, b: int) -> int:
    """Helper function to calculate the least common multiple of two numbers."""
    return a * b // gcd(a, b)

def subarrayLCM(nums: List[int], k: int) -> int:
    """
    Function to count the number of subarrays where the LCM of the subarray's elements equals k.
    """
    n = len(nums)
    count = 0

    for i in range(n):
        current_lcm = 1
        for j in range(i, n):
            current_lcm = lcm(current_lcm, nums[j])
            if current_lcm > k:  # If LCM exceeds k, no need to continue
                break
            if current_lcm == k:
                count += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 6, 2, 7, 1]
    k1 = 6
    print(subarrayLCM(nums1, k1))  # Expected Output: 4

    # Test Case 2
    nums2 = [2, 3, 4, 6]
    k2 = 12
    print(subarrayLCM(nums2, k2))  # Expected Output: 1

    # Test Case 3
    nums3 = [2, 3, 5]
    k3 = 30
    print(subarrayLCM(nums3, k3))  # Expected Output: 1

    # Test Case 4
    nums4 = [1, 2, 3, 4]
    k4 = 1
    print(subarrayLCM(nums4, k4))  # Expected Output: 4

"""
Time Complexity Analysis:
- Outer loop runs `n` times (for each starting index of the subarray).
- Inner loop runs at most `n` times (for each ending index of the subarray).
- Calculating the LCM for two numbers takes O(log(min(a, b))) due to the GCD calculation.
- In the worst case, the time complexity is O(n^2 * log(max(nums[i]))), where `n` is the length of the array.

Space Complexity Analysis:
- The space complexity is O(1) as we are using a constant amount of extra space.

Topic: Arrays, Math
"""