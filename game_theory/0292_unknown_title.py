"""
LeetCode Problem #292: Nim Game

Problem Statement:
You are playing the following Nim Game with your friend:
- Initially, there is a heap of stones on the table.
- You and your friend will alternate taking turns, and you go first.
- On each turn, a player can remove 1 to 3 stones from the heap.
- The player who removes the last stone wins.

Given `n`, the number of stones in the heap, return `true` if you can win the game assuming both players play optimally, otherwise return `false`.

Constraints:
- 1 <= n <= 2^31 - 1
"""

def canWinNim(n: int) -> bool:
    """
    Determines if the first player can win the Nim Game given `n` stones.

    :param n: Number of stones in the heap.
    :return: True if the first player can win, False otherwise.
    """
    return n % 4 != 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: n = 4
    # Explanation: If there are 4 stones, no matter how many stones you remove (1, 2, or 3),
    # your opponent can always remove the remaining stones to win. Hence, you cannot win.
    print(canWinNim(4))  # Expected output: False

    # Test Case 2: n = 1
    # Explanation: If there is 1 stone, you can remove it and win the game.
    print(canWinNim(1))  # Expected output: True

    # Test Case 3: n = 7
    # Explanation: If there are 7 stones, you can remove 3 stones, leaving 4 for your opponent.
    # Since 4 is a losing position, you can win.
    print(canWinNim(7))  # Expected output: True

    # Test Case 4: n = 8
    # Explanation: If there are 8 stones, no matter how many stones you remove (1, 2, or 3),
    # your opponent can always leave you with a multiple of 4 stones, ensuring their win.
    print(canWinNim(8))  # Expected output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution involves a single modulo operation, which is O(1).
- Therefore, the time complexity is O(1).

Space Complexity:
- The solution uses a constant amount of space, as no additional data structures are used.
- Therefore, the space complexity is O(1).
"""

# Topic: Game Theory