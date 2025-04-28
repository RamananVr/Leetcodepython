"""
LeetCode Problem #887: Super Egg Drop

Problem Statement:
You are given `k` eggs, and you have access to a building with `n` floors from 1 to n. Each egg is identical in function, and if an egg breaks, you cannot use it again. You want to determine the minimum number of moves you need to find the highest floor from which you can drop the egg without breaking it.

Rules:
1. If an egg breaks when dropped from floor x, then it will also break when dropped from any floor above x.
2. If an egg does not break when dropped from floor x, then it will not break when dropped from any floor below x.
3. You may reuse a non-broken egg in future drops.

Write a function `superEggDrop(k: int, n: int) -> int` that returns the minimum number of moves required to find the critical floor.

Constraints:
- 1 <= k <= 100
- 1 <= n <= 10^4
"""

# Solution
def superEggDrop(k: int, n: int) -> int:
    """
    Dynamic Programming solution to solve the Super Egg Drop problem.
    """
    # dp[m][k] represents the maximum number of floors that can be tested with m moves and k eggs
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Iterate over the number of moves
    for m in range(1, n + 1):
        for e in range(1, k + 1):
            # Recurrence relation: dp[m][e] = dp[m-1][e-1] + dp[m-1][e] + 1
            dp[m][e] = dp[m - 1][e - 1] + dp[m - 1][e] + 1
            # If we can test all n floors, return the number of moves
            if dp[m][e] >= n:
                return m

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    k1, n1 = 1, 2
    print(f"superEggDrop({k1}, {n1}) = {superEggDrop(k1, n1)}")  # Expected: 2

    # Test Case 2
    k2, n2 = 2, 6
    print(f"superEggDrop({k2}, {n2}) = {superEggDrop(k2, n2)}")  # Expected: 3

    # Test Case 3
    k3, n3 = 3, 14
    print(f"superEggDrop({k3}, {n3}) = {superEggDrop(k3, n3)}")  # Expected: 4

    # Test Case 4
    k4, n4 = 2, 100
    print(f"superEggDrop({k4}, {n4}) = {superEggDrop(k4, n4)}")  # Expected: 14

# Time Complexity Analysis:
# The outer loop runs for at most `n` moves, and the inner loop runs for `k` eggs.
# Each iteration involves a constant-time computation, so the time complexity is O(n * k).
# However, the algorithm terminates early when dp[m][k] >= n, so the actual runtime is much faster in practice.

# Space Complexity Analysis:
# The space complexity is O(n * k) due to the dp table.

# Topic: Dynamic Programming