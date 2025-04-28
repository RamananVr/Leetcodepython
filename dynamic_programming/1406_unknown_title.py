"""
LeetCode Problem #1406: Stone Game III

Problem Statement:
Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer representing its score. Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2, or 3 stones from the row. The score of each stone taken is added to the player's score. The game ends when all the stones have been taken.

The winner is the player with the higher score, and if the scores are tied, the result is a draw. Alice and Bob will each play optimally to maximize their scores.

Given an integer array `stoneValue`, where `stoneValue[i]` is the value of the ith stone, return "Alice" if Alice wins, "Bob" if Bob wins, or "Tie" if they end with the same score.

Constraints:
- 1 <= stoneValue.length <= 5 * 10^4
- -1000 <= stoneValue[i] <= 1000
"""

# Solution
from typing import List

def stoneGameIII(stoneValue: List[int]) -> str:
    n = len(stoneValue)
    dp = [float('-inf')] * (n + 1)  # dp[i] represents the max score difference Alice can achieve starting from index i
    dp[n] = 0  # Base case: no stones left, score difference is 0

    for i in range(n - 1, -1, -1):
        current_sum = 0
        for k in range(1, 4):  # Alice can take 1, 2, or 3 stones
            if i + k <= n:
                current_sum += stoneValue[i + k - 1]
                dp[i] = max(dp[i], current_sum - dp[i + k])

    if dp[0] > 0:
        return "Alice"
    elif dp[0] < 0:
        return "Bob"
    else:
        return "Tie"

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    stoneValue = [1, 2, 3, 7]
    print(stoneGameIII(stoneValue))  # Expected Output: "Bob"

    # Test Case 2
    stoneValue = [1, 2, 3, -9]
    print(stoneGameIII(stoneValue))  # Expected Output: "Alice"

    # Test Case 3
    stoneValue = [1, 2, 3, 6]
    print(stoneGameIII(stoneValue))  # Expected Output: "Tie"

    # Test Case 4
    stoneValue = [1, 2, 3, -1, -2, -3, 7]
    print(stoneGameIII(stoneValue))  # Expected Output: "Alice"

    # Test Case 5
    stoneValue = [-1, -2, -3]
    print(stoneGameIII(stoneValue))  # Expected Output: "Tie"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates over the array from the last index to the first (O(n)).
- For each index, it considers up to 3 possible moves (constant time).
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The algorithm uses a dp array of size n + 1 to store intermediate results.
- Thus, the space complexity is O(n).
"""

# Topic: Dynamic Programming