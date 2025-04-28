"""
LeetCode Problem #39: Combination Sum

Problem Statement:
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.

The same number may be chosen from `candidates` an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are guaranteed to have at least one valid solution. The input array is guaranteed to not contain duplicates.

Constraints:
- 1 <= candidates.length <= 30
- 1 <= candidates[i] <= 200
- All elements of `candidates` are distinct.
- 1 <= target <= 500
"""

# Solution
from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    def backtrack(start, target, path):
        # Base case: if target is 0, we found a valid combination
        if target == 0:
            result.append(path[:])
            return
        # Iterate through the candidates starting from the current index
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
    print("Test Case 1:", combinationSum(candidates, target))
    # Expected Output: [[2, 2, 3], [7]]

    # Test Case 2
    candidates = [2, 3, 5]
    target = 8
    print("Test Case 2:", combinationSum(candidates, target))
    # Expected Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    # Test Case 3
    candidates = [2]
    target = 1
    print("Test Case 3:", combinationSum(candidates, target))
    # Expected Output: []

    # Test Case 4
    candidates = [1]
    target = 1
    print("Test Case 4:", combinationSum(candidates, target))
    # Expected Output: [[1]]

    # Test Case 5
    candidates = [1]
    target = 2
    print("Test Case 5:", combinationSum(candidates, target))
    # Expected Output: [[1, 1]]

"""
Time Complexity Analysis:
- Let `n` be the number of candidates and `T` be the target value.
- In the worst case, the algorithm explores all possible combinations of candidates that sum up to `T`.
- The depth of the recursion tree is at most `T / min(candidates)`, and at each level, we iterate over `n` candidates.
- Therefore, the time complexity is O(n^(T/min(candidates))).

Space Complexity Analysis:
- The space complexity is determined by the recursion stack and the space used to store the result.
- The recursion stack can go as deep as `T / min(candidates)`, and the result list can grow to include all valid combinations.
- Therefore, the space complexity is O(T / min(candidates)) for the recursion stack and O(number of combinations) for the result.

Topic: Backtracking
"""