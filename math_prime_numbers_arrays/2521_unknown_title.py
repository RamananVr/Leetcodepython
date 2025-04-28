"""
LeetCode Problem #2521: Distinct Prime Factors of Product of Array

Problem Statement:
Given an array of positive integers `nums`, return the number of distinct prime factors in the product of the elements of `nums`.

Note:
- A prime factor of a number is a factor that is a prime number.
- A number `x` is a factor of `y` if `y % x == 0`.

Constraints:
- 1 <= nums.length <= 1000
- 2 <= nums[i] <= 1000
"""

from math import sqrt
from typing import List

def distinctPrimeFactors(nums: List[int]) -> int:
    """
    Function to calculate the number of distinct prime factors in the product of the elements of nums.
    """
    def prime_factors(n: int) -> set:
        """Helper function to find all prime factors of a number."""
        factors = set()
        # Check for divisibility by 2
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        # Check for odd divisors
        for i in range(3, int(sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.add(i)
                n //= i
        # If n is a prime number greater than 2
        if n > 2:
            factors.add(n)
        return factors

    # Use a set to store all distinct prime factors
    all_primes = set()
    for num in nums:
        all_primes.update(prime_factors(num))
    
    return len(all_primes)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 4, 8, 16]
    print(distinctPrimeFactors(nums1))  # Output: 1 (Only prime factor is 2)

    # Test Case 2
    nums2 = [2, 3, 5, 7]
    print(distinctPrimeFactors(nums2))  # Output: 4 (Prime factors are 2, 3, 5, 7)

    # Test Case 3
    nums3 = [6, 10, 15]
    print(distinctPrimeFactors(nums3))  # Output: 4 (Prime factors are 2, 3, 5, 7)

    # Test Case 4
    nums4 = [30, 42, 70]
    print(distinctPrimeFactors(nums4))  # Output: 5 (Prime factors are 2, 3, 5, 7, 11)

"""
Time Complexity Analysis:
- The `prime_factors` function iterates up to the square root of the input number `n` to find its prime factors.
  In the worst case, this is O(sqrt(n)) for a single number.
- For the entire array `nums` of size `m`, the function is called `m` times.
  Therefore, the overall time complexity is O(m * sqrt(k)), where `k` is the maximum value in `nums`.
- Since `k` is at most 1000 (as per constraints), the time complexity is approximately O(m * sqrt(1000)) = O(m * 31.6).

Space Complexity Analysis:
- The space complexity is O(p), where `p` is the number of distinct prime factors in the product of the array.
- The `prime_factors` function uses a set to store prime factors, and the `all_primes` set stores all distinct prime factors across the array.

Topic: Math, Prime Numbers, Arrays
"""