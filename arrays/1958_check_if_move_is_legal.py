"""
LeetCode Question #1958: Check if Move is Legal

Problem Statement:
You are given a `board` of size `n x n` representing the current state of a game board, where:
- `board[i][j]` is either `'B'` (a black piece), `'W'` (a white piece), or `'.'` (an empty square).
- You are also given two integers `rMove` and `cMove` representing the row and column of a square on the board that is empty (`board[rMove][cMove] == '.'`).

Your task is to determine if placing a piece of the opposite color at `board[rMove][cMove]` is a legal move. A move is legal if:
1. The piece placed at `board[rMove][cMove]` forms a straight line (horizontal, vertical, or diagonal) with at least one piece of the same color.
2. Between the newly placed piece and the other pieces of the same color, there are one or more pieces of the opposite color.

Return `True` if the move is legal, otherwise return `False`.

Constraints:
- `n == board.length == board[i].length`
- `4 <= n <= 500`
- `board[i][j]` is either `'B'`, `'W'`, or `'.'`.
- `0 <= rMove, cMove < n`
- `board[rMove][cMove] == '.'`

"""

def checkMove(board, rMove, cMove, color):
    """
    Determines if placing a piece of the given color at (rMove, cMove) is a legal move.

    :param board: List[List[str]] - The game board.
    :param rMove: int - Row index of the move.
    :param cMove: int - Column index of the move.
    :param color: str - The color of the piece to place ('B' or 'W').
    :return: bool - True if the move is legal, False otherwise.
    """
    n = len(board)
    directions = [
        (-1, 0), (1, 0),  # Vertical
        (0, -1), (0, 1),  # Horizontal
        (-1, -1), (1, 1),  # Diagonal \
        (-1, 1), (1, -1)   # Diagonal /
    ]
    
    opposite_color = 'B' if color == 'W' else 'W'
    
    for dr, dc in directions:
        i, j = rMove + dr, cMove + dc
        count_opposite = 0
        
        # Traverse in the current direction
        while 0 <= i < n and 0 <= j < n and board[i][j] == opposite_color:
            count_opposite += 1
            i += dr
            j += dc
        
        # Check if the line ends with a piece of the same color
        if count_opposite > 0 and 0 <= i < n and 0 <= j < n and board[i][j] == color:
            return True
    
    return False

# Example Test Cases
if __name__ == "__main__":
    board1 = [
        ['.', '.', '.', 'B', '.', '.', '.'],
        ['.', '.', '.', 'W', '.', '.', '.'],
        ['.', '.', '.', 'W', '.', '.', '.'],
        ['.', '.', '.', 'W', '.', '.', '.'],
        ['.', '.', '.', 'B', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.']
    ]
    rMove1, cMove1, color1 = 3, 3, 'B'
    print(checkMove(board1, rMove1, cMove1, color1))  # Output: True

    board2 = [
        ['.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.']
    ]
    rMove2, cMove2, color2 = 3, 3, 'B'
    print(checkMove(board2, rMove2, cMove2, color2))  # Output: False

    board3 = [
        ['B', 'W', 'B', '.', '.', '.', '.'],
        ['W', 'W', 'W', '.', '.', '.', '.'],
        ['B', 'W', 'B', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.']
    ]
    rMove3, cMove3, color3 = 3, 0, 'W'
    print(checkMove(board3, rMove3, cMove3, color3))  # Output: False

# Time and Space Complexity Analysis
# Time Complexity: O(n), where n is the size of the board. For each direction, we traverse the board in a straight line.
# Space Complexity: O(1), as we use a constant amount of extra space.

# Topic: Arrays