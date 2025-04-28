"""
LeetCode Problem #2038: Remove Colored Pieces if Both Neighbors are the Same Color

Problem Statement:
Alice and Bob are playing a game where there is a row of n colored pieces arranged in a line. Each piece is colored either 'A' or 'B'. 
Alice and Bob take turns removing pieces from the row. Alice can only remove a piece colored 'A' if both its neighbors are also colored 'A'. 
Similarly, Bob can only remove a piece colored 'B' if both its neighbors are also colored 'B'. Alice goes first.

Given a string colors of length n where colors[i] is either 'A' or 'B', return true if Alice wins the game, or false if Bob wins.

Assume both players play optimally.

Constraints:
- 1 <= colors.length <= 10^5
- colors consists of only the letters 'A' and 'B'.

"""

def winnerOfGame(colors: str) -> bool:
    """
    Determines if Alice wins the game given the string of colors.

    :param colors: A string consisting of 'A' and 'B' representing the row of pieces.
    :return: True if Alice wins, False if Bob wins.
    """
    # Count the number of removable 'A' and 'B' pieces
    alice_moves = 0
    bob_moves = 0

    # Traverse the string and count consecutive 'A's and 'B's
    n = len(colors)
    for i in range(1, n - 1):
        if colors[i - 1] == colors[i] == colors[i + 1]:
            if colors[i] == 'A':
                alice_moves += 1
            elif colors[i] == 'B':
                bob_moves += 1

    # Alice wins if she has more moves than Bob
    return alice_moves > bob_moves


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    colors = "AAABABB"
    print(winnerOfGame(colors))  # Output: True (Alice wins)

    # Test Case 2
    colors = "AA"
    print(winnerOfGame(colors))  # Output: False (Bob wins)

    # Test Case 3
    colors = "ABBBBBBBAAA"
    print(winnerOfGame(colors))  # Output: False (Bob wins)

    # Test Case 4
    colors = "AAAABBBB"
    print(winnerOfGame(colors))  # Output: False (Bob wins)

    # Test Case 5
    colors = "AAAAAA"
    print(winnerOfGame(colors))  # Output: True (Alice wins)


"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution involves a single traversal of the string `colors`, which has a length of n.
- Therefore, the time complexity is O(n).

Space Complexity:
- The solution uses a constant amount of extra space for variables like `alice_moves` and `bob_moves`.
- Therefore, the space complexity is O(1).

Topic: String
"""