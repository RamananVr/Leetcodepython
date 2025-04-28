"""
LeetCode Problem #2968: Problem Statement

You are given a list of integers `nums` and an integer `target`. Your task is to find all unique combinations in `nums` where the numbers sum up to `target`. Each number in `nums` may be used multiple times in the combination.

The solution set must not contain duplicate combinations. You may return the combinations in any order.

Constraints:
- 1 <= nums.length <= 30
- 1 <= nums[i] <= 200
- All integers in `nums` are distinct.
- 1 <= target <= 500

Example:
Input: nums = [2, 3, 6, 7], target = 7
Output: [[2, 2, 3], [7]]

Input: nums = [2, 3, 5], target = 8
Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

Input: nums = [2], target = 1
Output: []
"""

# Python Solution
from typing import List

def combinationSum(nums: List[int], target: int) -> List[List[int]]:
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])
            return
        for i in range(start, len(nums)):
            if nums[i] <= target:
                path.append(nums[i])
                backtrack(i, target - nums[i], path)
                path.pop()

    result = []
    backtrack(0, target, [])
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 6, 7]
    target1 = 7
    print(combinationSum(nums1, target1))  # Expected Output: [[2, 2, 3], [7]]

    # Test Case 2
    nums2 = [2, 3, 5]
    target2 = 8
    print(combinationSum(nums2, target2))  # Expected Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    # Test Case 3
    nums3 = [2]
    target3 = 1
    print(combinationSum(nums3, target3))  # Expected Output: []

    # Test Case 4
    nums4 = [1]
    target4 = 1
    print(combinationSum(nums4, target4))  # Expected Output: [[1]]

    # Test Case 5
    nums5 = [1, 2]
    target5 = 4
    print(combinationSum(nums5, target5))  # Expected Output: [[1, 1, 1, 1], [1, 1, 2], [2, 2]]

"""
Time and Space Complexity Analysis

Time Complexity:
- The time complexity is O(2^(target/min(nums))) in the worst case. This is because for each number in `nums`, we explore all possible combinations recursively until the target is reached.

Space Complexity:
- The space complexity is O(target/min(nums)) due to the recursion stack and the storage of intermediate paths.

Topic: Backtracking
"""