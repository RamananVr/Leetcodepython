"""
LeetCode Problem #2585: Number of Ways to Earn Points

Problem Statement:
You are playing a game that consists of multiple rounds. In each round, you can earn points by completing one of several tasks. Each task has a fixed number of points associated with it and a maximum number of times it can be completed in a single round.

Given:
- An integer `target` representing the total number of points you want to earn.
- A 2D integer array `types` where `types[i] = [points_i, max_count_i]`:
  - `points_i` is the number of points you earn for completing the i-th task.
  - `max_count_i` is the maximum number of times you can complete the i-th task in a single round.

Return:
The number of distinct ways you can earn exactly `target` points. Since the answer may be large, return it modulo `10^9 + 7`.

Constraints:
- 1 <= types.length <= 50
- 1 <= points_i, max_count_i <= 50
- 1 <= target <= 1000

Example:
Input: target = 6, types = [[1, 3], [2, 2]]
Output: 7
Explanation: The 7 ways to earn 6 points are:
- 1+1+1+1+1+1 (6 times 1-point task)
- 1+1+1+1+2 (4 times 1-point task, 1 time 2-point task)
- 1+1+1+2+2 (3 times 1-point task, 2 times 2-point task)
- 1+1+2+2+2 (2 times 1-point task, 3 times 2-point task)
- 1+2+2+2+2 (1 time 1-point task, 4 times 2-point task)
- 2+2+2+2+2 (5 times 2-point task)
- 2+2+2+2+2+2 (6 times 2-point task)

Topic: Dynamic Programming (DP)
"""

# Python Solution
def waysToReachTarget(target: int, types: list[list[int]]) -> int:
    MOD = 10**9 + 7
    n = len(types)
    
    # Initialize a DP array where dp[j] represents the number of ways to earn exactly j points
    dp = [0] * (target + 1)
    dp[0] = 1  # Base case: 1 way to earn 0 points (do nothing)
    
    for points, max_count in types:
        # Iterate backwards to avoid overwriting results for the current task
        for j in range(target, -1, -1):
            for k in range(1, max_count + 1):
                if j >= k * points:
                    dp[j] = (dp[j] + dp[j - k * points]) % MOD
                else:
                    break
    
    return dp[target]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    target = 6
    types = [[1, 3], [2, 2]]
    print(waysToReachTarget(target, types))  # Output: 7

    # Test Case 2
    target = 5
    types = [[1, 2], [2, 3]]
    print(waysToReachTarget(target, types))  # Output: 4

    # Test Case 3
    target = 10
    types = [[2, 5], [3, 4]]
    print(waysToReachTarget(target, types))  # Output: 10

    # Test Case 4
    target = 1
    types = [[1, 1]]
    print(waysToReachTarget(target, types))  # Output: 1

    # Test Case 5
    target = 15
    types = [[3, 5], [5, 3], [7, 2]]
    print(waysToReachTarget(target, types))  # Output: 6

"""
Time Complexity:
- Let `n` be the number of task types and `target` be the target score.
- For each task type, we iterate over the `target` in reverse and for each target value, we iterate up to `max_count`.
- In the worst case, this results in O(n * target * max_count).
- Since `max_count` is at most 50, the complexity simplifies to O(n * target * 50) = O(n * target).

Space Complexity:
- The space complexity is O(target) due to the DP array.

Topic: Dynamic Programming (DP)
"""