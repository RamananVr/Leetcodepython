"""
LeetCode Problem 2765: Longest Alternating Subarray

You are given a 0-indexed integer array nums. A subarray s of length m is called alternating if:
- m is greater than 1.
- s[0] != s[1].
- s[i] != s[i+1] for all i from 0 to m - 2.

Return the length of the longest alternating subarray of nums or 0 if no such subarray exists.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4

Example 1:
Input: nums = [2,3,3,3]
Output: 2
Explanation: The longest alternating subarray is [2,3].

Example 2:
Input: nums = [1,2,1,2]
Output: 4
Explanation: The longest alternating subarray is [1,2,1,2].

Example 3:
Input: nums = [3,3,3,3]
Output: 0
Explanation: No alternating subarray exists.

Topics: Arrays, Two Pointers, Sliding Window
"""

class Solution:
    def alternatingSubarray(self, nums: list[int]) -> int:
        """
        Approach 1: Two Pointers / Sliding Window
        
        Use two pointers to find the longest alternating subarray.
        Track current length and maximum length found.
        
        Time: O(n) - single pass through array
        Space: O(1) - only using constant extra space
        """
        if len(nums) < 2:
            return 0
        
        max_length = 0
        current_length = 1
        
        for i in range(1, len(nums)):
            # Check if current element is different from previous
            if nums[i] != nums[i-1]:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 1  # Reset to single element
        
        return max_length if max_length > 1 else 0
    
    def alternatingSubarray_bruteforce(self, nums: list[int]) -> int:
        """
        Approach 2: Brute Force
        
        Check all possible subarrays to find longest alternating one.
        
        Time: O(n^3) - O(n^2) subarrays, O(n) to check each
        Space: O(1)
        """
        n = len(nums)
        max_length = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                # Check if subarray nums[i:j+1] is alternating
                is_alternating = True
                for k in range(i, j):
                    if nums[k] == nums[k + 1]:
                        is_alternating = False
                        break
                
                if is_alternating:
                    max_length = max(max_length, j - i + 1)
        
        return max_length
    
    def alternatingSubarray_optimized_bruteforce(self, nums: list[int]) -> int:
        """
        Approach 3: Optimized Brute Force
        
        For each starting position, extend as far as possible.
        Stop early when alternating pattern breaks.
        
        Time: O(n^2) - worst case, but often better in practice
        Space: O(1)
        """
        n = len(nums)
        max_length = 0
        
        for i in range(n):
            current_length = 1
            
            for j in range(i + 1, n):
                if nums[j] != nums[j - 1]:
                    current_length += 1
                    max_length = max(max_length, current_length)
                else:
                    break  # Pattern broken, no point continuing
        
        return max_length if max_length > 1 else 0
    
    def alternatingSubarray_dp(self, nums: list[int]) -> int:
        """
        Approach 4: Dynamic Programming approach
        
        Track the length of alternating subarray ending at each position.
        
        Time: O(n)
        Space: O(1)
        """
        if len(nums) < 2:
            return 0
        
        max_length = 0
        current_length = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                current_length += 1
            else:
                current_length = 1
            
            if current_length > 1:
                max_length = max(max_length, current_length)
        
        return max_length

def test_alternating_subarray():
    """Test the alternating subarray solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Basic case
    assert solution.alternatingSubarray([2, 3, 3, 3]) == 2
    
    # Test case 2: Full array alternating
    assert solution.alternatingSubarray([1, 2, 1, 2]) == 4
    
    # Test case 3: No alternating subarray
    assert solution.alternatingSubarray([3, 3, 3, 3]) == 0
    
    # Test case 4: Single element
    assert solution.alternatingSubarray([1]) == 0
    
    # Test case 5: Two different elements
    assert solution.alternatingSubarray([1, 2]) == 2
    
    # Test case 6: Two same elements
    assert solution.alternatingSubarray([1, 1]) == 0
    
    # Test case 7: Mixed pattern
    assert solution.alternatingSubarray([1, 2, 2, 3, 1]) == 2
    
    # Test case 8: Long alternating in middle
    assert solution.alternatingSubarray([5, 5, 1, 2, 1, 2, 1, 3, 3]) == 5
    
    # Test case 9: All different elements
    assert solution.alternatingSubarray([1, 2, 3, 4, 5]) == 5
    
    # Compare different approaches
    test_cases = [
        [2, 3, 3, 3],
        [1, 2, 1, 2],
        [3, 3, 3, 3],
        [1],
        [1, 2],
        [1, 1],
        [1, 2, 2, 3, 1],
        [5, 5, 1, 2, 1, 2, 1, 3, 3],
        [1, 2, 3, 4, 5]
    ]
    
    for nums in test_cases:
        result1 = solution.alternatingSubarray(nums)
        result2 = solution.alternatingSubarray_optimized_bruteforce(nums)
        result3 = solution.alternatingSubarray_dp(nums)
        assert result1 == result2 == result3, f"Mismatch for {nums}: {result1}, {result2}, {result3}"
    
    print("All alternating subarray tests passed!")

if __name__ == "__main__":
    test_alternating_subarray()
