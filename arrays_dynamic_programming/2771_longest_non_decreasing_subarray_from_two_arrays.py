"""
LeetCode Problem 2771: Longest Non-decreasing Subarray From Two Arrays

You are given two 0-indexed integer arrays nums1 and nums2 of length n.

Let's define another 0-indexed integer array nums3 of length n such that for each index i in the range [0, n - 1], you can assign nums3[i] to be either nums1[i] or nums2[i].

Your task is to maximize the length of the longest non-decreasing subarray in nums3.

Return the length of the longest non-decreasing subarray in nums3.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
- 1 <= nums1.length == nums2.length <= 10^5
- 1 <= nums1[i], nums2[i] <= 10^9

Example 1:
Input: nums1 = [2,3,1], nums2 = [1,2,1]
Output: 2
Explanation: One way to construct nums3 is: 
nums3 = [nums1[0], nums2[1], nums2[2]] => [2, 2, 1].
The longest non-decreasing subarray is [2, 2] with length 2.

Example 2:
Input: nums1 = [1,3,2,1], nums2 = [2,2,3,4]
Output: 4
Explanation: One way to construct nums3 is:
nums3 = [nums1[0], nums2[1], nums2[2], nums2[3]] => [1, 2, 3, 4].
The entire array is non-decreasing, so the length is 4.

Example 3:
Input: nums1 = [1,1], nums2 = [2,2]
Output: 2

Topics: Array, Dynamic Programming
"""

class Solution:
    def maxNonDecreasingLength(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Approach 1: Dynamic Programming
        
        For each position i, track the longest non-decreasing subarray ending at i
        when choosing from nums1[i] or nums2[i].
        
        dp1[i] = longest non-decreasing subarray ending at i using nums1[i]
        dp2[i] = longest non-decreasing subarray ending at i using nums2[i]
        
        Time: O(n)
        Space: O(n) - can be optimized to O(1)
        """
        n = len(nums1)
        if n == 0:
            return 0
        
        # dp1[i] = length ending at i with nums1[i]
        # dp2[i] = length ending at i with nums2[i]
        dp1 = [1] * n
        dp2 = [1] * n
        
        for i in range(1, n):
            # If we choose nums1[i] at position i
            if nums1[i] >= nums1[i-1]:
                dp1[i] = max(dp1[i], dp1[i-1] + 1)
            if nums1[i] >= nums2[i-1]:
                dp1[i] = max(dp1[i], dp2[i-1] + 1)
            
            # If we choose nums2[i] at position i
            if nums2[i] >= nums1[i-1]:
                dp2[i] = max(dp2[i], dp1[i-1] + 1)
            if nums2[i] >= nums2[i-1]:
                dp2[i] = max(dp2[i], dp2[i-1] + 1)
        
        return max(max(dp1), max(dp2))
    
    def maxNonDecreasingLength_optimized(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Approach 2: Space-optimized DP
        
        Since we only need the previous state, optimize space to O(1).
        
        Time: O(n)
        Space: O(1)
        """
        n = len(nums1)
        if n == 0:
            return 0
        
        # Previous state
        prev_dp1 = prev_dp2 = 1
        max_length = 1
        
        for i in range(1, n):
            curr_dp1 = curr_dp2 = 1
            
            # If we choose nums1[i] at position i
            if nums1[i] >= nums1[i-1]:
                curr_dp1 = max(curr_dp1, prev_dp1 + 1)
            if nums1[i] >= nums2[i-1]:
                curr_dp1 = max(curr_dp1, prev_dp2 + 1)
            
            # If we choose nums2[i] at position i
            if nums2[i] >= nums1[i-1]:
                curr_dp2 = max(curr_dp2, prev_dp1 + 1)
            if nums2[i] >= nums2[i-1]:
                curr_dp2 = max(curr_dp2, prev_dp2 + 1)
            
            max_length = max(max_length, curr_dp1, curr_dp2)
            prev_dp1, prev_dp2 = curr_dp1, curr_dp2
        
        return max_length
    
    def maxNonDecreasingLength_bruteforce(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Approach 3: Brute Force (for verification on small inputs)
        
        Try all possible combinations and find the longest non-decreasing subarray.
        
        Time: O(2^n * n^2) - exponential, only for small inputs
        Space: O(n)
        """
        n = len(nums1)
        max_length = 0
        
        # Try all 2^n possible combinations
        for mask in range(1 << n):
            nums3 = []
            for i in range(n):
                if mask & (1 << i):
                    nums3.append(nums1[i])
                else:
                    nums3.append(nums2[i])
            
            # Find longest non-decreasing subarray in nums3
            current_length = 1
            max_subarray_length = 1
            
            for i in range(1, n):
                if nums3[i] >= nums3[i-1]:
                    current_length += 1
                    max_subarray_length = max(max_subarray_length, current_length)
                else:
                    current_length = 1
            
            max_length = max(max_length, max_subarray_length)
        
        return max_length

def test_max_non_decreasing_length():
    """Test the max non-decreasing length solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Basic case
    assert solution.maxNonDecreasingLength([2, 3, 1], [1, 2, 1]) == 2
    
    # Test case 2: Full array possible
    assert solution.maxNonDecreasingLength([1, 3, 2, 1], [2, 2, 3, 4]) == 4
    
    # Test case 3: Same length arrays
    assert solution.maxNonDecreasingLength([1, 1], [2, 2]) == 2
    
    # Test case 4: Single element
    assert solution.maxNonDecreasingLength([5], [3]) == 1
    
    # Test case 5: All decreasing in both
    assert solution.maxNonDecreasingLength([5, 4, 3], [6, 5, 4]) == 1
    
    # Test case 6: Optimal choice switches between arrays
    assert solution.maxNonDecreasingLength([1, 5, 3], [4, 2, 6]) == 3
    
    # Test case 7: One array is better throughout
    assert solution.maxNonDecreasingLength([1, 2, 3, 4], [5, 6, 7, 8]) == 4
    
    # Test case 8: Mixed optimal choices
    assert solution.maxNonDecreasingLength([10, 20, 10, 30], [20, 10, 30, 20]) == 3
    
    # Compare approaches on smaller inputs
    small_test_cases = [
        ([2, 3, 1], [1, 2, 1]),
        ([1, 1], [2, 2]),
        ([5], [3]),
        ([5, 4, 3], [6, 5, 4]),
        ([1, 5], [4, 2])
    ]
    
    for nums1, nums2 in small_test_cases:
        result1 = solution.maxNonDecreasingLength(nums1, nums2)
        result2 = solution.maxNonDecreasingLength_optimized(nums1, nums2)
        if len(nums1) <= 10:  # Only test brute force on very small inputs
            result3 = solution.maxNonDecreasingLength_bruteforce(nums1, nums2)
            assert result1 == result2 == result3, f"Mismatch for {nums1}, {nums2}: {result1}, {result2}, {result3}"
        else:
            assert result1 == result2, f"Mismatch for {nums1}, {nums2}: {result1}, {result2}"
    
    print("All max non-decreasing length tests passed!")

if __name__ == "__main__":
    test_max_non_decreasing_length()
