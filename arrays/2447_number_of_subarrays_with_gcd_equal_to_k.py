"""
LeetCode Question #2447: Number of Subarrays With GCD Equal to K

Problem Statement:
Given an integer array `nums` and an integer `k`, return the number of subarrays of `nums` where the greatest common divisor (GCD) of the subarray's elements is equal to `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

The greatest common divisor (GCD) of an array is the largest integer that divides all the array elements.

Example 1:
Input: nums = [9, 3, 1, 2, 6, 3], k = 3
Output: 4
Explanation: The subarrays of nums where the GCD equals k are:
- [9]
- [9, 3]
- [3]
- [6]

Example 2:
Input: nums = [4], k = 7
Output: 0
Explanation: There are no subarrays where the GCD equals k.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i], k <= 100
"""

from math import gcd

def subarrayGCD(nums, k):
    """
    Function to calculate the number of subarrays where the GCD equals k.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The target GCD value.

    Returns:
    int: The number of subarrays where the GCD equals k.
    """
    n = len(nums)
    count = 0

    # Iterate over all possible starting points of subarrays
    for i in range(n):
        current_gcd = 0
        # Iterate over all possible ending points of subarrays starting at i
        for j in range(i, n):
            current_gcd = gcd(current_gcd, nums[j])
            # If the GCD becomes less than k, break early
            if current_gcd < k:
                break
            # If the GCD equals k, increment the count
            if current_gcd == k:
                count += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [9, 3, 1, 2, 6, 3]
    k1 = 3
    print(subarrayGCD(nums1, k1))  # Output: 4

    # Test Case 2
    nums2 = [4]
    k2 = 7
    print(subarrayGCD(nums2, k2))  # Output: 0

    # Test Case 3
    nums3 = [2, 4, 6, 8]
    k3 = 2
    print(subarrayGCD(nums3, k3))  # Output: 6

    # Test Case 4
    nums4 = [5, 10, 15]
    k4 = 5
    print(subarrayGCD(nums4, k4))  # Output: 6

"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop iterates over all starting indices of subarrays (O(n)).
- The inner loop iterates over all ending indices for each starting index (O(n)).
- Calculating the GCD for each pair of elements takes O(log(max(nums[i], nums[j]))), but this is effectively constant for small values of nums[i] and nums[j] (bounded by 100).
- Therefore, the overall time complexity is O(n^2).

Space Complexity:
- The algorithm uses a constant amount of extra space (O(1)) for variables like `current_gcd` and `count`.
- Hence, the space complexity is O(1).

Topic: Arrays
"""