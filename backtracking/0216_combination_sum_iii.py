"""
LeetCode Question #216: Combination Sum III

Problem Statement:
Find all possible combinations of `k` numbers that add up to a number `n`, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Return a list of all possible combinations. The list must not contain duplicate combinations, and the numbers in each combination must be sorted in ascending order.

Constraints:
- 2 <= k <= 9
- 1 <= n <= 60

Example:
Input: k = 3, n = 7
Output: [[1, 2, 4]]

Input: k = 3, n = 9
Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
"""

# Clean, Correct Python Solution
def combinationSum3(k: int, n: int) -> list[list[int]]:
    def backtrack(start, path, target):
        # Base case: if the combination is valid
        if len(path) == k and target == 0:
            result.append(path[:])
            return
        # If the combination is invalid, stop further exploration
        if len(path) > k or target < 0:
            return
        
        # Explore numbers from `start` to 9
        for i in range(start, 10):
            path.append(i)  # Choose the current number
            backtrack(i + 1, path, target - i)  # Explore further
            path.pop()  # Undo the choice
    
    result = []
    backtrack(1, [], n)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    k = 3
    n = 7
    print(f"Input: k = {k}, n = {n}")
    print(f"Output: {combinationSum3(k, n)}")  # Expected: [[1, 2, 4]]

    # Test Case 2
    k = 3
    n = 9
    print(f"Input: k = {k}, n = {n}")
    print(f"Output: {combinationSum3(k, n)}")  # Expected: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]

    # Test Case 3
    k = 4
    n = 1
    print(f"Input: k = {k}, n = {n}")
    print(f"Output: {combinationSum3(k, n)}")  # Expected: []

    # Test Case 4
    k = 2
    n = 18
    print(f"Input: k = {k}, n = {n}")
    print(f"Output: {combinationSum3(k, n)}")  # Expected: [[9, 9]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution uses backtracking to explore all possible combinations of numbers from 1 to 9.
- In the worst case, we explore all subsets of size `k` from the set {1, 2, ..., 9}.
- The number of subsets is approximately 2^9 = 512, but since we limit the size to `k`, the complexity is reduced.
- The time complexity is O(9^k), where `k` is the size of the combination.

Space Complexity:
- The space complexity is O(k) for the recursion stack and O(9^k) for storing the results.
- The recursion stack depth is proportional to `k`, and the result list stores all valid combinations.

Overall:
Time Complexity: O(9^k)
Space Complexity: O(k + 9^k)
"""

# Topic: Backtracking