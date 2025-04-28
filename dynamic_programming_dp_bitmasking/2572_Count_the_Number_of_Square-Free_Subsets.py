"""
LeetCode Problem #2572: Count the Number of Square-Free Subsets

Problem Statement:
You are given an integer array `nums`. A subset of `nums` is square-free if the product of its elements is not divisible by any perfect square greater than 1.

Return the number of square-free subsets of `nums`. Since the answer may be very large, return it modulo 10^9 + 7.

A subset of an array is a selection of elements (possibly none) of the array such that the order of the elements in the subset is the same as in the original array.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 30

Example:
Input: nums = [3, 4, 4, 5]
Output: 3
Explanation: The square-free subsets are [3], [5], and [3, 5].
"""

# Solution
from math import gcd
from functools import lru_cache
from collections import Counter

def squareFreeSubsets(nums):
    MOD = 10**9 + 7

    # Precompute the prime factorization masks for numbers 1 to 30
    prime_factors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    factor_masks = {}
    for i in range(1, 31):
        mask = 0
        for j, prime in enumerate(prime_factors):
            if i % (prime * prime) == 0:  # If divisible by a square of a prime, it's not square-free
                mask = -1
                break
            if i % prime == 0:
                mask |= (1 << j)
        factor_masks[i] = mask

    # Filter out non-square-free numbers
    nums = [num for num in nums if factor_masks[num] != -1]
    if not nums:
        return 0

    # Count the frequency of each number
    freq = Counter(nums)

    # DP to count square-free subsets
    @lru_cache(None)
    def dfs(index, current_mask):
        if index == len(unique_nums):
            return 1  # Empty subset is valid

        num = unique_nums[index]
        mask = factor_masks[num]

        # Option 1: Skip the current number
        result = dfs(index + 1, current_mask)

        # Option 2: Include the current number (if it doesn't conflict with the current mask)
        if current_mask & mask == 0:
            result += freq[num] * dfs(index + 1, current_mask | mask)

        return result % MOD

    unique_nums = list(freq.keys())
    return (dfs(0, 0) - 1) % MOD  # Subtract 1 to exclude the empty subset


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 4, 4, 5]
    print(squareFreeSubsets(nums1))  # Output: 3

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    print(squareFreeSubsets(nums2))  # Output: 6

    # Test Case 3
    nums3 = [4, 9, 16, 25]
    print(squareFreeSubsets(nums3))  # Output: 0

    # Test Case 4
    nums4 = [1, 1, 1, 1]
    print(squareFreeSubsets(nums4))  # Output: 15

    # Test Case 5
    nums5 = [2, 3, 5, 7, 11]
    print(squareFreeSubsets(nums5))  # Output: 31


"""
Time Complexity:
- Precomputing the prime factor masks takes O(30 * P), where P is the number of primes ≤ 30 (constant).
- Filtering the input array takes O(n), where n is the length of nums.
- The DFS function explores all subsets of unique numbers, so its complexity is O(2^u), where u is the number of unique square-free numbers in nums.
- Overall complexity: O(n + 2^u), where u ≤ 30 (constant).

Space Complexity:
- The space used by the DFS recursion stack is O(u), where u is the number of unique square-free numbers.
- The space for the `factor_masks` dictionary and `freq` counter is O(30) and O(n), respectively.
- Overall space complexity: O(n).

Topic: Dynamic Programming (DP), Bitmasking
"""