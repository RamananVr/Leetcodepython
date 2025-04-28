"""
LeetCode Question #2983: Full Problem Statement

Problem Statement:
You are given a list of integers `nums` and an integer `target`. Your task is to find all unique combinations in `nums` where the numbers sum to `target`. Each number in `nums` may be used multiple times in the combination.

The solution set must not contain duplicate combinations. You may return the combinations in any order.

Constraints:
1. 1 <= nums.length <= 30
2. 1 <= nums[i] <= 200
3. All elements of nums are distinct.
4. 1 <= target <= 500

Example:
Input: nums = [2, 3, 6, 7], target = 7
Output: [[2, 2, 3], [7]]

Input: nums = [2, 3, 5], target = 8
Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

Input: nums = [2], target = 1
Output: []

Follow-up:
Can you optimize your solution to handle larger inputs efficiently?
"""

# Clean, Correct Python Solution
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
    nums.sort()  # Sorting helps to avoid unnecessary computations
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
    nums4 = [1, 2, 3]
    target4 = 4
    print(combinationSum(nums4, target4))  # Expected Output: [[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The time complexity is O(2^n), where n is the number of elements in `nums`.
- This is because for each number, we decide whether to include it in the combination or not, leading to exponential growth.

Space Complexity:
- The space complexity is O(target / min(nums)), where `min(nums)` is the smallest number in the list.
- This is due to the recursion stack and the storage of intermediate combinations.

Overall, the algorithm is efficient for small to medium-sized inputs but may struggle with larger inputs due to the exponential nature of the problem.

Topic: Backtracking
"""