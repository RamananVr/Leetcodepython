"""
LeetCode Problem #2709: Greatest Common Divisor Traversal

Problem Statement:
You are given an array `nums` of positive integers. You can perform the following operation any number of times:

- Pick two indices `i` and `j` (1 <= i, j <= n) such that `gcd(nums[i], nums[j]) > 1`, and merge `nums[i]` and `nums[j]` into one element. 
  The merged element will be the greatest common divisor (GCD) of `nums[i]` and `nums[j]`.

Return `True` if it is possible to merge all the elements of `nums` into a single element, otherwise return `False`.

Constraints:
- 1 <= nums.length <= 10^4
- 1 <= nums[i] <= 10^6
"""

from math import gcd
from collections import defaultdict
from typing import List

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        """
        Determines if all elements in the array can be merged into a single element
        using the GCD operation.
        """
        if len(nums) == 1:
            return True
        if 1 in nums:
            return False

        # Helper function to find prime factors of a number
        def prime_factors(n):
            factors = set()
            d = 2
            while d * d <= n:
                while n % d == 0:
                    factors.add(d)
                    n //= d
                d += 1
            if n > 1:
                factors.add(n)
            return factors

        # Union-Find (Disjoint Set Union) implementation
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        # Map each prime factor to the indices of numbers in nums
        prime_to_indices = defaultdict(list)
        for i, num in enumerate(nums):
            primes = prime_factors(num)
            for prime in primes:
                prime_to_indices[prime].append(i)

        # Initialize Union-Find structure
        for i in range(len(nums)):
            parent[i] = i

        # Union indices that share a common prime factor
        for indices in prime_to_indices.values():
            for i in range(1, len(indices)):
                union(indices[0], indices[i])

        # Check if all elements are in the same connected component
        root = find(0)
        for i in range(1, len(nums)):
            if find(i) != root:
                return False

        return True

# Example Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    nums1 = [6, 10, 15]
    print(sol.canTraverseAllPairs(nums1))  # Output: True

    # Test Case 2
    nums2 = [4, 7, 15]
    print(sol.canTraverseAllPairs(nums2))  # Output: False

    # Test Case 3
    nums3 = [2, 3, 6]
    print(sol.canTraverseAllPairs(nums3))  # Output: True

    # Test Case 4
    nums4 = [1]
    print(sol.canTraverseAllPairs(nums4))  # Output: True

    # Test Case 5
    nums5 = [1, 2]
    print(sol.canTraverseAllPairs(nums5))  # Output: False

"""
Time Complexity:
- Prime factorization: O(n * sqrt(m)), where n is the length of nums and m is the maximum value in nums.
- Union-Find operations: O(n * α(n)), where α(n) is the inverse Ackermann function (very small, nearly constant).
- Overall: O(n * sqrt(m)).

Space Complexity:
- Space for prime factorization and Union-Find: O(n + m), where m is the maximum value in nums.

Topic: Union-Find, Number Theory, Graphs
"""