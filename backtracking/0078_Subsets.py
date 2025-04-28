"""
LeetCode Problem #78: Subsets

Problem Statement:
Given an integer array `nums` of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of `nums` are unique.
"""

# Clean, Correct Python Solution
from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    result = []
    
    def backtrack(start, current):
        # Append the current subset to the result
        result.append(current[:])
        
        # Explore further subsets
        for i in range(start, len(nums)):
            # Include nums[i] in the current subset
            current.append(nums[i])
            # Recurse with the next index
            backtrack(i + 1, current)
            # Backtrack by removing the last element
            current.pop()
    
    # Start the backtracking process
    backtrack(0, [])
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    print("Input:", nums1)
    print("Output:", subsets(nums1))
    # Expected Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

    # Test Case 2
    nums2 = [0]
    print("Input:", nums2)
    print("Output:", subsets(nums2))
    # Expected Output: [[], [0]]

    # Test Case 3
    nums3 = [1, 2]
    print("Input:", nums3)
    print("Output:", subsets(nums3))
    # Expected Output: [[], [1], [2], [1, 2]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- There are 2^n subsets for a list of size n, as each element can either be included or excluded.
- For each subset, we spend O(n) time to copy the current subset to the result.
- Therefore, the total time complexity is O(n * 2^n).

Space Complexity:
- The recursion stack can go as deep as O(n) in the worst case.
- Additionally, the result list will store all 2^n subsets, and each subset can have up to n elements.
- Thus, the space complexity is O(n * 2^n).
"""

# Topic: Backtracking