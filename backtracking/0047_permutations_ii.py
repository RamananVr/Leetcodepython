"""
LeetCode Question #47: Permutations II

Problem Statement:
Given a collection of numbers, `nums`, that might contain duplicates, return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output: [[1,1,2], [1,2,1], [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

Constraints:
- 1 <= nums.length <= 8
- -10 <= nums[i] <= 10
"""

from typing import List

def permuteUnique(nums: List[int]) -> List[List[int]]:
    """
    Generate all unique permutations of the input list `nums`.
    """
    def backtrack(path, counter):
        # If the current path is a complete permutation, add it to the result
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        # Iterate through the counter dictionary
        for num in counter:
            if counter[num] > 0:
                # Choose the current number
                path.append(num)
                counter[num] -= 1
                
                # Explore further
                backtrack(path, counter)
                
                # Undo the choice (backtrack)
                path.pop()
                counter[num] += 1

    # Initialize result list and counter dictionary
    result = []
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1
    
    # Start backtracking
    backtrack([], counter)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 1, 2]
    print("Input:", nums1)
    print("Output:", permuteUnique(nums1))
    # Expected Output: [[1,1,2], [1,2,1], [2,1,1]]

    # Test Case 2
    nums2 = [1, 2, 3]
    print("Input:", nums2)
    print("Output:", permuteUnique(nums2))
    # Expected Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

    # Test Case 3
    nums3 = [2, 2, 1, 1]
    print("Input:", nums3)
    print("Output:", permuteUnique(nums3))
    # Expected Output: [[1,1,2,2], [1,2,1,2], [1,2,2,1], [2,1,1,2], [2,1,2,1], [2,2,1,1]]

"""
Time Complexity:
- The time complexity is O(n! * n), where n is the length of the input list `nums`.
  - There are at most n! permutations, and for each permutation, we spend O(n) time to construct it.

Space Complexity:
- The space complexity is O(n), where n is the length of the input list `nums`.
  - This is due to the recursion stack and the space used by the `path` list.

Topic: Backtracking
"""