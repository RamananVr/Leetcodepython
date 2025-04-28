"""
LeetCode Problem #1703: Minimum Adjacent Swaps for K Consecutive Ones

Problem Statement:
You are given an integer array `nums` and an integer `k`. The array `nums` consists of only `0`s and `1`s. 
In one move, you can choose two adjacent indices and swap their values.

Return the minimum number of moves required so that `k` consecutive `1`s appear in the array.

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
- 1 <= k <= sum(nums)

Example:
Input: nums = [1,0,0,1,0,1], k = 2
Output: 1
Explanation: In 1 move, you can swap the last two elements to get [1,0,0,1,1,0].

Input: nums = [1,0,0,0,0,0,1,1], k = 3
Output: 5
Explanation: In 5 moves, you can rearrange the array to [0,0,0,0,1,1,1,0].

Input: nums = [1,1,0,1], k = 2
Output: 0
Explanation: No swaps are needed since there are already 2 consecutive 1's.
"""

from typing import List

def minMoves(nums: List[int], k: int) -> int:
    """
    Calculate the minimum number of moves required to make k consecutive 1's in the array.
    """
    # Step 1: Extract the indices of all 1's in the array
    ones_indices = [i for i, num in enumerate(nums) if num == 1]
    
    # Step 2: Compute prefix sums of the indices for efficient range sum calculation
    prefix_sum = [0] * (len(ones_indices) + 1)
    for i in range(len(ones_indices)):
        prefix_sum[i + 1] = prefix_sum[i] + ones_indices[i]
    
    # Step 3: Sliding window to find the minimum cost
    min_cost = float('inf')
    for i in range(len(ones_indices) - k + 1):
        mid = i + k // 2
        median = ones_indices[mid]
        left_cost = median * (mid - i) - (prefix_sum[mid] - prefix_sum[i])
        right_cost = (prefix_sum[i + k] - prefix_sum[mid + 1]) - median * (i + k - mid - 1)
        min_cost = min(min_cost, left_cost + right_cost)
    
    return min_cost

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 0, 0, 1, 0, 1]
    k1 = 2
    print(minMoves(nums1, k1))  # Output: 1

    # Test Case 2
    nums2 = [1, 0, 0, 0, 0, 0, 1, 1]
    k2 = 3
    print(minMoves(nums2, k2))  # Output: 5

    # Test Case 3
    nums3 = [1, 1, 0, 1]
    k3 = 2
    print(minMoves(nums3, k3))  # Output: 0

    # Test Case 4
    nums4 = [1, 0, 1, 0, 1, 0, 1]
    k4 = 3
    print(minMoves(nums4, k4))  # Output: 2

"""
Time Complexity:
- Extracting indices of 1's: O(n), where n is the length of nums.
- Prefix sum computation: O(m), where m is the number of 1's in nums.
- Sliding window computation: O(m - k), which is approximately O(m).
Overall: O(n + m), where m is the number of 1's in nums.

Space Complexity:
- Storing indices of 1's: O(m).
- Prefix sum array: O(m).
Overall: O(m), where m is the number of 1's in nums.

Topic: Arrays, Sliding Window, Prefix Sum
"""