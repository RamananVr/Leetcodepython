"""
LeetCode Question #2617: Minimum Number of Visited Cells in a Grid

Problem Statement:
You are given an m x n grid of integers where each cell has a value representing the maximum number of cells you can move in one step. 
You can move either horizontally or vertically, but you cannot move diagonally. You start at the top-left cell (0, 0) and want to reach 
the bottom-right cell (m-1, n-1). Return the minimum number of cells you need to visit to reach the bottom-right cell, or -1 if it is 
impossible to reach the bottom-right cell.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 1000
- 1 <= grid[i][j] <= 1000
"""

from collections import deque

def minimumVisitedCells(grid):
    """
    Function to find the minimum number of cells visited to reach the bottom-right cell in the grid.
    :param grid: List[List[int]] - 2D grid of integers
    :return: int - Minimum number of cells visited or -1 if unreachable
    """
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    queue = deque([(0, 0, 1)])  # (row, col, steps)
    visited[0][0] = True

    while queue:
        row, col, steps = queue.popleft()

        # If we reach the bottom-right cell, return the number of steps
        if row == m - 1 and col == n - 1:
            return steps

        # Explore all possible moves within the range of grid[row][col]
        max_jump = grid[row][col]

        # Move horizontally
        for next_col in range(col + 1, min(col + max_jump + 1, n)):
            if not visited[row][next_col]:
                visited[row][next_col] = True
                queue.append((row, next_col, steps + 1))

        # Move vertically
        for next_row in range(row + 1, min(row + max_jump + 1, m)):
            if not visited[next_row][col]:
                visited[next_row][col] = True
                queue.append((next_row, col, steps + 1))

    # If we exhaust the queue without reaching the bottom-right cell, return -1
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [2, 3, 1],
        [1, 2, 2],
        [1, 1, 1]
    ]
    print(minimumVisitedCells(grid1))  # Expected Output: 4

    # Test Case 2
    grid2 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    print(minimumVisitedCells(grid2))  # Expected Output: -1

    # Test Case 3
    grid3 = [
        [3, 2, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    print(minimumVisitedCells(grid3))  # Expected Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- In the worst case, we may need to visit every cell in the grid once. For each cell, we explore up to `grid[row][col]` possible moves.
- Therefore, the time complexity is O(m * n), where m is the number of rows and n is the number of columns.

Space Complexity:
- We use a `visited` matrix of size m x n to track visited cells, which takes O(m * n) space.
- Additionally, the queue can hold up to O(m * n) elements in the worst case.
- Thus, the space complexity is O(m * n).

Topic: Breadth-First Search (BFS)
"""