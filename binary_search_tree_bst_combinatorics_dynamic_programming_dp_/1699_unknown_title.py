"""
LeetCode Problem #1699: "Number of Ways to Reorder Array to Get Same BST"

Problem Statement:
Given an array nums that represents a permutation of integers from 1 to n. 
We are going to reorder nums into a binary search tree (BST) by inserting the elements in order from left to right. 
Return the number of ways to reorder nums such that the constructed BST is identical to that formed from the original array nums.

Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:
Input: nums = [2,1,3]
Output: 1
Explanation: We can reorder nums in only one way: [2,1,3]. The BST formed in this case is identical to the original BST.

Example 2:
Input: nums = [3,4,5,1,2]
Output: 5
Explanation: There are 5 ways to reorder nums to get the same BST.

Example 3:
Input: nums = [1,2,3]
Output: 0
Explanation: There are no other orderings of nums that will result in the same BST.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= nums.length
- All integers in nums are distinct.
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
            return 1  # Base case: 0 or 1 way to reorder if array has <= 2 elements
        
        root = arr[0]
        left = [x for x in arr if x < root]
        right = [x for x in arr if x > root]
        
        # Calculate the number of ways to interleave left and right subtrees
        left_size, right_size = len(left), len(right)
        interleave_ways = comb(left_size + right_size, left_size)
        
        # Recursively calculate the number of ways for left and right subtrees
        return (interleave_ways * count_ways(tuple(left)) * count_ways(tuple(right))) % MOD

    # Subtract 1 because the original order is not considered a "reordering"
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

    # Test Case 4
    nums4 = [4, 3, 2, 1]
    print(numOfWays(nums4))  # Output: 0

    # Test Case 5
    nums5 = [5, 3, 8, 2, 4, 7, 9]
    print(numOfWays(nums5))  # Output: 80


"""
Time Complexity:
- The function `count_ways` is called recursively for each subtree. 
- For each call, we split the array into left and right subtrees, which takes O(n) time.
- The number of recursive calls is proportional to the number of nodes in the BST, which is O(n).
- Calculating combinations using `comb` is O(n) for each call.
- Overall, the time complexity is approximately O(n^2) in the worst case.

Space Complexity:
- The space complexity is dominated by the recursion stack and the memoization cache.
- The recursion stack depth is O(n) in the worst case.
- The memoization cache stores results for subsets of the array, which can be O(2^n) in the worst case.
- Overall, the space complexity is O(2^n) due to memoization.

Topic: Binary Search Tree (BST), Combinatorics, Dynamic Programming (DP)
"""