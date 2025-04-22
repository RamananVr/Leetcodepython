"""
LeetCode Question #992: Subarrays with K Different Integers

Problem Statement:
Given an integer array `nums` and an integer `k`, return the number of subarrays 
that have exactly `k` different integers.

A subarray is a contiguous part of an array.

Example:
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays with exactly 2 different integers are:
[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,3].

Constraints:
- 1 <= nums.length <= 2 * 10^4
- 1 <= nums[i], k <= nums.length
"""

# Solution
from collections import defaultdict

def subarraysWithKDistinct(nums, k):
    def atMostKDistinct(nums, k):
        """Helper function to count subarrays with at most k distinct integers."""
        count = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(nums)):
            if count[nums[right]] == 0:
                k -= 1
            count[nums[right]] += 1
            
            while k < 0:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    k += 1
                left += 1
            
            result += right - left + 1
        return result
    
    # Subarrays with exactly k distinct = Subarrays with at most k distinct - Subarrays with at most (k-1) distinct
    return atMostKDistinct(nums, k) - atMostKDistinct(nums, k - 1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [1, 2, 1, 2, 3]
    k = 2
    print(subarraysWithKDistinct(nums, k))  # Output: 7

    # Test Case 2
    nums = [1, 2, 1, 3, 4]
    k = 3
    print(subarraysWithKDistinct(nums, k))  # Output: 3

    # Test Case 3
    nums = [1, 2, 3, 4, 5]
    k = 1
    print(subarraysWithKDistinct(nums, k))  # Output: 5

    # Test Case 4
    nums = [1, 1, 1, 1, 1]
    k = 1
    print(subarraysWithKDistinct(nums, k))  # Output: 15

# Time and Space Complexity Analysis
"""
Time Complexity:
- The helper function `atMostKDistinct` iterates through the array once, and the sliding window 
  ensures that each element is processed at most twice (once when expanding the window and once 
  when contracting it). Thus, the time complexity is O(n), where n is the length of the array.
- Since we call `atMostKDistinct` twice, the overall time complexity is O(n).

Space Complexity:
- The space complexity is O(k), where k is the number of distinct integers in the sliding window. 
  This is due to the `count` dictionary used to track the frequency of elements in the current window.
"""

# Topic: Sliding Window, Hash Table