"""
LeetCode Problem #1140: Stone Game II

Problem Statement:
Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones, `piles[i]`. The objective of the game is to maximize the number of stones Alice can get.

Alice and Bob take turns, with Alice starting first. Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. Then, the value of M is updated to max(M, X).

The game continues until all the stones are taken. The person with the most stones wins.

Given an array `piles` where `piles[i]` is the number of stones in the ith pile, return the maximum number of stones Alice can get if both players play optimally.

Constraints:
- 1 <= piles.length <= 100
- 1 <= piles[i] <= 10^4
"""

# Solution
from functools import lru_cache

def stoneGameII(piles):
    n = len(piles)
    # Compute suffix sums to quickly calculate the total stones from any index to the end
    suffix_sum = [0] * n
    suffix_sum[-1] = piles[-1]
    for i in range(n - 2, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + piles[i]

    @lru_cache(None)
    def dfs(index, M):
        # If we can take all remaining piles, return their sum
        if index >= n:
            return 0
        if 2 * M >= n - index:
            return suffix_sum[index]

        max_stones = 0
        # Try taking X piles where 1 <= X <= 2M
        for X in range(1, 2 * M + 1):
            if index + X > n:
                break
            # Maximize Alice's stones by minimizing Bob's stones
            max_stones = max(max_stones, suffix_sum[index] - dfs(index + X, max(M, X)))
        return max_stones

    return dfs(0, 1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    piles = [2, 7, 9, 4, 4]
    print(stoneGameII(piles))  # Expected Output: 10

    # Test Case 2
    piles = [1, 2, 3, 4, 5, 100]
    print(stoneGameII(piles))  # Expected Output: 104

    # Test Case 3
    piles = [8, 15, 3, 7]
    print(stoneGameII(piles))  # Expected Output: 22

    # Test Case 4
    piles = [1, 2]
    print(stoneGameII(piles))  # Expected Output: 3

    # Test Case 5
    piles = [10, 50, 20, 30, 40]
    print(stoneGameII(piles))  # Expected Output: 90

"""
Time and Space Complexity Analysis:

Time Complexity:
- The `dfs` function is called with at most `O(n * n)` unique states, where `n` is the length of the `piles` array.
- For each state, we iterate over at most `2M` choices, where `M` can be at most `n/2`.
- Thus, the time complexity is O(n^3) in the worst case.

Space Complexity:
- The space complexity is O(n^2) due to the memoization table (`lru_cache`).
- Additionally, the recursion stack can go up to O(n) in depth.
- Therefore, the total space complexity is O(n^2).

Topic: Dynamic Programming (DP)
"""