"""
LeetCode Problem #935: Knight Dialer

Problem Statement:
The chess knight has a unique movement, it may move two squares in one direction and then one square in a perpendicular direction, or vice versa. The knight can move to eight possible positions from its current position.

The chessboard used in this problem is a grid of numbers arranged like this:

    1 2 3
    4 5 6
    7 8 9
      0

This grid represents a phone keypad. The knight starts at any number and makes `n-1` hops. Each hop must be a valid knight move. Every time it lands on a number, it counts as one distinct number sequence.

Given an integer `n`, return how many distinct phone numbers of length `n` we can dial.

Since the answer may be very large, return the answer modulo `10^9 + 7`.

Constraints:
- 1 <= n <= 5000
"""

# Python Solution
def knightDialer(n: int) -> int:
    MOD = 10**9 + 7

    # Define the possible moves for each digit
    moves = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }

    # Initialize dp array
    dp = [1] * 10  # At n=1, there is one way to start at each digit

    for _ in range(n - 1):
        new_dp = [0] * 10
        for digit in range(10):
            for move in moves[digit]:
                new_dp[move] = (new_dp[move] + dp[digit]) % MOD
        dp = new_dp

    return sum(dp) % MOD


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: n = 1
    print(knightDialer(1))  # Expected output: 10 (all digits are valid starting points)

    # Test Case 2: n = 2
    print(knightDialer(2))  # Expected output: 20 (each digit has specific valid moves)

    # Test Case 3: n = 3
    print(knightDialer(3))  # Expected output: 46

    # Test Case 4: n = 4
    print(knightDialer(4))  # Expected output: 104

    # Test Case 5: Large input
    print(knightDialer(5000))  # Expected output: Large number modulo 10^9 + 7


# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop runs for `n-1` iterations.
- The inner loop iterates over 10 digits, and for each digit, we process its possible moves (at most 8 moves).
- Therefore, the time complexity is O(n * 10 * 8) = O(n).

Space Complexity:
- We use two arrays (`dp` and `new_dp`) of size 10 to store the number of ways to reach each digit.
- The space complexity is O(10), which is constant space.

Overall:
Time Complexity: O(n)
Space Complexity: O(1)
"""

# Topic: Dynamic Programming