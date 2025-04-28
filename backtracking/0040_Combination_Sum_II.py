"""
LeetCode Problem #40: Combination Sum II

Problem Statement:
Given a collection of candidate numbers (`candidates`) and a target number (`target`), 
find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used once in the combination.

Note:
- All numbers (including `target`) will be positive integers.
- The solution set must not contain duplicate combinations.

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

def combinationSum2(candidates, target):
    """
    Finds all unique combinations of numbers in `candidates` that sum up to `target`.
    Each number in `candidates` can only be used once in the combination.

    :param candidates: List[int] - List of candidate numbers
    :param target: int - Target sum
    :return: List[List[int]] - List of unique combinations
    """
    def backtrack(start, target, path):
        # Base case: if target is 0, add the current path to the result
        if target == 0:
            result.append(path[:])
            return
        
        # Iterate through the candidates starting from the current index
        for i in range(start, len(candidates)):
            # Skip duplicates
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            # If the current candidate exceeds the target, break early (since the array is sorted)
            if candidates[i] > target:
                break
            
            # Include the current candidate and move to the next index
            path.append(candidates[i])
            backtrack(i + 1, target - candidates[i], path)
            path.pop()  # Backtrack by removing the last element

    # Sort the candidates to handle duplicates and enable early stopping
    candidates.sort()
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

"""
Time Complexity:
- Sorting the candidates takes O(n log n), where n is the length of the candidates array.
- The backtracking algorithm explores subsets of the candidates array. In the worst case, 
  it generates all possible subsets, which is O(2^n). However, due to pruning (skipping duplicates 
  and stopping early when the target is exceeded), the actual number of subsets explored is much smaller.
- Overall, the time complexity is O(2^n) in the worst case.

Space Complexity:
- The space complexity is O(n), where n is the depth of the recursion tree (equal to the length of the candidates array).
- Additional space is used for the `path` list and the `result` list, but these are proportional to the input size.

Topic: Backtracking
"""