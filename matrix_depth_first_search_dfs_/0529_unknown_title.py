"""
LeetCode Problem #529: Minesweeper

Problem Statement:
You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

1. If a mine ('M') is revealed, then the game is over - change it to 'X'.
2. If an empty square ('E') with no adjacent mines is revealed, then change it to a revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
3. If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
4. Return the board when no more squares will be revealed.

Example 1:
Input: 
board = [['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'M', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E']]
click = [3, 0]
Output: 
[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Example 2:
Input: 
board = [['B', '1', 'E', '1', 'B'],
         ['B', '1', 'M', '1', 'B'],
         ['B', '1', '1', '1', 'B'],
         ['B', 'B', 'B', 'B', 'B']]
click = [1, 2]
Output: 
[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 50
- board[i][j] is either 'M', 'E', 'B', 'X', or a digit ('1' to '8').
- click.length == 2
- 0 <= click[0] < m
- 0 <= click[1] < n
"""

from typing import List

def updateBoard(board: List[List[str]], click: List[int]) -> List[List[str]]:
    def count_adjacent_mines(x, y):
        """Count the number of adjacent mines around a given cell."""
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'M':
                count += 1
        return count

    def dfs(x, y):
        """Perform DFS to reveal cells recursively."""
        if not (0 <= x < m and 0 <= y < n) or board[x][y] != 'E':
            return
        adjacent_mines = count_adjacent_mines(x, y)
        if adjacent_mines > 0:
            board[x][y] = str(adjacent_mines)
        else:
            board[x][y] = 'B'
            for dx, dy in directions:
                dfs(x + dx, y + dy)

    m, n = len(board), len(board[0])
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    x, y = click

    if board[x][y] == 'M':
        board[x][y] = 'X'
    else:
        dfs(x, y)

    return board

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    board1 = [['E', 'E', 'E', 'E', 'E'],
              ['E', 'E', 'M', 'E', 'E'],
              ['E', 'E', 'E', 'E', 'E'],
              ['E', 'E', 'E', 'E', 'E']]
    click1 = [3, 0]
    print(updateBoard(board1, click1))

    # Test Case 2
    board2 = [['B', '1', 'E', '1', 'B'],
              ['B', '1', 'M', '1', 'B'],
              ['B', '1', '1', '1', 'B'],
              ['B', 'B', 'B', 'B', 'B']]
    click2 = [1, 2]
    print(updateBoard(board2, click2))

"""
Time Complexity:
- The DFS function visits each cell at most once. In the worst case, we may visit all cells in the board.
- Therefore, the time complexity is O(m * n), where m is the number of rows and n is the number of columns.

Space Complexity:
- The space complexity is O(m * n) in the worst case due to the recursion stack in DFS.

Topic: Matrix, Depth-First Search (DFS)
"""