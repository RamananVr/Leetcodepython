"""
LeetCode Problem #1879: Minimum XOR Sum of Two Arrays

Problem Statement:
You are given two integer arrays nums1 and nums2 of length n.

The XOR sum of the two arrays is defined as the sum of nums1[i] XOR nums2[j] 
for all 0 <= i, j < n, where each element in nums1 is paired with exactly one 
element in nums2 (and vice versa).

Return the minimum XOR sum of nums1 and nums2.

Constraints:
- n == nums1.length == nums2.length
- 1 <= n <= 14
- 0 <= nums1[i], nums2[i] <= 2^14
"""

# Solution
from functools import lru_cache

def minimumXORSum(nums1, nums2):
    n = len(nums1)
    
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return 0
        
        min_xor_sum = float('inf')
        for j in range(n):
            if mask & (1 << j) == 0:  # Check if nums2[j] is not used
                xor_sum = nums1[i] ^ nums2[j]
                min_xor_sum = min(min_xor_sum, xor_sum + dp(i + 1, mask | (1 << j)))
        
        return min_xor_sum
    
    return dp(0, 0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2]
    nums2 = [2, 3]
    print(minimumXORSum(nums1, nums2))  # Expected Output: 2

    # Test Case 2
    nums1 = [1, 0, 3]
    nums2 = [5, 3, 4]
    print(minimumXORSum(nums1, nums2))  # Expected Output: 8

    # Test Case 3
    nums1 = [0, 1, 2]
    nums2 = [2, 3, 4]
    print(minimumXORSum(nums1, nums2))  # Expected Output: 6

"""
Time and Space Complexity Analysis:

Time Complexity:
- The number of states in the DP is O(n * 2^n), where `n` is the length of nums1 and nums2.
- For each state, we iterate through `n` elements to find the minimum XOR sum.
- Therefore, the overall time complexity is O(n * n * 2^n), which is feasible for n <= 14.

Space Complexity:
- The space complexity is dominated by the memoization table, which stores O(n * 2^n) states.
- Additionally, the recursion stack can go up to O(n) depth.
- Therefore, the overall space complexity is O(n * 2^n).

Topic: Dynamic Programming (DP)
"""