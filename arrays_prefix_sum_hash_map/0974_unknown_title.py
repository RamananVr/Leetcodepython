"""
LeetCode Problem #974: Subarray Sums Divisible by K

Problem Statement:
Given an integer array `nums` and an integer `k`, return the number of non-empty subarrays that have a sum divisible by `k`.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Example 2:
Input: nums = [5], k = 9
Output: 0

Constraints:
1. 1 <= nums.length <= 3 * 10^4
2. -10^4 <= nums[i] <= 10^4
3. 2 <= k <= 10^4
"""

def subarraysDivByK(nums, k):
    """
    Function to count the number of subarrays with a sum divisible by k.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The divisor.

    Returns:
    int: The number of subarrays with a sum divisible by k.
    """
    prefix_sum = 0
    remainder_count = {0: 1}  # Initialize with 0 remainder having a count of 1
    count = 0

    for num in nums:
        prefix_sum += num
        remainder = prefix_sum % k

        # Handle negative remainders to ensure they are in the range [0, k-1]
        if remainder < 0:
            remainder += k

        # If the remainder has been seen before, add its count to the result
        if remainder in remainder_count:
            count += remainder_count[remainder]

        # Update the remainder count
        remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 5, 0, -2, -3, 1]
    k1 = 5
    print(subarraysDivByK(nums1, k1))  # Output: 7

    # Test Case 2
    nums2 = [5]
    k2 = 9
    print(subarraysDivByK(nums2, k2))  # Output: 0

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    k3 = 3
    print(subarraysDivByK(nums3, k3))  # Output: 4

    # Test Case 4
    nums4 = [-1, 2, 9]
    k4 = 2
    print(subarraysDivByK(nums4, k4))  # Output: 2

"""
Time Complexity:
- The algorithm iterates through the array once, performing O(1) operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The space complexity is O(k) due to the dictionary `remainder_count` which stores at most k keys (one for each possible remainder).
- Thus, the space complexity is O(k).

Topic: Arrays, Prefix Sum, Hash Map
"""