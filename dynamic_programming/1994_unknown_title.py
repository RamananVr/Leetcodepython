"""
LeetCode Problem #1994: The Number of Good Subsets

Problem Statement:
You are given an integer array nums. A subset of nums is called a good subset if:
- The product of its elements is a positive integer that is divisible by no square number other than 1.

Return the number of different good subsets of nums modulo 10^9 + 7.

A subset of nums is any array that can be obtained by deleting some (possibly none or all) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

Constraints:
- 1 <= nums.length <= 10^4
- 1 <= nums[i] <= 30
"""

from collections import Counter
from functools import lru_cache

def numberOfGoodSubsets(nums):
    MOD = 10**9 + 7
    
    # Prime numbers less than 30
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    
    # Mapping each number to its prime factorization mask
    def get_prime_mask(x):
        mask = 0
        for i, prime in enumerate(primes):
            count = 0
            while x % prime == 0:
                x //= prime
                count += 1
            if count > 1:  # If divisible by a square number, return -1
                return -1
            if count == 1:
                mask |= (1 << i)
        return mask
    
    # Count frequency of each number in nums
    freq = Counter(nums)
    
    # DP array to count subsets with specific prime masks
    dp = [0] * (1 << len(primes))
    dp[0] = 1  # Base case: empty subset
    
    for num, count in freq.items():
        if num == 1:
            continue  # Skip 1 for now
        prime_mask = get_prime_mask(num)
        if prime_mask == -1:
            continue  # Skip numbers divisible by square numbers
        for state in range((1 << len(primes)) - 1, -1, -1):
            if state & prime_mask == 0:  # No overlap in prime factors
                dp[state | prime_mask] = (dp[state | prime_mask] + dp[state] * count) % MOD
    
    # Calculate result excluding subsets containing only 1s
    result = sum(dp[1:]) % MOD
    
    # Include subsets containing 1s
    if freq[1] > 0:
        result = result * pow(2, freq[1], MOD) % MOD
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    print(numberOfGoodSubsets(nums1))  # Expected Output: 6

    # Test Case 2
    nums2 = [4, 4, 4, 4]
    print(numberOfGoodSubsets(nums2))  # Expected Output: 1

    # Test Case 3
    nums3 = [1, 1, 1, 1]
    print(numberOfGoodSubsets(nums3))  # Expected Output: 0

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(numberOfGoodSubsets(nums4))  # Expected Output: 44

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating the prime mask for each number in nums takes O(30 * len(primes)) = O(300) in the worst case.
- The DP update process iterates over all states (2^len(primes)) and all numbers in nums, resulting in O(len(nums) * 2^len(primes)).
- Overall complexity: O(len(nums) * 2^len(primes)) = O(len(nums) * 1024).

Space Complexity:
- The DP array requires O(2^len(primes)) = O(1024) space.
- The frequency counter and other auxiliary variables require O(len(nums)) space.
- Overall space complexity: O(len(nums) + 2^len(primes)).

Topic: Dynamic Programming
"""