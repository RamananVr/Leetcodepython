"""
LeetCode Problem 2799: Count Complete Subarrays in an Array

You are given an array nums consisting of positive integers.

We call a subarray complete if the number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.

Return the number of complete subarrays.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 2000

Example 1:
Input: nums = [1,3,1,2,2]
Output: 4
Explanation: The complete subarrays are: [1,3,1,2], [1,3,1,2,2], [3,1,2], [3,1,2,2].

Example 2:
Input: nums = [5,5,5]
Output: 6
Explanation: The complete subarrays are: [5], [5], [5], [5,5], [5,5], [5,5,5].

Topics: Array, Hash Table, Sliding Window
"""

class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        """
        Approach 1: Brute Force - Check all subarrays
        
        For each possible subarray, count distinct elements and compare
        with total distinct elements in the array.
        
        Time: O(n^3) - O(n^2) subarrays, O(n) to check each
        Space: O(n) for storing distinct elements
        """
        n = len(nums)
        total_distinct = len(set(nums))
        count = 0
        
        for i in range(n):
            distinct_elements = set()
            for j in range(i, n):
                distinct_elements.add(nums[j])
                
                if len(distinct_elements) == total_distinct:
                    count += 1
        
        return count
    
    def countCompleteSubarrays_optimized(self, nums: list[int]) -> int:
        """
        Approach 2: Optimized with early termination
        
        Once we have all distinct elements in a subarray, all extensions
        of that subarray will also be complete.
        
        Time: O(n^2) - early termination helps in practice
        Space: O(n)
        """
        n = len(nums)
        total_distinct = len(set(nums))
        count = 0
        
        for i in range(n):
            distinct_elements = set()
            for j in range(i, n):
                distinct_elements.add(nums[j])
                
                if len(distinct_elements) == total_distinct:
                    # All subarrays from i to k (k >= j) are complete
                    count += n - j
                    break
        
        return count
    
    def countCompleteSubarrays_sliding_window(self, nums: list[int]) -> int:
        """
        Approach 3: Sliding Window approach
        
        Use sliding window to find the shortest complete subarray starting
        at each position, then count all extensions.
        
        Time: O(n^2) in worst case, but often better
        Space: O(n)
        """
        from collections import defaultdict
        
        n = len(nums)
        total_distinct = len(set(nums))
        count = 0
        
        for start in range(n):
            element_count = defaultdict(int)
            distinct_count = 0
            
            for end in range(start, n):
                # Add current element
                if element_count[nums[end]] == 0:
                    distinct_count += 1
                element_count[nums[end]] += 1
                
                # Check if subarray is complete
                if distinct_count == total_distinct:
                    # All subarrays from start to k (k >= end) are complete
                    count += n - end
                    break
        
        return count
    
    def countCompleteSubarrays_frequency_tracking(self, nums: list[int]) -> int:
        """
        Approach 4: Track frequency changes efficiently
        
        More efficient tracking of when we gain/lose distinct elements.
        
        Time: O(n^2)
        Space: O(n)
        """
        n = len(nums)
        total_distinct = len(set(nums))
        count = 0
        
        for i in range(n):
            freq = {}
            distinct = 0
            
            for j in range(i, n):
                # Add nums[j] to current subarray
                if nums[j] not in freq:
                    freq[nums[j]] = 0
                    distinct += 1
                freq[nums[j]] += 1
                
                # Check if complete
                if distinct == total_distinct:
                    count += n - j
                    break
        
        return count
    
    def countCompleteSubarrays_two_pointers(self, nums: list[int]) -> int:
        """
        Approach 5: Two pointers with optimization
        
        Use two pointers to efficiently find complete subarrays.
        
        Time: O(n^2)
        Space: O(n)
        """
        n = len(nums)
        total_distinct = len(set(nums))
        count = 0
        
        for left in range(n):
            seen = set()
            for right in range(left, n):
                seen.add(nums[right])
                
                if len(seen) == total_distinct:
                    # Found first complete subarray starting at left
                    # All subarrays [left, k] where k >= right are complete
                    count += n - right
                    break
                elif len(seen) > total_distinct:
                    # This shouldn't happen with our logic
                    break
        
        return count

def test_count_complete_subarrays():
    """Test the count complete subarrays solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Basic case
    assert solution.countCompleteSubarrays([1, 3, 1, 2, 2]) == 4
    # Total distinct: 3 (1, 2, 3)
    # Complete subarrays: [1,3,1,2], [1,3,1,2,2], [3,1,2], [3,1,2,2]
    
    # Test case 2: All same elements
    assert solution.countCompleteSubarrays([5, 5, 5]) == 6
    # Total distinct: 1 (5)
    # All subarrays are complete: [5], [5], [5], [5,5], [5,5], [5,5,5]
    
    # Test case 3: Single element
    assert solution.countCompleteSubarrays([1]) == 1
    
    # Test case 4: All different elements
    assert solution.countCompleteSubarrays([1, 2, 3]) == 1
    # Only the entire array [1,2,3] is complete
    
    # Test case 5: Two distinct elements
    assert solution.countCompleteSubarrays([1, 2, 1, 2]) == 3
    # Total distinct: 2 (1, 2)
    # Complete subarrays: [1,2], [1,2,1], [1,2,1,2]
    
    # Test case 6: Complex case
    result6 = solution.countCompleteSubarrays([1, 1, 2, 2, 3, 3])
    # Total distinct: 3 (1, 2, 3)
    # Need to find all subarrays containing all three elements
    
    # Test case 7: Repeating pattern
    assert solution.countCompleteSubarrays([1, 2, 1, 2, 1]) == 4
    # Total distinct: 2 (1, 2)
    # Complete subarrays start from positions where we first see both
    
    # Test case 8: Large numbers
    assert solution.countCompleteSubarrays([1000, 2000, 1000]) == 2
    # Total distinct: 2
    # Complete subarrays: [1000,2000], [1000,2000,1000]
    
    # Test case 9: Early complete subarray
    assert solution.countCompleteSubarrays([1, 2, 3, 1, 2, 3]) == 10
    # Total distinct: 3
    # Once we have [1,2,3], many extensions are possible
    
    # Compare different approaches
    test_cases = [
        [1, 3, 1, 2, 2],
        [5, 5, 5],
        [1],
        [1, 2, 3],
        [1, 2, 1, 2],
        [1, 1, 2, 2, 3, 3],
        [1, 2, 1, 2, 1],
        [1000, 2000, 1000]
    ]
    
    for nums in test_cases:
        result1 = solution.countCompleteSubarrays(nums)
        result2 = solution.countCompleteSubarrays_optimized(nums)
        result3 = solution.countCompleteSubarrays_sliding_window(nums)
        result4 = solution.countCompleteSubarrays_frequency_tracking(nums)
        result5 = solution.countCompleteSubarrays_two_pointers(nums)
        
        assert result1 == result2 == result3 == result4 == result5, \
            f"Mismatch for {nums}: {result1}, {result2}, {result3}, {result4}, {result5}"
    
    # Test edge cases
    assert solution.countCompleteSubarrays([1, 1, 1, 1]) == 10  # n*(n+1)/2 = 4*5/2 = 10
    assert solution.countCompleteSubarrays([1, 2]) == 1  # Only [1,2] is complete
    
    # Test larger case
    nums_large = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    result_large = solution.countCompleteSubarrays_optimized(nums_large)
    # Should be efficient with optimization
    
    print("All count complete subarrays tests passed!")

if __name__ == "__main__":
    test_count_complete_subarrays()
