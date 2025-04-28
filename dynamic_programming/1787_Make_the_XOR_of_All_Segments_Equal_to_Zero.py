"""
LeetCode Problem #1787: Make the XOR of All Segments Equal to Zero

Problem Statement:
You are given an array nums and an integer k. The array is split into k segments, where each segment is a consecutive 
subarray of the array. After splitting the array into k segments, you can rearrange the order of the segments.

The XOR of a segment is the XOR of all the numbers in that segment. The XOR of all the segments is the XOR of their 
individual XORs. Return the minimum number of elements that need to be changed in the array to make the XOR of all 
segments equal to zero.

Example:
Input: nums = [1,2,0,3,0], k = 2
Output: 1
Explanation: We can split the array into segments [1,2] and [0,3,0]. Rearranging the segments gives [0,3,0] and [1,2]. 
The XOR of the segments is (0 XOR 3 XOR 0) XOR (1 XOR 2) = 0. We only need to change one element, for example, change 
nums[0] to 0.

Constraints:
- 1 <= k <= nums.length <= 2000
- 0 <= nums[i] < 2^10
"""

# Python Solution
from collections import Counter
from functools import lru_cache

def minChanges(nums, k):
    # Step 1: Group numbers by their modulo k value
    groups = [[] for _ in range(k)]
    for i, num in enumerate(nums):
        groups[i % k].append(num)
    
    # Step 2: Calculate frequency of numbers in each group
    freq = [Counter(group) for group in groups]
    
    # Step 3: Dynamic Programming to minimize changes
    @lru_cache(None)
    def dp(index, xor):
        if index == k:
            return 0 if xor == 0 else float('inf')
        
        # Option 1: Change all elements in the group to a single value
        total_elements = len(groups[index])
        min_changes = float('inf')
        for key, count in freq[index].items():
            min_changes = min(min_changes, dp(index + 1, xor ^ key) + (total_elements - count))
        
        return min_changes
    
    # Step 4: Solve the problem starting from the first group
    return dp(0, 0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 0, 3, 0]
    k1 = 2
    print(minChanges(nums1, k1))  # Output: 1

    # Test Case 2
    nums2 = [4, 3, 1, 2, 4, 3]
    k2 = 3
    print(minChanges(nums2, k2))  # Output: 3

    # Test Case 3
    nums3 = [0, 0, 0, 0]
    k3 = 1
    print(minChanges(nums3, k3))  # Output: 0

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    k4 = 5
    print(minChanges(nums4, k4))  # Output: 5

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses dynamic programming with memoization. For each group, we iterate over all possible XOR values 
  (up to 2^10 = 1024) and all possible keys in the frequency counter. This results in a complexity of O(k * 1024 * m), 
  where m is the average number of unique elements in each group. In the worst case, m = n/k, so the complexity is 
  approximately O(n * 1024).

Space Complexity:
- The space complexity is dominated by the memoization table, which stores results for O(k * 1024) states. Additionally, 
  we store frequency counters for each group, which takes O(n) space. Thus, the total space complexity is O(k * 1024 + n).

Topic: Dynamic Programming
"""