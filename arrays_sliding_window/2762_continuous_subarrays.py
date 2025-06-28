"""
LeetCode Problem 2762: Continuous Subarrays

You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:
- The absolute difference between any two elements in the subarray is at most 2.

Return the total number of continuous subarrays.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9

Example 1:
Input: nums = [5,4,2,4]
Output: 6
Explanation: 
Continuous subarrays: [5], [4], [2], [4], [5,4], [2,4].

Example 2:
Input: nums = [1,2,3]
Output: 6
Explanation:
Continuous subarrays: [1], [2], [3], [1,2], [2,3], [1,2,3].

Topics: Arrays, Sliding Window, Deque
"""

from collections import deque

class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        """
        Approach 1: Sliding Window with Deques
        
        Use two deques to maintain min and max in current window.
        Expand window while max - min <= 2, shrink when > 2.
        
        Time: O(n) - each element added/removed from deques at most once
        Space: O(n) - deques can store up to n elements
        """
        n = len(nums)
        result = 0
        left = 0
        
        # Deques to maintain min and max indices in current window
        min_deque = deque()  # Indices of elements in increasing order
        max_deque = deque()  # Indices of elements in decreasing order
        
        for right in range(n):
            # Maintain min_deque in increasing order of values
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # Maintain max_deque in decreasing order of values
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Shrink window while max - min > 2
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                left += 1
                # Remove indices that are out of window
                if min_deque[0] < left:
                    min_deque.popleft()
                if max_deque[0] < left:
                    max_deque.popleft()
            
            # Add count of subarrays ending at right
            result += right - left + 1
        
        return result
    
    def continuousSubarrays_bruteforce(self, nums: list[int]) -> int:
        """
        Approach 2: Brute Force (for comparison)
        
        Check every possible subarray and count valid ones.
        
        Time: O(n^3) - O(n^2) subarrays, O(n) to check each
        Space: O(1)
        """
        n = len(nums)
        count = 0
        
        for i in range(n):
            for j in range(i, n):
                # Check if subarray nums[i:j+1] is continuous
                min_val = min(nums[i:j+1])
                max_val = max(nums[i:j+1])
                if max_val - min_val <= 2:
                    count += 1
        
        return count
    
    def continuousSubarrays_optimized_bruteforce(self, nums: list[int]) -> int:
        """
        Approach 3: Optimized Brute Force
        
        For each starting position, extend as far as possible.
        Track min/max incrementally.
        
        Time: O(n^2)
        Space: O(1)
        """
        n = len(nums)
        count = 0
        
        for i in range(n):
            min_val = max_val = nums[i]
            for j in range(i, n):
                min_val = min(min_val, nums[j])
                max_val = max(max_val, nums[j])
                
                if max_val - min_val <= 2:
                    count += 1
                else:
                    break  # No point extending further
        
        return count

def test_continuous_subarrays():
    """Test the continuous subarrays solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Basic case
    assert solution.continuousSubarrays([5, 4, 2, 4]) == 6
    
    # Test case 2: All elements valid
    assert solution.continuousSubarrays([1, 2, 3]) == 6
    
    # Test case 3: Single element
    assert solution.continuousSubarrays([1]) == 1
    
    # Test case 4: All same elements
    assert solution.continuousSubarrays([1, 1, 1, 1]) == 10
    
    # Test case 5: Large differences
    assert solution.continuousSubarrays([1, 10, 1]) == 3
    
    # Test case 6: Increasing sequence within range
    assert solution.continuousSubarrays([1, 2, 3, 4]) == 8
    
    # Test case 7: Edge case with range exactly 2
    assert solution.continuousSubarrays([1, 3, 2]) == 6
    
    # Compare with brute force on smaller inputs
    test_cases = [
        [5, 4, 2, 4],
        [1, 2, 3],
        [1],
        [1, 1, 1, 1],
        [1, 10, 1]
    ]
    
    for nums in test_cases:
        result1 = solution.continuousSubarrays(nums)
        result2 = solution.continuousSubarrays_optimized_bruteforce(nums)
        assert result1 == result2, f"Mismatch for {nums}: {result1} vs {result2}"
    
    print("All continuous subarrays tests passed!")

if __name__ == "__main__":
    test_continuous_subarrays()
