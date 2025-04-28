"""
LeetCode Question #2953: Full Problem Statement

Problem Statement:
You are given a list of integers `nums` and an integer `target`. Your task is to find all unique combinations in `nums` where the numbers sum to `target`. Each number in `nums` may be used an unlimited number of times. The solution set must not contain duplicate combinations.

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

Note:
- You may return the combinations in any order.
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
    nums.sort()  # Sorting helps to avoid unnecessary combinations
    backtrack(0, target, [])
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 6, 7]
    target1 = 7
    print("Test Case 1 Output:", combinationSum(nums1, target1))  # Expected: [[2, 2, 3], [7]]

    # Test Case 2
    nums2 = [2, 3, 5]
    target2 = 8
    print("Test Case 2 Output:", combinationSum(nums2, target2))  # Expected: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    # Test Case 3
    nums3 = [2]
    target3 = 1
    print("Test Case 3 Output:", combinationSum(nums3, target3))  # Expected: []

    # Test Case 4
    nums4 = [1]
    target4 = 1
    print("Test Case 4 Output:", combinationSum(nums4, target4))  # Expected: [[1]]

    # Test Case 5
    nums5 = [2, 3, 5]
    target5 = 10
    print("Test Case 5 Output:", combinationSum(nums5, target5))  # Expected: [[2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 3, 5], [5, 5]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The time complexity is O(2^T), where T is the target value. This is because for each number in `nums`, we explore all possible combinations that sum up to `target`.

Space Complexity:
- The space complexity is O(T), where T is the target value. This is due to the recursion stack and the space used to store the current combination path.
"""

# Topic: Backtracking