"""
LeetCode Question #2670: Find the Distinct Difference Array

Problem Statement:
You are given a 0-indexed array nums of length n.

The distinct difference array of nums is an array diff of length n such that diff[i] is equal to the number of distinct elements in the suffix nums[i+1..n-1] subtracted from the number of distinct elements in the prefix nums[0..i].

Formally, diff[i] = distinct(nums[0..i]) - distinct(nums[i+1..n-1]).

Return the distinct difference array of nums.

Note that nums[i+1..n-1] is empty when i == n-1. In this case, distinct(nums[i+1..n-1]) = 0.

Examples:
Example 1:
Input: nums = [1,2,3,4,5]
Output: [1,2,3,4,5]
Explanation: For index i = 0, there is 1 element in the prefix and 4 elements in the suffix. So diff[0] = 1 - 4 = -3.
Note that when i = n - 1, the suffix is empty.

Example 2:
Input: nums = [3,2,3,4,2]
Output: [-2,-1,0,2,3]
Explanation: For index i = 0, there is 1 element in the prefix and 3 elements in the suffix. So diff[0] = 1 - 3 = -2.

Constraints:
- 1 <= nums.length <= 50
- 1 <= nums[i] <= 50
"""

from typing import List

def distinctDifferenceArray(nums: List[int]) -> List[int]:
    """
    Find the distinct difference array using prefix and suffix distinct counts.
    
    Time: O(n^2)
    Space: O(n)
    """
    n = len(nums)
    diff = []
    
    for i in range(n):
        # Count distinct elements in prefix [0..i]
        prefix_distinct = len(set(nums[:i+1]))
        
        # Count distinct elements in suffix [i+1..n-1]
        suffix_distinct = len(set(nums[i+1:])) if i < n - 1 else 0
        
        # Calculate difference
        diff.append(prefix_distinct - suffix_distinct)
    
    return diff

def distinctDifferenceArrayOptimized(nums: List[int]) -> List[int]:
    """
    Optimized approach using precomputed prefix and suffix distinct counts.
    
    Time: O(n^2) worst case, but more efficient in practice
    Space: O(n)
    """
    n = len(nums)
    
    # Precompute prefix distinct counts
    prefix_distinct = [0] * n
    seen = set()
    for i in range(n):
        seen.add(nums[i])
        prefix_distinct[i] = len(seen)
    
    # Precompute suffix distinct counts
    suffix_distinct = [0] * n
    seen = set()
    for i in range(n - 1, -1, -1):
        if i < n - 1:
            seen.add(nums[i + 1])
        suffix_distinct[i] = len(seen)
    
    # Calculate differences
    diff = []
    for i in range(n):
        diff.append(prefix_distinct[i] - suffix_distinct[i])
    
    return diff

def distinctDifferenceArrayBruteForce(nums: List[int]) -> List[int]:
    """
    Brute force approach for clarity.
    
    Time: O(n^3) - for each position, we iterate through prefix and suffix
    Space: O(n)
    """
    n = len(nums)
    diff = []
    
    for i in range(n):
        # Count distinct elements in prefix [0..i]
        prefix_set = set()
        for j in range(i + 1):
            prefix_set.add(nums[j])
        prefix_count = len(prefix_set)
        
        # Count distinct elements in suffix [i+1..n-1]
        suffix_set = set()
        for j in range(i + 1, n):
            suffix_set.add(nums[j])
        suffix_count = len(suffix_set)
        
        diff.append(prefix_count - suffix_count)
    
    return diff

def distinctDifferenceArraySinglePass(nums: List[int]) -> List[int]:
    """
    Single pass approach with more efficient computation.
    
    Time: O(n^2)
    Space: O(n)
    """
    n = len(nums)
    diff = []
    
    # For each position, calculate the difference
    for i in range(n):
        # Use sets to count distinct elements efficiently
        prefix_distinct = len(set(nums[j] for j in range(i + 1)))
        suffix_distinct = len(set(nums[j] for j in range(i + 1, n)))
        
        diff.append(prefix_distinct - suffix_distinct)
    
    return diff

# Test Cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([3, 2, 3, 4, 2], [-2, -1, 0, 2, 3]),
        ([1], [1]),
        ([1, 1, 1], [1, 1, 1]),
        ([1, 2, 1, 2], [1, 0, 1, 2]),
    ]
    
    print("Testing main approach:")
    for nums, expected in test_cases:
        result = distinctDifferenceArray(nums.copy())
        print(f"nums = {nums}")
        print(f"Result: {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()
    
    print("Testing optimized approach:")
    for nums, expected in test_cases:
        result = distinctDifferenceArrayOptimized(nums.copy())
        print(f"nums = {nums}")
        print(f"Result: {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()
    
    print("Testing brute force approach:")
    for nums, expected in test_cases:
        result = distinctDifferenceArrayBruteForce(nums.copy())
        print(f"nums = {nums}")
        print(f"Result: {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()
    
    # Manual verification for example 2
    print("Manual verification for [3,2,3,4,2]:")
    nums = [3, 2, 3, 4, 2]
    for i in range(len(nums)):
        prefix = nums[:i+1]
        suffix = nums[i+1:]
        prefix_distinct = len(set(prefix))
        suffix_distinct = len(set(suffix))
        diff_val = prefix_distinct - suffix_distinct
        print(f"i={i}: prefix={prefix} (distinct={prefix_distinct}), suffix={suffix} (distinct={suffix_distinct}), diff={diff_val}")

"""
Time and Space Complexity Analysis:

Main Approach:
Time Complexity: O(n^2) - for each position, we create sets of size up to n
Space Complexity: O(n) - for the result array and temporary sets

Optimized Approach:
Time Complexity: O(n^2) - two passes through array, each creating sets
Space Complexity: O(n) - for prefix/suffix arrays and temporary sets

Brute Force Approach:
Time Complexity: O(n^3) - for each position, we iterate through elements multiple times
Space Complexity: O(n) - for temporary sets and result

Key Insights:
1. The problem requires counting distinct elements in prefix and suffix
2. Sets are perfect for counting distinct elements efficiently
3. Precomputing prefix/suffix counts can improve readability
4. The key insight is that suffix becomes empty when i = n-1

Topic: Arrays, Hash Set, Prefix Sum, Suffix Array
"""
