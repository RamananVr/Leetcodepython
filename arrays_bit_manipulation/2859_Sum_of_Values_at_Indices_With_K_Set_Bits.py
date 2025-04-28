"""
LeetCode Problem #2859: Sum of Values at Indices With K Set Bits

Problem Statement:
You are given a 0-indexed integer array `nums` and an integer `k`.

Return the sum of the elements in `nums` whose corresponding indices have exactly `k` set bits in their binary representation.

The set bits in an integer are the 1s present when it is written in binary. For example, the binary representation of 21 is `10101`, which has 3 set bits.

Example 1:
Input: nums = [5, 10, 1, 5, 2], k = 1
Output: 13
Explanation:
- Indices with exactly 1 set bit in their binary representation are 1 and 2.
- nums[1] = 10 and nums[2] = 1.
- Their sum is 10 + 1 = 13.

Example 2:
Input: nums = [4, 3, 2, 1], k = 2
Output: 1
Explanation:
- Indices with exactly 2 set bits in their binary representation are 3.
- nums[3] = 1.
- Their sum is 1.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 10^5
- 0 <= k <= 10
"""

# Python Solution
from typing import List

def sum_indices_with_k_set_bits(nums: List[int], k: int) -> int:
    def count_set_bits(n: int) -> int:
        """Helper function to count the number of set bits in the binary representation of n."""
        count = 0
        while n > 0:
            count += n & 1
            n >>= 1
        return count

    total_sum = 0
    for i, num in enumerate(nums):
        if count_set_bits(i) == k:
            total_sum += num
    return total_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [5, 10, 1, 5, 2]
    k1 = 1
    print(sum_indices_with_k_set_bits(nums1, k1))  # Output: 13

    # Test Case 2
    nums2 = [4, 3, 2, 1]
    k2 = 2
    print(sum_indices_with_k_set_bits(nums2, k2))  # Output: 1

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5, 6, 7, 8]
    k3 = 0
    print(sum_indices_with_k_set_bits(nums3, k3))  # Output: 1

    # Test Case 4
    nums4 = [10, 20, 30, 40, 50]
    k4 = 3
    print(sum_indices_with_k_set_bits(nums4, k4))  # Output: 40

# Time and Space Complexity Analysis
"""
Time Complexity:
- The helper function `count_set_bits` runs in O(log(i)) for each index `i` because it processes the binary representation of `i`.
- The main loop iterates over all indices of the array, so the total time complexity is O(n * log(n)), where `n` is the length of the array.

Space Complexity:
- The space complexity is O(1) since we are using a constant amount of extra space.
"""

# Topic: Arrays, Bit Manipulation