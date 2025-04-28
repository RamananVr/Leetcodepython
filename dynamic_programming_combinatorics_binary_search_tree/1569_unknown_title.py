"""
LeetCode Problem #1569: Number of Ways to Reorder Array to Get Same BST

Problem Statement:
Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.

- The answer may be very large, so return it modulo 10^9 + 7.

Constraints:
1. 1 <= nums.length <= 1000
2. 1 <= nums[i] <= nums.length
3. All integers in nums are distinct.

Example 1:
Input: nums = [2,1,3]
Output: 1
Explanation: We can reorder nums to get the same BST in only 1 way: [2,1,3]

Example 2:
Input: nums = [3,4,5,1,2]
Output: 5
Explanation: There are 5 ways to reorder nums to get the same BST.

Example 3:
Input: nums = [1,2,3]
Output: 0
Explanation: There are no other orderings of nums that will result in the same BST.
"""

from math import comb
from functools import lru_cache

MOD = 10**9 + 7

def numOfWays(nums):
    """
    Function to calculate the number of ways to reorder nums to get the same BST.
    """
    @lru_cache(None)
    def count_ways(arr):
        if len(arr) <= 2:
            return 1  # Base case: 0 or 1 element, only one way to reorder
        
        root = arr[0]
        left = [x for x in arr if x < root]
        right = [x for x in arr if x > root]
        
        # Calculate the number of ways to interleave left and right subtrees
        left_size, right_size = len(left), len(right)
        interleave_ways = comb(left_size + right_size, left_size)
        
        # Recursively calculate the number of ways for left and right subtrees
        return (interleave_ways * count_ways(tuple(left)) * count_ways(tuple(right))) % MOD
    
    # Subtract 1 because the original order is not counted as a "reordering"
    return (count_ways(tuple(nums)) - 1) % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 1, 3]
    print(numOfWays(nums1))  # Output: 1

    # Test Case 2
    nums2 = [3, 4, 5, 1, 2]
    print(numOfWays(nums2))  # Output: 5

    # Test Case 3
    nums3 = [1, 2, 3]
    print(numOfWays(nums3))  # Output: 0

    # Additional Test Case
    nums4 = [4, 2, 1, 3, 6, 5, 7]
    print(numOfWays(nums4))  # Output: 80

"""
Time Complexity:
- The function `count_ways` is called recursively for each subtree. 
- For each call, we compute the binomial coefficient using `comb`, which is O(min(n, k)) for nCk.
- In the worst case, the recursion depth is O(n), where n is the size of the input array.
- Thus, the overall time complexity is approximately O(n^2) in the worst case.

Space Complexity:
- The space complexity is O(n) for the recursion stack and O(n^2) for the memoization cache.

Topic: Dynamic Programming, Combinatorics, Binary Search Tree
"""