"""
LeetCode Problem #488: Zuma Game

Problem Statement:
You are playing a variation of the Zuma game. In this game, you have a row of balls on a table, 
each ball has a color represented by a character. You also have several balls in your hand, 
each ball also has a color. You need to insert the balls from your hand into the row such that 
the row becomes stable (no adjacent balls of the same color exist). 

Each time you insert a ball, if there are three or more consecutive balls of the same color, 
they will be removed from the row. After the removal, if there are more than three consecutive 
balls of the same color, they will also be removed. This process is repeated until the row becomes stable.

Return the minimum number of balls you have to insert to make the row stable. If you cannot make the row stable, return -1.

Example 1:
Input: board = "WRRBBW", hand = "RB"
Output: -1
Explanation: It is impossible to stabilize the row.

Example 2:
Input: board = "WWRRBBWW", hand = "WRBRW"
Output: 2
Explanation: To make the row stable, insert 'R' at index 2 and 'B' at index 4.

Example 3:
Input: board = "G", hand = "GGGGG"
Output: 2
Explanation: To make the row stable, insert 'G' at index 0 and index 1.

Constraints:
- 1 <= board.length <= 16
- 1 <= hand.length <= 5
- Both `board` and `hand` consist of uppercase English letters, representing colors.
- The answer is guaranteed to fit in a 32-bit signed integer.
"""

from collections import Counter

def findMinStep(board: str, hand: str) -> int:
    def remove_consecutive(board):
        i = 0
        while i < len(board):
            j = i
            while j < len(board) and board[j] == board[i]:
                j += 1
            if j - i >= 3:
                return remove_consecutive(board[:i] + board[j:])
            i += 1
        return board

    def dfs(board, hand_count):
        if not board:
            return 0
        if not any(hand_count.values()):
            return -1

        min_steps = float('inf')
        i = 0
        while i < len(board):
            j = i
            while j < len(board) and board[j] == board[i]:
                j += 1
            needed = max(0, 3 - (j - i))
            if hand_count[board[i]] >= needed:
                hand_count[board[i]] -= needed
                next_board = remove_consecutive(board[:i] + board[j:])
                steps = dfs(next_board, hand_count)
                if steps != -1:
                    min_steps = min(min_steps, steps + needed)
                hand_count[board[i]] += needed
            i = j

        return min_steps if min_steps != float('inf') else -1

    hand_count = Counter(hand)
    return dfs(board, hand_count)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    board = "WRRBBW"
    hand = "RB"
    print(findMinStep(board, hand))  # Output: -1

    # Test Case 2
    board = "WWRRBBWW"
    hand = "WRBRW"
    print(findMinStep(board, hand))  # Output: 2

    # Test Case 3
    board = "G"
    hand = "GGGGG"
    print(findMinStep(board, hand))  # Output: 2

    # Test Case 4
    board = "RBYYBBRRB"
    hand = "YRBGB"
    print(findMinStep(board, hand))  # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- The problem involves a depth-first search (DFS) approach with backtracking. 
- The number of states is limited by the length of the board (up to 16) and the number of balls in the hand (up to 5).
- In the worst case, the DFS explores all possible combinations of inserting balls, leading to exponential complexity: O(5^16).

Space Complexity:
- The space complexity is determined by the recursion stack and the storage for the board and hand count.
- The recursion stack can go up to the length of the board, so the space complexity is O(16).

Topic: Backtracking
"""