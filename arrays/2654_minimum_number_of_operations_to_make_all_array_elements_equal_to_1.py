"""
LeetCode Question #2654: Minimum Number of Operations to Make All Array Elements Equal to 1

Problem Statement:
You are given a 0-indexed integer array nums. In one operation, you can:
- Choose two indices i and j where i != j
- Replace nums[i] with gcd(nums[i], nums[j])

Return the minimum number of operations to make all elements of nums equal to 1. If it is impossible, return -1.

The gcd of two integers is the largest positive integer that divides both integers.

Examples:
Example 1:
Input: nums = [2,6,3,4]
Output: 4
Explanation: We can do the following operations:
- Choose i = 2, j = 3, replace nums[2] = gcd(3, 4) = 1. Now nums = [2,6,1,4].
- Choose i = 0, j = 2, replace nums[0] = gcd(2, 1) = 1. Now nums = [1,6,1,4].
- Choose i = 1, j = 2, replace nums[1] = gcd(6, 1) = 1. Now nums = [1,1,1,4].
- Choose i = 3, j = 2, replace nums[3] = gcd(4, 1) = 1. Now nums = [1,1,1,1].

Example 2:
Input: nums = [2,10,6,14]
Output: -1
Explanation: It can be shown that it is impossible to make all elements equal to 1.

Constraints:
- 2 <= nums.length <= 50
- 1 <= nums[i] <= 10^6
"""

from typing import List
import math
from functools import reduce

def minOperations(nums: List[int]) -> int:
    """
    Find minimum operations to make all elements equal to 1.
    
    Key insights:
    1. If any element is already 1, we can make all others 1 in (n-1) operations
    2. If gcd of all elements > 1, it's impossible
    3. Otherwise, find minimum operations to create a 1, then make all others 1
    """
    n = len(nums)
    
    # Count existing 1s
    ones_count = nums.count(1)
    
    # If we already have 1s, we need (n - ones_count) operations
    if ones_count > 0:
        return n - ones_count
    
    # Check if it's possible (gcd of all elements should be 1)
    overall_gcd = reduce(math.gcd, nums)
    if overall_gcd > 1:
        return -1
    
    # Find minimum operations to create first 1
    min_ops_to_create_one = float('inf')
    
    # Try all possible subsequences to find minimum operations to get gcd = 1
    for i in range(n):
        current_gcd = nums[i]
        for j in range(i + 1, n):
            current_gcd = math.gcd(current_gcd, nums[j])
            if current_gcd == 1:
                # Found a subsequence with gcd = 1
                # Operations needed: (j - i) to create 1, then (n - 1) to make all 1
                operations_to_create = j - i
                min_ops_to_create_one = min(min_ops_to_create_one, operations_to_create)
                break
    
    # Total operations: create one 1 + make remaining (n-1) elements 1
    return min_ops_to_create_one + (n - 1)

def minOperationsOptimized(nums: List[int]) -> int:
    """
    Optimized approach with better handling of edge cases.
    """
    n = len(nums)
    
    # Count existing 1s
    ones_count = nums.count(1)
    if ones_count > 0:
        return n - ones_count
    
    # Check if possible
    overall_gcd = nums[0]
    for i in range(1, n):
        overall_gcd = math.gcd(overall_gcd, nums[i])
    
    if overall_gcd > 1:
        return -1
    
    # Find minimum length subarray with gcd = 1
    min_subarray_length = n
    
    for i in range(n):
        current_gcd = 0
        for j in range(i, n):
            current_gcd = math.gcd(current_gcd, nums[j])
            if current_gcd == 1:
                min_subarray_length = min(min_subarray_length, j - i + 1)
                break
    
    # Operations = (min_subarray_length - 1) to create 1 + (n - 1) to make all 1
    return min_subarray_length - 1 + n - 1

def minOperationsBruteForce(nums: List[int]) -> int:
    """
    Brute force approach for verification.
    """
    n = len(nums)
    
    # Count 1s
    ones = nums.count(1)
    if ones > 0:
        return n - ones
    
    # Check if possible
    g = nums[0]
    for num in nums[1:]:
        g = math.gcd(g, num)
    if g > 1:
        return -1
    
    # Find minimum operations to get first 1
    ans = n
    for i in range(n):
        g = nums[i]
        for j in range(i, n):
            g = math.gcd(g, nums[j])
            if g == 1:
                ans = min(ans, j - i + n - 1)
                break
    
    return ans

# Test Cases
if __name__ == "__main__":
    test_cases = [
        ([2, 6, 3, 4], 4),
        ([2, 10, 6, 14], -1),
        ([1, 2, 3], 2),
        ([1], 0),
        ([1, 1, 1], 0),
        ([2, 4, 8], -1),
        ([6, 10, 15], 3),
        ([2, 3], 1)
    ]
    
    print("Testing main approach:")
    for nums, expected in test_cases:
        result = minOperations(nums.copy())
        print(f"minOperations({nums}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting optimized approach:")
    for nums, expected in test_cases:
        result = minOperationsOptimized(nums.copy())
        print(f"minOperationsOptimized({nums}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting brute force approach:")
    for nums, expected in test_cases:
        result = minOperationsBruteForce(nums.copy())
        print(f"minOperationsBruteForce({nums}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")

"""
Time and Space Complexity Analysis:

Main Approach:
Time Complexity: O(n^2 * log(max(nums))) 
- O(n^2) for checking all subsequences
- O(log(max(nums))) for gcd calculation
Space Complexity: O(1) - only using constant extra space

Optimized Approach:
Time Complexity: O(n^2 * log(max(nums)))
- Similar to main approach but with better constant factors
Space Complexity: O(1) - only using constant extra space

Brute Force Approach:
Time Complexity: O(n^2 * log(max(nums)))
Space Complexity: O(1) - only using constant extra space

Key Insights:
1. If array already contains 1, answer is (n - count_of_ones)
2. If gcd of all elements > 1, impossible (-1)
3. Otherwise, find minimum length subarray with gcd = 1, then propagate

Topic: Arrays, Math, GCD, Greedy
"""
