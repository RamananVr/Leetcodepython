"""
LeetCode Problem #2709: Greatest Common Divisor Traversal

Problem Statement:
You are given a 0-indexed integer array `nums`, and you are allowed to traverse between its indices. You can traverse between index `i` and index `j`, `i != j`, if and only if `gcd(nums[i], nums[j]) > 1`.

Determine if it is possible to traverse between all pairs of indices.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

import math
from collections import defaultdict

def canTraverseAllPairs(nums):
    """
    Determines if all pairs of indices can be traversed using Union-Find.
    
    :param nums: List[int] - Array of integers
    :return: bool - True if all pairs can be traversed
    """
    if len(nums) == 1:
        return True
    
    # If any number is 1, it can't connect to others (gcd with 1 is always 1)
    if 1 in nums:
        return False
    
    n = len(nums)
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
    
    # Group indices by their prime factors
    factor_to_indices = defaultdict(list)
    
    for i, num in enumerate(nums):
        # Find all prime factors of num
        temp = num
        d = 2
        while d * d <= temp:
            if temp % d == 0:
                factor_to_indices[d].append(i)
                while temp % d == 0:
                    temp //= d
            d += 1
        if temp > 1:
            factor_to_indices[temp].append(i)
    
    # Union indices that share common prime factors
    for indices in factor_to_indices.values():
        for i in range(1, len(indices)):
            union(indices[0], indices[i])
    
    # Check if all indices are in the same connected component
    root = find(0)
    return all(find(i) == root for i in range(n))

def canTraverseAllPairsOptimized(nums):
    """
    Optimized solution with better prime factorization.
    
    :param nums: List[int] - Array of integers
    :return: bool - True if all pairs can be traversed
    """
    if len(nums) == 1:
        return True
    
    if 1 in nums:
        return False
    
    n = len(nums)
    parent = list(range(n))
    rank = [0] * n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
    
    def get_prime_factors(num):
        factors = set()
        d = 2
        while d * d <= num:
            if num % d == 0:
                factors.add(d)
                while num % d == 0:
                    num //= d
            d += 1
        if num > 1:
            factors.add(num)
        return factors
    
    # Map prime factors to first index that has them
    factor_to_first_index = {}
    
    for i, num in enumerate(nums):
        factors = get_prime_factors(num)
        for factor in factors:
            if factor in factor_to_first_index:
                union(i, factor_to_first_index[factor])
            else:
                factor_to_first_index[factor] = i
    
    # Check if all indices are connected
    root = find(0)
    return all(find(i) == root for i in range(n))

def canTraverseAllPairsBruteForce(nums):
    """
    Brute force solution for small inputs - checks all pairs directly.
    
    :param nums: List[int] - Array of integers
    :return: bool - True if all pairs can be traversed
    """
    if len(nums) == 1:
        return True
    
    n = len(nums)
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
    
    # Check all pairs and union if gcd > 1
    for i in range(n):
        for j in range(i + 1, n):
            if math.gcd(nums[i], nums[j]) > 1:
                union(i, j)
    
    # Check if all indices are in the same connected component
    root = find(0)
    return all(find(i) == root for i in range(n))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [2, 3, 6]
    print(f"nums: {nums}")
    print(f"canTraverseAllPairs: {canTraverseAllPairs(nums)}")  # Output: True
    print(f"canTraverseAllPairsOptimized: {canTraverseAllPairsOptimized(nums)}")  # Output: True
    print(f"canTraverseAllPairsBruteForce: {canTraverseAllPairsBruteForce(nums)}")  # Output: True
    print()

    # Test Case 2
    nums = [3, 9, 5]
    print(f"nums: {nums}")
    print(f"canTraverseAllPairs: {canTraverseAllPairs(nums)}")  # Output: False
    print(f"canTraverseAllPairsOptimized: {canTraverseAllPairsOptimized(nums)}")  # Output: False
    print(f"canTraverseAllPairsBruteForce: {canTraverseAllPairsBruteForce(nums)}")  # Output: False
    print()

    # Test Case 3
    nums = [4, 3, 12, 8]
    print(f"nums: {nums}")
    print(f"canTraverseAllPairs: {canTraverseAllPairs(nums)}")  # Output: True
    print(f"canTraverseAllPairsOptimized: {canTraverseAllPairsOptimized(nums)}")  # Output: True
    print(f"canTraverseAllPairsBruteForce: {canTraverseAllPairsBruteForce(nums)}")  # Output: True
    print()

    # Test Case 4
    nums = [1, 2, 3]
    print(f"nums: {nums}")
    print(f"canTraverseAllPairs: {canTraverseAllPairs(nums)}")  # Output: False
    print(f"canTraverseAllPairsOptimized: {canTraverseAllPairsOptimized(nums)}")  # Output: False
    print()

    # Test Case 5
    nums = [7]
    print(f"nums: {nums}")
    print(f"canTraverseAllPairs: {canTraverseAllPairs(nums)}")  # Output: True
    print(f"canTraverseAllPairsOptimized: {canTraverseAllPairsOptimized(nums)}")  # Output: True

    # Validation
    assert canTraverseAllPairs([2, 3, 6]) == True
    assert canTraverseAllPairsOptimized([3, 9, 5]) == False
    assert canTraverseAllPairsBruteForce([4, 3, 12, 8]) == True
    print("All test cases passed!")

"""
Time Complexity Analysis:
Prime Factorization Approach:
- Time complexity: O(n * sqrt(max(nums)) + n * α(n)) where α is the inverse Ackermann function.

Brute Force:
- Time complexity: O(n^2 * log(max(nums))) for GCD calculations.

Space Complexity Analysis:
- Space complexity: O(n + number_of_unique_prime_factors) for Union-Find and factor mapping.

Topic: Union Find, Number Theory, Prime Factorization, Graph
"""
