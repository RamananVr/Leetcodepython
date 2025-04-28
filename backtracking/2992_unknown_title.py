"""
LeetCode Problem #2992: Full Problem Statement

Problem:
You are given a list of integers `nums` and an integer `target`. Your task is to find all unique combinations in `nums` where the numbers sum to `target`. Each number in `nums` can be used an unlimited number of times. The solution set must not contain duplicate combinations.

Constraints:
1. All numbers (including `target`) will be positive integers.
2. The input list `nums` will not contain duplicates.
3. You may return the combinations in any order.

Example:
Input: nums = [2, 3, 6, 7], target = 7
Output: [[2, 2, 3], [7]]

Input: nums = [2, 3, 5], target = 8
Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

Input: nums = [2], target = 1
Output: []

Follow-up:
Can you optimize the solution to avoid unnecessary recursive calls?
"""

# Clean, Correct Python Solution
from typing import List

def combinationSum(nums: List[int], target: int) -> List[List[int]]:
    def backtrack(start, target, path):
        # Base case: if target is 0, add the current path to the result
        if target == 0:
            result.append(path[:])
            return
        # Iterate through the candidates starting from the current index
        for i in range(start, len(nums)):
            # If the current number exceeds the target, skip it
            if nums[i] > target:
                continue
            # Include the current number and recurse
            path.append(nums[i])
            backtrack(i, target - nums[i], path)
            # Backtrack by removing the last number added
            path.pop()

    result = []
    nums.sort()  # Optional: sort the input to optimize the recursion
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
    target4 = 2
    print(combinationSum(nums4, target4))  # Expected Output: [[1, 1]]

    # Test Case 5
    nums5 = [3, 4, 5]
    target5 = 9
    print(combinationSum(nums5, target5))  # Expected Output: [[3, 3, 3], [3, 4, 4], [4, 5]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The time complexity is O(2^T), where T is the target value. This is because, in the worst case, we explore all possible combinations of numbers that sum up to the target.

Space Complexity:
- The space complexity is O(T), where T is the target value. This is due to the recursion stack and the space used to store the current path.

Overall, the algorithm is efficient for small to medium-sized inputs but may become slow for very large target values or large input arrays.
"""

# Topic: Backtracking