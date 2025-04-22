"""
LeetCode Problem #46: Permutations

Problem Statement:
Given an array `nums` of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of `nums` are unique.
"""

# Solution
from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    def backtrack(start=0):
        # If we've reached the end of the array, add the current permutation
        if start == len(nums):
            result.append(nums[:])  # Make a copy of nums
            return
        
        for i in range(start, len(nums)):
            # Swap the current element with the start element
            nums[start], nums[i] = nums[i], nums[start]
            # Recurse on the next part of the array
            backtrack(start + 1)
            # Backtrack (undo the swap)
            nums[start], nums[i] = nums[i], nums[start]
    
    result = []
    backtrack()
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    print("Input:", nums1)
    print("Output:", permute(nums1))
    print()

    # Test Case 2
    nums2 = [0, 1]
    print("Input:", nums2)
    print("Output:", permute(nums2))
    print()

    # Test Case 3
    nums3 = [1]
    print("Input:", nums3)
    print("Output:", permute(nums3))
    print()

"""
Time Complexity:
- The total number of permutations of an array of size `n` is `n!` (factorial of n).
- For each permutation, we perform a constant amount of work (swapping and backtracking).
- Therefore, the time complexity is O(n * n!), where the extra `n` comes from the cost of copying the current permutation into the result.

Space Complexity:
- The recursion stack can go as deep as `n` (the length of the input array), so the space complexity for the recursion is O(n).
- Additionally, we store all the permutations in the result list, which takes O(n * n!) space.
- Overall, the space complexity is O(n * n!).

Topic: Backtracking
"""