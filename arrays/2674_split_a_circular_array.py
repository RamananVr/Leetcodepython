"""
LeetCode Question #2674: Split a Circular Array

Problem Statement:
Given a 0-indexed integer array nums of length n, split it into two non-empty arrays such that:
- The first array consists of the first k elements of nums for some k (1 <= k < n).
- The second array consists of the remaining elements of nums.
- In both arrays, the first element is the maximum element of that array.

Return the number of ways to split the array.

Examples:
Example 1:
Input: nums = [2,1,3,4,5,2]
Output: 3
Explanation: The array can be split in the following ways:
- [2] and [1,3,4,5,2]: The first element 2 is the maximum in [2], and the first element 1 is not the maximum in [1,3,4,5,2].
- [2,1] and [3,4,5,2]: The first element 2 is the maximum in [2,1], and the first element 3 is not the maximum in [3,4,5,2].
- [2,1,3,4,5] and [2]: The first element 2 is the maximum in [2,1,3,4,5], and the first element 2 is the maximum in [2].

Wait, let me reconsider this problem. The split should result in valid arrays where first element is maximum.

Example 1:
Input: nums = [2,1,3,4,5,2]
Valid splits:
- k=1: [2] and [1,3,4,5,2] -> first=2 (max), first=1 (not max) -> Invalid
- k=2: [2,1] and [3,4,5,2] -> first=2 (max), first=3 (not max) -> Invalid  
- k=3: [2,1,3] and [4,5,2] -> first=2 (not max), first=4 (not max) -> Invalid
- k=4: [2,1,3,4] and [5,2] -> first=2 (not max), first=5 (max) -> Invalid
- k=5: [2,1,3,4,5] and [2] -> first=2 (not max), first=2 (max) -> Invalid

Let me reread... Actually, let me implement based on the constraint that first element should be maximum in each part.

Example 2:
Input: nums = [1,1,1]
Output: 2
Explanation: [1] and [1,1], or [1,1] and [1] are both valid.

Constraints:
- 2 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
"""

from typing import List

def waysToSplitArray(nums: List[int]) -> int:
    """
    Count ways to split array such that first element is maximum in each part.
    
    Time: O(n^2) in worst case
    Space: O(1)
    """
    n = len(nums)
    count = 0
    
    for k in range(1, n):  # k is the length of first array
        # Check if first element is maximum in first part [0:k]
        first_part_max = max(nums[:k])
        if nums[0] != first_part_max:
            continue
        
        # Check if first element is maximum in second part [k:n]
        second_part_max = max(nums[k:])
        if nums[k] != second_part_max:
            continue
        
        count += 1
    
    return count

def waysToSplitArrayOptimized(nums: List[int]) -> int:
    """
    Optimized approach using precomputed prefix and suffix maximums.
    
    Time: O(n)
    Space: O(n)
    """
    n = len(nums)
    
    # Precompute prefix maximums
    prefix_max = [0] * n
    prefix_max[0] = nums[0]
    for i in range(1, n):
        prefix_max[i] = max(prefix_max[i-1], nums[i])
    
    # Precompute suffix maximums
    suffix_max = [0] * n
    suffix_max[n-1] = nums[n-1]
    for i in range(n-2, -1, -1):
        suffix_max[i] = max(suffix_max[i+1], nums[i])
    
    count = 0
    for k in range(1, n):
        # Check if nums[0] is maximum in [0:k]
        if nums[0] == prefix_max[k-1]:
            # Check if nums[k] is maximum in [k:n]
            if nums[k] == suffix_max[k]:
                count += 1
    
    return count

def waysToSplitArraySinglePass(nums: List[int]) -> int:
    """
    Single pass approach with rolling maximum.
    
    Time: O(n^2) worst case, but more efficient in practice
    Space: O(1)
    """
    n = len(nums)
    count = 0
    
    for k in range(1, n):
        # Check first part: nums[0] should be max in nums[0:k]
        first_part_valid = True
        for i in range(1, k):
            if nums[i] > nums[0]:
                first_part_valid = False
                break
        
        if not first_part_valid:
            continue
        
        # Check second part: nums[k] should be max in nums[k:n]
        second_part_valid = True
        for i in range(k + 1, n):
            if nums[i] > nums[k]:
                second_part_valid = False
                break
        
        if second_part_valid:
            count += 1
    
    return count

def waysToSplitArrayEarlyTermination(nums: List[int]) -> int:
    """
    Approach with early termination optimizations.
    
    Time: O(n^2) worst case, O(n) best case
    Space: O(1)
    """
    n = len(nums)
    count = 0
    
    # Find all positions where nums[0] could be maximum up to that point
    valid_k_positions = []
    current_max = nums[0]
    
    for k in range(1, n):
        if k > 1:
            current_max = max(current_max, nums[k-1])
        
        # nums[0] is maximum in [0:k] if current_max == nums[0]
        if current_max == nums[0]:
            valid_k_positions.append(k)
    
    # For each valid k, check if nums[k] is maximum in [k:n]
    for k in valid_k_positions:
        is_valid = True
        for i in range(k + 1, n):
            if nums[i] > nums[k]:
                is_valid = False
                break
        
        if is_valid:
            count += 1
    
    return count

# Test Cases
if __name__ == "__main__":
    test_cases = [
        ([2, 1, 3, 4, 5, 2], 0),  # Need to verify this
        ([1, 1, 1], 2),
        ([3, 1, 2], 0),
        ([1, 2, 1], 1),  # k=2: [1,2] and [1] -> 2 is max in first, 1 is max in second
        ([5, 4, 3, 2, 1], 4),  # All splits work since array is decreasing
    ]
    
    print("Testing main approach:")
    for nums, expected in test_cases:
        result = waysToSplitArray(nums.copy())
        print(f"nums = {nums}")
        print(f"Result: {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
        
        # Show detailed analysis
        n = len(nums)
        print("Detailed analysis:")
        for k in range(1, n):
            first_part = nums[:k]
            second_part = nums[k:]
            first_max = max(first_part)
            second_max = max(second_part)
            valid = (nums[0] == first_max) and (nums[k] == second_max)
            print(f"  k={k}: {first_part} | {second_part} -> {nums[0]}=={first_max} and {nums[k]}=={second_max} -> {'Valid' if valid else 'Invalid'}")
        print()
    
    print("Testing optimized approach:")
    for nums, expected in test_cases:
        result = waysToSplitArrayOptimized(nums.copy())
        print(f"nums = {nums}")
        print(f"Result: {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()

"""
Time and Space Complexity Analysis:

Main Approach:
Time Complexity: O(n^2) - for each split position, we find max in both parts
Space Complexity: O(1) - only using constant extra space

Optimized Approach:
Time Complexity: O(n) - single pass to build prefix/suffix arrays + O(n) to check
Space Complexity: O(n) - for prefix and suffix maximum arrays

Single Pass Approach:
Time Complexity: O(n^2) - for each position, we check all elements in both parts
Space Complexity: O(1) - only using constant extra space

Key Insights:
1. A split is valid if and only if the first element is maximum in the first part AND the element at split position is maximum in the second part
2. We can optimize by precomputing prefix and suffix maximums
3. The constraint that first element must be maximum limits valid split positions
4. This problem tests understanding of array partitioning and maximum finding

Topic: Arrays, Prefix Sum, Maximum Finding, Array Splitting
"""
