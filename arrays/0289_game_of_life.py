"""
LeetCode Question #289: Game of Life

Problem Statement:
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules:

1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 25
- board[i][j] is 0 or 1

Follow-up:
- Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
"""

# Solution
def gameOfLife(board):
    """
    Updates the board in-place to represent the next state of the Game of Life.
    
    :param board: List[List[int]] - The current state of the board
    :return: None - The board is updated in-place
    """
    rows, cols = len(board), len(board[0])
    
    # Directions for the 8 neighbors
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    # Iterate through each cell
    for row in range(rows):
        for col in range(cols):
            live_neighbors = 0
            
            # Count live neighbors
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < rows and 0 <= c < cols and abs(board[r][c]) == 1:
                    live_neighbors += 1
            
            # Apply the rules
            if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                # Mark as dead in the next state
                board[row][col] = -1
            elif board[row][col] == 0 and live_neighbors == 3:
                # Mark as live in the next state
                board[row][col] = 2
    
    # Update the board to the next state
    for row in range(rows):
        for col in range(cols):
            if board[row][col] > 0:
                board[row][col] = 1
            else:
                board[row][col] = 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    board1 = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    gameOfLife(board1)
    print("Test Case 1 Output:")
    print(board1)  # Expected: [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

    # Test Case 2
    board2 = [
        [1, 1],
        [1, 0]
    ]
    gameOfLife(board2)
    print("Test Case 2 Output:")
    print(board2)  # Expected: [[1, 1], [1, 1]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- For each cell in the board, we check its 8 neighbors. This results in O(m * n) operations, where m is the number of rows and n is the number of columns.

Space Complexity:
- The solution is in-place, so no additional space is used apart from a few variables. Thus, the space complexity is O(1).
"""

# Topic: Arrays