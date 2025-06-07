# filepath: q:\source\AgentGeneratedLeetcode\arrays\2680_maximum_or.py
"""
LeetCode Question #2680: Maximum OR

Problem Statement:
You are given a 0-indexed integer array nums of length n and an integer k. In one operation, you can choose an element and multiply it by 2.

Return the maximum possible value of nums[0] | nums[1] | ... | nums[n-1] that you can obtain after applying the operation at most k times.

Note that a | b denotes the bitwise OR of two integers a and b.

Examples:
Example 1:
Input: nums = [12,9], k = 1
Output: 30
Explanation: If we apply the operation to index 1, our new array nums becomes [12,18]. The bitwise OR of 12 and 18 is 30.

Example 2:
Input: nums = [8,1,2], k = 2
Output: 35
Explanation: If we apply the operation twice on index 0, the new array becomes [32,1,2]. The bitwise OR of 32, 1, and 2 is 35.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= 15
"""

from typing import List

def maximumOr(nums: List[int], k: int) -> int:
    """
    Find maximum OR value after applying at most k multiply-by-2 operations.
    
    Time: O(n) where n is length of nums
    Space: O(1)
    """
    n = len(nums)
    
    # Precompute prefix and suffix OR values
    prefix_or = [0] * (n + 1)
    suffix_or = [0] * (n + 1)
    
    # Build prefix OR array
    for i in range(n):
        prefix_or[i + 1] = prefix_or[i] | nums[i]
    
    # Build suffix OR array
    for i in range(n - 1, -1, -1):
        suffix_or[i] = suffix_or[i + 1] | nums[i]
    
    max_or = 0
    
    # Try applying all k operations to each element
    for i in range(n):
        # Apply k multiplications to nums[i]
        boosted_value = nums[i] * (2 ** k)
        
        # Calculate OR with prefix and suffix
        current_or = prefix_or[i] | boosted_value | suffix_or[i + 1]
        max_or = max(max_or, current_or)
    
    return max_or

def maximumOrBruteForce(nums: List[int], k: int) -> int:
    """
    Brute force approach trying all possible ways to distribute operations.
    
    Time: O(n^k) - exponential, only feasible for small k
    Space: O(k) for recursion stack
    """
    def backtrack(index: int, operations_left: int, current_nums: List[int]) -> int:
        if operations_left == 0:
            result = 0
            for num in current_nums:
                result |= num
            return result
        
        if index >= len(current_nums):
            return backtrack(0, operations_left, current_nums)
        
        max_or = 0
        
        # Try not applying operation to current element
        max_or = max(max_or, backtrack(index + 1, operations_left, current_nums))
        
        # Try applying operation to current element
        current_nums[index] *= 2
        max_or = max(max_or, backtrack(index + 1, operations_left - 1, current_nums))
        current_nums[index] //= 2  # Backtrack
        
        return max_or
    
    return backtrack(0, k, nums[:])

def maximumOrGreedy(nums: List[int], k: int) -> int:
    """
    Greedy approach - always boost the element that gives maximum improvement.
    
    Time: O(n * k)
    Space: O(1)
    """
    nums = nums[:]  # Make a copy
    
    for _ in range(k):
        best_improvement = 0
        best_index = 0
        current_or = 0
        
        # Calculate current OR
        for num in nums:
            current_or |= num
        
        # Try doubling each element and see which gives best improvement
        for i in range(len(nums)):
            original_value = nums[i]
            nums[i] *= 2
            
            # Calculate new OR
            new_or = 0
            for num in nums:
                new_or |= num
            
            improvement = new_or - current_or
            if improvement > best_improvement:
                best_improvement = improvement
                best_index = i
            
            nums[i] = original_value  # Restore
        
        # Apply the best operation
        nums[best_index] *= 2
    
    # Calculate final OR
    result = 0
    for num in nums:
        result |= num
    
    return result

