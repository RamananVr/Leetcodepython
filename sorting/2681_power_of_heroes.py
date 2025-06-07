"""
LeetCode Question #2681: Power of Heroes

Problem Statement:
You are given a 0-indexed integer array nums representing the strength of some heroes. The power of a group of heroes is defined as follows:

Let i0, i1, ..., ik be the indices of a group of heroes in a nums array. Then the power of this group is max(nums[i0], nums[i1], ..., nums[ik]) * min(nums[i0], nums[i1], ..., nums[ik]) * (number of heroes in the group).

Return the sum of the power of all possible non-empty groups of heroes possible. Since the sum could be very large, return it modulo 10^9 + 7.

Examples:
Example 1:
Input: nums = [2,1,4]
Output: 141
Explanation: 
1st group: [2] has power = 2 * 2 * 1 = 4.
2nd group: [1] has power = 1 * 1 * 1 = 1.
3rd group: [4] has power = 4 * 4 * 1 = 16.
4th group: [2,1] has power = max(2,1) * min(2,1) * 2 = 2 * 1 * 2 = 4.
5th group: [2,4] has power = max(2,4) * min(2,4) * 2 = 4 * 2 * 2 = 16.
6th group: [1,4] has power = max(1,4) * min(1,4) * 2 = 4 * 1 * 2 = 8.
7th group: [2,1,4] has power = max(2,1,4) * min(2,1,4) * 3 = 4 * 1 * 3 = 12.
The sum of powers of all groups is 4 + 1 + 16 + 4 + 16 + 8 + 12 = 61.

Example 2:
Input: nums = [1,1,1]
Output: 12
Explanation: Each group of size 1 has power = 1 * 1 * 1 = 1.
Each group of size 2 has power = 1 * 1 * 2 = 2.
Each group of size 3 has power = 1 * 1 * 3 = 3.
The sum of powers is 3 * 1 + 3 * 2 + 1 * 3 = 12.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

from typing import List

def sumOfPower(nums: List[int]) -> int:
    """
    Calculate sum of power of all possible non-empty groups.
    
    For a sorted array, when we fix the minimum element at index i,
    we need to count all subarrays that include this minimum.
    """
    MOD = 10**9 + 7
    nums.sort()
    n = len(nums)
    result = 0
    
    # For each element as minimum
    for i in range(n):
        min_val = nums[i]
        
        # For each possible maximum >= min_val
        for j in range(i, n):
            max_val = nums[j]
            
            # Number of ways to choose elements between i and j
            # We must include nums[i] and nums[j]
            # We can choose any subset of elements between them
            if i == j:
                count = 1
            else:
                count = pow(2, j - i - 1, MOD)
            
            power = (max_val * min_val % MOD) * ((j - i + 1) * count % MOD) % MOD
            result = (result + power) % MOD
    
    return result

def sumOfPowerOptimized(nums: List[int]) -> int:
    """
    Optimized approach using mathematical insight.
    
    For sorted array, fix minimum at position i, then for each position j >= i,
    calculate contribution when nums[j] is maximum.
    """
    MOD = 10**9 + 7
    nums.sort()
    n = len(nums)
    result = 0
    
    # Precompute powers of 2
    pow2 = [1] * n
    for i in range(1, n):
        pow2[i] = (pow2[i-1] * 2) % MOD
    
    for i in range(n):
        min_val = nums[i]
        
        for j in range(i, n):
            max_val = nums[j]
            
            # Number of subsets that include both i and j
            # and have min at i and max at j
            if i == j:
                count = 1
                size = 1
            else:
                # We can choose any subset of elements between i and j
                count = pow2[j - i - 1]
                size = j - i + 1
            
            power = (max_val * min_val % MOD) * (size * count % MOD) % MOD
            result = (result + power) % MOD
    
    return result

def sumOfPowerBruteForce(nums: List[int]) -> int:
    """
    Brute force approach - generate all possible subsets.
    Time complexity: O(2^n * n)
    """
    MOD = 10**9 + 7
    n = len(nums)
    result = 0
    
    # Generate all non-empty subsets
    for mask in range(1, 1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        
        if subset:
            min_val = min(subset)
            max_val = max(subset)
            size = len(subset)
            
            power = (max_val * min_val % MOD) * size % MOD
            result = (result + power) % MOD
    
    return result

def sumOfPowerDP(nums: List[int]) -> int:
    """
    Dynamic programming approach with contribution counting.
    """
    MOD = 10**9 + 7
    nums.sort()
    n = len(nums)
    result = 0
    
    # dp[i] = sum of powers where nums[i] is the maximum element
    for i in range(n):
        # When nums[i] is both min and max (single element)
        power = (nums[i] * nums[i] % MOD) * 1 % MOD
        result = (result + power) % MOD
        
        # When nums[i] is max, but not necessarily min
        for j in range(i):
            # nums[j] is minimum, nums[i] is maximum
            # Count valid subsets
            if i == j:
                continue
            
            # All subsets that include both j and i
            # Must include j (min) and i (max)
            # Can include any subset of elements between j and i
            count = pow(2, i - j - 1, MOD)
            size = i - j + 1
            
            power = (nums[i] * nums[j] % MOD) * (size * count % MOD) % MOD
            result = (result + power) % MOD
    
    return result

# Test Cases
if __name__ == "__main__":
    test_cases = [
        ([2, 1, 4], 141),
        ([1, 1, 1], 12),
        ([1], 1),
        ([1, 2], 10),
        ([5, 2, 3, 1], 480)
    ]
    
    print("Testing main approach:")
    for nums, expected in test_cases:
        result = sumOfPower(nums.copy())
        print(f"sumOfPower({nums}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting optimized approach:")
    for nums, expected in test_cases:
        result = sumOfPowerOptimized(nums.copy())
        print(f"sumOfPowerOptimized({nums}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting brute force approach:")
    for nums, expected in test_cases:
        result = sumOfPowerBruteForce(nums.copy())
        print(f"sumOfPowerBruteForce({nums}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting DP approach:")
    for nums, expected in test_cases:
        result = sumOfPowerDP(nums.copy())
        print(f"sumOfPowerDP({nums}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")

"""
Time and Space Complexity Analysis:

Main Approach:
Time Complexity: O(n^2) - nested loops through sorted array
Space Complexity: O(1) - only using constant extra space

Optimized Approach:
Time Complexity: O(n^2) - similar to main but with precomputed powers
Space Complexity: O(n) - for precomputed powers of 2

Brute Force Approach:
Time Complexity: O(2^n * n) - generate all subsets and find min/max
Space Complexity: O(n) - for storing subset

DP Approach:
Time Complexity: O(n^2) - nested loops for each max element
Space Complexity: O(1) - constant extra space

Key Insights:
1. Sort the array to efficiently handle min/max relationships
2. For fixed min and max, count valid subsets using powers of 2
3. Mathematical approach avoids generating all subsets explicitly
4. Modular arithmetic is crucial for large numbers

Topic: Sorting, Combinatorics, Dynamic Programming, Mathematics
"""
