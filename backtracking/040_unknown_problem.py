"""
LeetCode Problem #40: Combination Sum II

Problem Statement:
Given a collection of candidate numbers (`candidates`) and a target number (`target`), 
find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used once in the combination.

Note:
- All numbers (including `target`) will be positive integers.
- The solution set must not contain duplicate combinations.

You may return the combinations in any order.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
    [1,1,6],
    [1,2,5],
    [1,7],
    [2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
    [1,2,2],
    [5]
]

Constraints:
- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30
"""

# Python Solution
from typing import List

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            # Skip duplicates
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            # If the current number exceeds the target, break (since the array is sorted)
            if candidates[i] > target:
                break
            # Include the current number and move to the next
            path.append(candidates[i])
            backtrack(i + 1, target - candidates[i], path)
            path.pop()  # Backtrack

    candidates.sort()  # Sort to handle duplicates and enable early stopping
    result = []
    backtrack(0, target, [])
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    print("Test Case 1 Output:", combinationSum2(candidates1, target1))
    # Expected Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

    # Test Case 2
    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5
    print("Test Case 2 Output:", combinationSum2(candidates2, target2))
    # Expected Output: [[1, 2, 2], [5]]

    # Test Case 3
    candidates3 = [3, 1, 3, 5, 1]
    target3 = 8
    print("Test Case 3 Output:", combinationSum2(candidates3, target3))
    # Expected Output: [[1, 3, 3], [3, 5]]

# Topic: Backtracking