def maximumOrOptimized(nums: List[int], k: int) -> int:
    """
    Optimized approach using bit manipulation insights.
    
    Time: O(n)
    Space: O(1)
    """
    n = len(nums)
    
    # The key insight: it's always optimal to apply all k operations to a single element
    # This is because OR is monotonic and concentrating operations maximizes high bits
    
    # Calculate prefix OR for elements before index i
    prefix_or = [0] * n
    if n > 0:
        prefix_or[0] = 0
        for i in range(1, n):
            prefix_or[i] = prefix_or[i - 1] | nums[i - 1]
    
    # Calculate suffix OR for elements after index i
    suffix_or = [0] * n
    if n > 0:
        suffix_or[n - 1] = 0
        for i in range(n - 2, -1, -1):
            suffix_or[i] = suffix_or[i + 1] | nums[i + 1]
    
    max_or = 0
    
    # Try applying all k operations to each element
    for i in range(n):
        boosted_value = nums[i] << k  # Equivalent to nums[i] * (2^k)
        current_or = prefix_or[i] | boosted_value | suffix_or[i]
        max_or = max(max_or, current_or)
    
    return max_or

def maximumOrWithExplanation(nums: List[int], k: int) -> int:
    """
    Version with detailed explanation of the process.
    """
    print(f"Input: nums = {nums}, k = {k}")
    n = len(nums)
    
    # Build prefix and suffix OR arrays
    prefix_or = [0] * n
    suffix_or = [0] * n
    
    # Prefix OR (OR of all elements before index i)
    prefix_or[0] = 0
    for i in range(1, n):
        prefix_or[i] = prefix_or[i - 1] | nums[i - 1]
    
    # Suffix OR (OR of all elements after index i)
    suffix_or[n - 1] = 0
    for i in range(n - 2, -1, -1):
        suffix_or[i] = suffix_or[i + 1] | nums[i + 1]
    
    print(f"Prefix OR: {prefix_or}")
    print(f"Suffix OR: {suffix_or}")
    
    max_or = 0
    best_index = 0
    
    # Try boosting each element
    for i in range(n):
        boosted_value = nums[i] * (2 ** k)
        current_or = prefix_or[i] | boosted_value | suffix_or[i]
        
        print(f"Boosting index {i}: {nums[i]} -> {boosted_value}, OR = {current_or}")
        
        if current_or > max_or:
            max_or = current_or
            best_index = i
    
    print(f"Best strategy: boost index {best_index}, final OR = {max_or}")
    return max_or

# Test Cases
if __name__ == "__main__":
    test_cases = [
        ([12, 9], 1, 30),
        ([8, 1, 2], 2, 35),
        ([1], 5, 32),
        ([1, 2, 4], 1, 7),  # 4 becomes 8, OR of [1,2,8] = 11
        ([7], 2, 28),  # 7 * 4 = 28
    ]
    
    print("Testing main approach:")
    for nums, k, expected in test_cases:
        result = maximumOr(nums[:], k)
        print(f"nums = {nums}, k = {k}")
        print(f"Result: {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()
    
    print("Testing optimized approach:")
    for nums, k, expected in test_cases:
        result = maximumOrOptimized(nums[:], k)
        print(f"nums = {nums}, k = {k}")
        print(f"Result: {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()
    
    # Detailed explanation for first test case
    print("Detailed explanation for [12, 9], k=1:")
    maximumOrWithExplanation([12, 9], 1)

"""
Time and Space Complexity Analysis:

Main Approach:
Time Complexity: O(n) - single pass to build prefix/suffix arrays and one pass to check each position
Space Complexity: O(n) - for prefix and suffix OR arrays

Optimized Approach:
Time Complexity: O(n) - similar to main approach but uses bit shifting
Space Complexity: O(n) - for prefix and suffix arrays

Brute Force Approach:
Time Complexity: O(n^k) - exponential in k, impractical for large k
Space Complexity: O(k) - recursion stack depth

Greedy Approach:
Time Complexity: O(n * k) - for each of k operations, try n positions
Space Complexity: O(n) - for array copy

Key Insights:
1. It's always optimal to apply all k operations to a single element
2. This is because OR is monotonic and concentrating operations maximizes the contribution of high-order bits
3. We can efficiently compute the OR for each choice using prefix and suffix OR arrays
4. Bit shifting (<<) is equivalent to multiplication by powers of 2
5. The problem reduces to finding which element to boost for maximum final OR

Mathematical Insight:
- OR operation: a | b sets all bits that are 1 in either a or b
- Multiplying by 2^k shifts bits left by k positions
- Higher-order bits contribute more to the final OR value
- Concentrating all operations on one element maximizes high-order bit contribution

Topic: Arrays, Bit Manipulation, Prefix Sum, Greedy, OR Operations
"""
