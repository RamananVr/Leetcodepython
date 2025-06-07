# filepath: q:\source\AgentGeneratedLeetcode\design\2669_count_the_number_of_fair_pairs.py
"""
LeetCode Question #2669: Count the Number of Fair Pairs

Problem Statement:
Given a 0-indexed integer array nums and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:
- 0 <= i < j < nums.length, and
- lower <= nums[i] + nums[j] <= upper

Examples:
Example 1:
Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

Example 2:
Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3) since nums[2] + nums[3] = 9 + 2 = 11.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
- 1 <= lower <= upper <= 2 * 10^9
"""

from typing import List
import bisect

def countFairPairs(nums: List[int], lower: int, upper: int) -> int:
    """
    Count fair pairs using sorting and binary search.
    
    Time: O(n log n)
    Space: O(1) excluding input
    """
    nums.sort()
    n = len(nums)
    count = 0
    
    for i in range(n - 1):
        # For nums[i], find the range of valid nums[j] where j > i
        # We need: lower <= nums[i] + nums[j] <= upper
        # So: lower - nums[i] <= nums[j] <= upper - nums[i]
        
        min_val = lower - nums[i]
        max_val = upper - nums[i]
        
        # Find the leftmost position where nums[j] >= min_val
        left = bisect.bisect_left(nums, min_val, i + 1, n)
        # Find the rightmost position where nums[j] <= max_val
        right = bisect.bisect_right(nums, max_val, i + 1, n)
        
        # Count valid pairs
        count += max(0, right - left)
    
    return count

def countFairPairsBruteForce(nums: List[int], lower: int, upper: int) -> int:
    """
    Brute force approach - check all pairs.
    
    Time: O(n^2)
    Space: O(1)
    """
    n = len(nums)
    count = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            pair_sum = nums[i] + nums[j]
            if lower <= pair_sum <= upper:
                count += 1
    
    return count

def countFairPairsTwoPointers(nums: List[int], lower: int, upper: int) -> int:
    """
    Alternative approach using two pointers after sorting.
    
    Time: O(n^2) in worst case, but often better in practice
    Space: O(1) excluding input
    """
    nums.sort()
    n = len(nums)
    count = 0
    
    for i in range(n - 1):
        left = i + 1
        right = n - 1
        
        # Find the range of valid j values for current i
        valid_start = -1
        valid_end = -1
        
        # Find first valid position
        while left <= right:
            mid = (left + right) // 2
            if nums[i] + nums[mid] >= lower:
                valid_start = mid
                right = mid - 1
            else:
                left = mid + 1
        
        if valid_start == -1:
            continue
        
        # Find last valid position
        left = valid_start
        right = n - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[i] + nums[mid] <= upper:
                valid_end = mid
                left = mid + 1
            else:
                right = mid - 1
        
        if valid_end != -1:
            count += valid_end - valid_start + 1
    
    return count

def countFairPairsOptimized(nums: List[int], lower: int, upper: int) -> int:
    """
    Helper function approach for cleaner code.
    """
    def countPairsLessEqual(target: int) -> int:
        """Count pairs where nums[i] + nums[j] <= target"""
        count = 0
        left, right = 0, len(nums) - 1
        
        while left < right:
            if nums[left] + nums[right] <= target:
                count += right - left
                left += 1
            else:
                right -= 1
        
        return count
    
    nums.sort()
    
    # Count pairs <= upper minus pairs < lower
    return countPairsLessEqual(upper) - countPairsLessEqual(lower - 1)

# Test Cases
if __name__ == "__main__":
    test_cases = [
        ([0, 1, 7, 4, 4, 5], 3, 6, 6),
        ([1, 7, 9, 2, 5], 11, 11, 1),
        ([1, 2, 3], 3, 5, 2),  # (0,1): 1+2=3, (0,2): 1+3=4
        ([1, 1, 1, 1], 2, 2, 6),  # All pairs sum to 2
        ([0, 0, 0], 0, 1, 3),  # All pairs sum to 0
    ]
    
    print("Testing optimized binary search approach:")
    for nums, lower, upper, expected in test_cases:
        result = countFairPairs(nums.copy(), lower, upper)
        print(f"nums={nums}, lower={lower}, upper={upper}")
        print(f"Result: {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()
    
    print("Testing brute force approach:")
    for nums, lower, upper, expected in test_cases:
        result = countFairPairsBruteForce(nums.copy(), lower, upper)
        print(f"nums={nums}, lower={lower}, upper={upper}")
        print(f"Result: {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()
    
    print("Testing optimized helper function approach:")
    for nums, lower, upper, expected in test_cases:
        result = countFairPairsOptimized(nums.copy(), lower, upper)
        print(f"nums={nums}, lower={lower}, upper={upper}")
        print(f"Result: {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()

"""
Time and Space Complexity Analysis:

Binary Search Approach:
Time Complexity: O(n log n) - sorting + n binary searches
Space Complexity: O(1) - only using constant extra space

Brute Force Approach:
Time Complexity: O(n^2) - checking all pairs
Space Complexity: O(1) - only using constant extra space

Optimized Helper Approach:
Time Complexity: O(n log n) - sorting + two O(n) two-pointer scans
Space Complexity: O(1) - only using constant extra space

Key Insights:
1. Sorting enables efficient range queries with binary search
2. The problem reduces to finding elements in a specific range
3. Two-pointer technique can also solve this efficiently
4. Binary search provides the most straightforward implementation

Topic: Arrays, Binary Search, Two Pointers, Sorting
"""
