"""
LeetCode Problem #1563: Stone Game V

Problem Statement:
Alice and Bob play a game with piles of stones. There are n piles of stones arranged in a row. Each pile has a positive integer number of stones `stoneValue[i]`.

The rules of the game are as follows:
1. Alice and Bob take turns, with Alice starting first.
2. On each player's turn, they can choose any pile of stones and split the row into two non-empty subarrays (left and right). The score of the player is the sum of stones in the smaller subarray. If both subarrays have the same sum, the player can choose either one.
3. The game ends when there is only one pile remaining, and the player cannot make a move.

Return the maximum score Alice can obtain assuming both players play optimally.

Constraints:
- 1 <= stoneValue.length <= 500
- 1 <= stoneValue[i] <= 10^6
"""

# Python Solution
def stoneGameV(stoneValue):
    n = len(stoneValue)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + stoneValue[i]

    # Memoization table
    dp = [[-1] * n for _ in range(n)]

    def dfs(left, right):
        if left == right:
            return 0
        if dp[left][right] != -1:
            return dp[left][right]

        max_score = 0
        for i in range(left, right):
            left_sum = prefix_sum[i + 1] - prefix_sum[left]
            right_sum = prefix_sum[right + 1] - prefix_sum[i + 1]

            if left_sum < right_sum:
                max_score = max(max_score, left_sum + dfs(left, i))
            elif left_sum > right_sum:
                max_score = max(max_score, right_sum + dfs(i + 1, right))
            else:
                max_score = max(max_score, left_sum + max(dfs(left, i), dfs(i + 1, right)))

        dp[left][right] = max_score
        return max_score

    return dfs(0, n - 1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    stoneValue1 = [6, 2, 3, 4, 5, 5]
    print(stoneGameV(stoneValue1))  # Expected Output: 18

    # Test Case 2
    stoneValue2 = [7, 7, 7]
    print(stoneGameV(stoneValue2))  # Expected Output: 14

    # Test Case 3
    stoneValue3 = [4]
    print(stoneGameV(stoneValue3))  # Expected Output: 0

    # Test Case 4
    stoneValue4 = [1, 2, 3, 4, 5]
    print(stoneGameV(stoneValue4))  # Expected Output: 10

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function uses memoization and recursion to solve the problem.
- For each pair of indices (left, right), we iterate over all possible split points, which takes O(n) time.
- There are O(n^2) pairs of indices (left, right), so the overall time complexity is O(n^3).

Space Complexity:
- The `dp` table requires O(n^2) space.
- The `prefix_sum` array requires O(n) space.
- The recursion stack depth is O(n) in the worst case.
- Overall space complexity is O(n^2).

Topic: Dynamic Programming
"""