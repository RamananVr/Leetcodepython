"""
LeetCode Question #723: Candy Crush

Problem Statement:
This problem is a simplified version of the Candy Crush game. Given an m x n board, where each cell contains an integer representing a candy type, the goal is to repeatedly "crush" candies until no more candies can be crushed. A candy is crushed if it forms a horizontal or vertical line of at least three candies of the same type. After crushing candies, the board is updated by dropping candies above the crushed ones to fill the empty spaces. Return the final state of the board after no more candies can be crushed.

Rules:
1. If multiple candies are crushed simultaneously, all of them are removed before any candies drop.
2. After candies drop, the process repeats until no more candies can be crushed.

Input:
- board: List[List[int]] (m x n grid of integers)

Output:
- List[List[int]] (final state of the board)

Constraints:
- m == len(board)
- n == len(board[i])
- 1 <= m, n <= 50
- -1000 <= board[i][j] <= 1000
"""

def candyCrush(board):
    def mark_candies_to_crush():
        """Mark candies to be crushed."""
        to_crush = set()
        rows, cols = len(board), len(board[0])
        
        # Check horizontal candies
        for r in range(rows):
            for c in range(cols - 2):
                if abs(board[r][c]) == abs(board[r][c + 1]) == abs(board[r][c + 2]) != 0:
                    to_crush.update([(r, c), (r, c + 1), (r, c + 2)])
        
        # Check vertical candies
        for c in range(cols):
            for r in range(rows - 2):
                if abs(board[r][c]) == abs(board[r + 1][c]) == abs(board[r + 2][c]) != 0:
                    to_crush.update([(r, c), (r + 1, c), (r + 2, c)])
        
        return to_crush

    def crush_candies(to_crush):
        """Crush candies by setting them to 0."""
        for r, c in to_crush:
            board[r][c] = 0

    def drop_candies():
        """Drop candies to fill empty spaces."""
        rows, cols = len(board), len(board[0])
        for c in range(cols):
            # Collect all non-zero candies in the column
            stack = [board[r][c] for r in range(rows) if board[r][c] != 0]
            # Fill the column from bottom to top
            for r in range(rows - 1, -1, -1):
                board[r][c] = stack.pop() if stack else 0

    while True:
        # Step 1: Mark candies to crush
        to_crush = mark_candies_to_crush()
        if not to_crush:
            break  # No more candies to crush
        
        # Step 2: Crush candies
        crush_candies(to_crush)
        
        # Step 3: Drop candies
        drop_candies()
    
    return board

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    board1 = [
        [110, 5, 112, 113, 114],
        [210, 211, 5, 213, 214],
        [310, 311, 3, 313, 314],
        [410, 411, 412, 5, 414],
        [5, 1, 512, 3, 3],
        [610, 4, 1, 613, 614],
        [710, 1, 2, 713, 714],
        [810, 1, 2, 1, 1],
        [1, 1, 2, 2, 2],
        [4, 1, 4, 4, 1014]
    ]
    print("Final Board State for Test Case 1:")
    print(candyCrush(board1))

    # Test Case 2
    board2 = [
        [1, 1, 1],
        [2, 2, 2],
        [3, 3, 3]
    ]
    print("Final Board State for Test Case 2:")
    print(candyCrush(board2))

"""
Time and Space Complexity Analysis:

Time Complexity:
- Marking candies to crush: O(m * n), where m is the number of rows and n is the number of columns.
- Crushing candies: O(k), where k is the number of candies to crush (bounded by m * n).
- Dropping candies: O(m * n), as we iterate through each column to drop candies.
- The process repeats until no more candies can be crushed. In the worst case, this could happen O(m * n) times.
- Overall time complexity: O((m * n)^2).

Space Complexity:
- The space complexity is O(m * n) due to the set used to store candies to crush.

Topic: Arrays
"""