"""
LeetCode Problem #1034: Coloring A Border

Problem Statement:
You are given an m x n integer matrix grid, four integers r0, c0, color, and a starting cell (r0, c0) 
that belongs to the connected component of the same color. The connected component of the starting cell 
is the set of cells in grid with the same color that can be reached directly or indirectly from the starting 
cell.

You must color the border of the connected component with the given color and return the resulting grid.

The border of a connected component is all the cells in the connected component that are either:
- On the boundary of the grid, or
- Neighboring a cell that is not in the connected component.

Example:
Input: grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
Output: [[2,2,2],[2,1,2],[2,2,2]]

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- 1 <= grid[i][j], color <= 1000
- r0 is a valid cell in grid.
"""

# Python Solution
from collections import deque

def colorBorder(grid, r0, c0, color):
    def is_border(x, y):
        # Check if the cell is on the border of the connected component
        if x == 0 or x == m - 1 or y == 0 or y == n - 1:
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < m and 0 <= ny < n) or grid[nx][ny] != original_color:
                return True
        return False

    m, n = len(grid), len(grid[0])
    original_color = grid[r0][c0]
    visited = [[False] * n for _ in range(m)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    component = []

    # BFS to find all cells in the connected component
    queue = deque([(r0, c0)])
    visited[r0][c0] = True
    while queue:
        x, y = queue.popleft()
        component.append((x, y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == original_color:
                visited[nx][ny] = True
                queue.append((nx, ny))

    # Color the border cells
    for x, y in component:
        if is_border(x, y):
            grid[x][y] = color

    return grid

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1,1,1],[1,1,1],[1,1,1]]
    r0_1, c0_1, color1 = 1, 1, 2
    print(colorBorder(grid1, r0_1, c0_1, color1))  # Expected: [[2,2,2],[2,1,2],[2,2,2]]

    # Test Case 2
    grid2 = [[1,2,2],[2,3,2],[2,2,2]]
    r0_2, c0_2, color2 = 1, 1, 4
    print(colorBorder(grid2, r0_2, c0_2, color2))  # Expected: [[1,4,4],[4,3,4],[4,4,4]]

    # Test Case 3
    grid3 = [[1,1,1],[1,1,1],[1,1,1]]
    r0_3, c0_3, color3 = 0, 0, 3
    print(colorBorder(grid3, r0_3, c0_3, color3))  # Expected: [[3,3,3],[3,1,3],[3,3,3]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The BFS traversal visits each cell in the connected component once, and the `is_border` function checks 
  the neighbors of each cell. Therefore, the time complexity is O(m * n), where m is the number of rows 
  and n is the number of columns.

Space Complexity:
- The space complexity is O(m * n) due to the `visited` matrix and the `component` list, which store 
  information about the connected component.

Overall: Time Complexity = O(m * n), Space Complexity = O(m * n)
"""

# Topic: Graph Traversal (BFS)