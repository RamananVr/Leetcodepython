"""
LeetCode Problem #1510: Stone Game IV

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones from the pile.

Also, if a player cannot make a move, they lose the game.

Given a positive integer n, return true if and only if Alice wins the game assuming both players play optimally.

Constraints:
- 1 <= n <= 10^5
"""

def winnerSquareGame(n: int) -> bool:
    """
    Determines if Alice can win the game given n stones and both players playing optimally.
    """
    # dp[i] represents whether the player whose turn it is can win with i stones remaining
    dp = [False] * (n + 1)
    
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            if not dp[i - j * j]:  # If the opponent loses after this move, current player wins
                dp[i] = True
                break
            j += 1
    
    return dp[n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Alice wins
    n1 = 1
    print(winnerSquareGame(n1))  # Expected: True (Alice removes 1 stone and wins)

    # Test Case 2: Alice loses
    n2 = 2
    print(winnerSquareGame(n2))  # Expected: False (Alice removes 1 stone, Bob removes 1 stone and wins)

    # Test Case 3: Alice wins
    n3 = 4
    print(winnerSquareGame(n3))  # Expected: True (Alice removes 4 stones and wins)

    # Test Case 4: Larger input
    n4 = 7
    print(winnerSquareGame(n4))  # Expected: False (Alice cannot force a win)

    # Test Case 5: Larger input
    n5 = 17
    print(winnerSquareGame(n5))  # Expected: False (Alice cannot force a win)

"""
Time Complexity:
- The outer loop runs from 1 to n, so O(n).
- The inner loop iterates over all square numbers less than or equal to i. The number of square numbers less than or equal to i is approximately O(sqrt(i)).
- Therefore, the total time complexity is O(n * sqrt(n)).

Space Complexity:
- The space complexity is O(n) due to the dp array.

Topic: Dynamic Programming (DP)
"""