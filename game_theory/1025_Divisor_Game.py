"""
LeetCode Problem #1025: Divisor Game

Problem Statement:
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number `n` on the chalkboard. On each player's turn, that player makes a move consisting of:
- Choosing any `x` with `0 < x < n` and `n % x == 0`.
- Replacing the number `n` on the chalkboard with `n - x`.

Also, if a player cannot make a move, they lose the game.

Return `True` if and only if Alice wins the game, assuming both players play optimally.

Constraints:
- 1 <= n <= 1000
"""

def divisorGame(n: int) -> bool:
    """
    Determines if Alice wins the game given the initial number n.
    
    :param n: The initial number on the chalkboard.
    :return: True if Alice wins, False otherwise.
    """
    # Alice wins if and only if n is even
    return n % 2 == 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: n = 2
    # Alice can choose x = 1, leaving n = 1 for Bob. Bob cannot make a move, so Alice wins.
    print(divisorGame(2))  # Expected output: True

    # Test Case 2: n = 3
    # Alice can only choose x = 1, leaving n = 2 for Bob. Bob can then choose x = 1, leaving n = 1 for Alice.
    # Alice cannot make a move, so Bob wins.
    print(divisorGame(3))  # Expected output: False

    # Test Case 3: n = 4
    # Alice can choose x = 1, leaving n = 3 for Bob. Bob cannot win optimally, so Alice wins.
    print(divisorGame(4))  # Expected output: True

    # Test Case 4: n = 1
    # Alice cannot make a move, so she loses.
    print(divisorGame(1))  # Expected output: False

    # Test Case 5: n = 10
    # Alice can choose x = 1, leaving n = 9 for Bob. Bob cannot win optimally, so Alice wins.
    print(divisorGame(10))  # Expected output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution is O(1) because the result is determined solely by checking if `n` is even or odd.

Space Complexity:
- The solution is O(1) because no additional space is used beyond a constant amount.

Topic: Game Theory
"""