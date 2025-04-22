"""
LeetCode Question #39: Combination Sum

Problem Statement:
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.

The same number may be chosen from `candidates` an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are guaranteed to have a solution, and the input array `candidates` does not contain duplicates.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Constraints:
- 1 <= candidates.length <= 30
- 1 <= candidates[i] <= 200
- All elements of `candidates` are distinct.
- 1 <= target <= 500
"""

# Python Solution
from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    def backtrack(start, target, path):
        # Base case: if target is 0, we found a valid combination
        if target == 0:
            result.append(path[:])
            return
        # Iterate through candidates starting from the current index
        for i in range(start, len(candidates)):
            # If the current candidate exceeds the target, skip it
            if candidates[i] > target:
                continue
            # Include the current candidate and recurse
            path.append(candidates[i])
            backtrack(i, target - candidates[i], path)
            # Backtrack by removing the last added element
            path.pop()

    result = []
    backtrack(0, target, [])
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    candidates = [2, 3, 6, 7]
    target = 7
    print(combinationSum(candidates, target))  # Output: [[2, 2, 3], [7]]

    # Test Case 2
    candidates = [2, 3, 5]
    target = 8
    print(combinationSum(candidates, target))  # Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    # Test Case 3
    candidates = [2]
    target = 1
    print(combinationSum(candidates, target))  # Output: []

    # Test Case 4
    candidates = [1]
    target = 2
    print(combinationSum(candidates, target))  # Output: [[1, 1]]

# Topic: Backtracking