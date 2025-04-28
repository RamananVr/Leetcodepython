"""
LeetCode Problem #1712: Ways to Split Array Into Three Subarrays

Problem Statement:
You are given a sorted array of integers `nums`.

Split the array into three non-empty contiguous subarrays `left`, `mid`, `right` such that:
- The sum of elements in `left` is less than or equal to the sum of elements in `mid`, and
- The sum of elements in `mid` is less than or equal to the sum of elements in `right`.

Return the number of ways to split `nums` such that the above conditions are satisfied. 
Since the answer may be large, return it modulo 10^9 + 7.

Example:
Input: nums = [1,2,2,2,5,0]
Output: 3
Explanation: There are three ways to split nums:
1. left = [1], mid = [2,2], right = [2,5,0]
2. left = [1], mid = [2,2,2], right = [5,0]
3. left = [1,2], mid = [2,2], right = [5,0]

Constraints:
- 3 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^4
"""

# Python Solution
from typing import List

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Compute prefix sums
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]
        
        result = 0
        
        # Iterate over the first split point
        for i in range(n - 2):
            if prefix[i] > prefix[-1] - prefix[i]:  # If left sum > total sum of mid + right, break
                break
            
            # Binary search for the first valid mid split point
            left = i + 1
            right = n - 2
            while left < right:
                mid = (left + right) // 2
                if prefix[mid] - prefix[i] >= prefix[i]:
                    right = mid
                else:
                    left = mid + 1
            mid_start = left
            
            # Binary search for the last valid mid split point
            left = i + 1
            right = n - 2
            while left < right:
                mid = (left + right + 1) // 2
                if prefix[mid] - prefix[i] <= prefix[-1] - prefix[mid]:
                    left = mid
                else:
                    right = mid - 1
            mid_end = left
            
            # Add the number of valid splits
            if mid_start <= mid_end:
                result += (mid_end - mid_start + 1)
                result %= MOD
        
        return result

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [1, 2, 2, 2, 5, 0]
    print(solution.waysToSplit(nums1))  # Output: 3
    
    # Test Case 2
    nums2 = [1, 1, 1]
    print(solution.waysToSplit(nums2))  # Output: 1
    
    # Test Case 3
    nums3 = [1, 1, 1, 1]
    print(solution.waysToSplit(nums3))  # Output: 2
    
    # Test Case 4
    nums4 = [0, 3, 3, 6, 6]
    print(solution.waysToSplit(nums4))  # Output: 4

"""
Time Complexity:
- Computing the prefix sum takes O(n).
- For each possible first split point (O(n)), we perform two binary searches (O(log n)).
- Thus, the overall time complexity is O(n log n).

Space Complexity:
- The prefix sum array takes O(n) space.
- Thus, the overall space complexity is O(n).

Topic: Arrays, Binary Search, Prefix Sum
"""