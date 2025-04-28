"""
LeetCode Problem #1391: Check if There is a Valid Path in a Grid

Problem Statement:
You are given an m x n grid. Each cell of the grid has a value representing a type of street. 
The street types are as follows:

1. Horizontal street connecting the left and right cells.
2. Vertical street connecting the top and bottom cells.
3. Corner street connecting the left and bottom cells.
4. Corner street connecting the right and bottom cells.
5. Corner street connecting the left and top cells.
6. Corner street connecting the right and top cells.

You start at the top-left corner of the grid and you need to reach the bottom-right corner. 
You can move to a neighboring cell if and only if there is a valid street connection between the two cells. 

Return true if there is a valid path from the top-left corner to the bottom-right corner.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is in the range [1, 6].

"""

from collections import deque

def hasValidPath(grid):
    """
    Determines if there is a valid path from the top-left corner to the bottom-right corner in the grid.

    :param grid: List[List[int]] - The grid representing the streets.
    :return: bool - True if there is a valid path, False otherwise.
    """
    m, n = len(grid), len(grid[0])
    
    # Directions for each street type
    directions = {
        1: [(0, -1), (0, 1)],  # Left, Right
        2: [(-1, 0), (1, 0)],  # Up, Down
        3: [(0, -1), (1, 0)],  # Left, Down
        4: [(0, 1), (1, 0)],   # Right, Down
        5: [(0, -1), (-1, 0)], # Left, Up
        6: [(0, 1), (-1, 0)]   # Right, Up
    }
    
    # Check if two cells are connected
    def is_connected(x1, y1, x2, y2):
        if not (0 <= x2 < m and 0 <= y2 < n):
            return False
        for dx, dy in directions[grid[x1][y1]]:
            if x1 + dx == x2 and y1 + dy == y2:
                for dx2, dy2 in directions[grid[x2][y2]]:
                    if x2 + dx2 == x1 and y2 + dy2 == y1:
                        return True
        return False
    
    # BFS to check for a valid path
    queue = deque([(0, 0)])
    visited = set()
    visited.add((0, 0))
    
    while queue:
        x, y = queue.popleft()
        if (x, y) == (m - 1, n - 1):
            return True
        for dx, dy in directions[grid[x][y]]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and is_connected(x, y, nx, ny):
                visited.add((nx, ny))
                queue.append((nx, ny))
    
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[2,4,3],[6,5,2]]
    print(hasValidPath(grid1))  # Output: True

    # Test Case 2
    grid2 = [[1,2,1],[1,2,1]]
    print(hasValidPath(grid2))  # Output: False

    # Test Case 3
    grid3 = [[1,1,2]]
    print(hasValidPath(grid3))  # Output: False

    # Test Case 4
    grid4 = [[1,1,1,1,1,1,3]]
    print(hasValidPath(grid4))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each cell is visited at most once during the BFS traversal.
- For each cell, we check its neighbors, which is a constant operation (at most 4 neighbors).
- Therefore, the time complexity is O(m * n), where m is the number of rows and n is the number of columns.

Space Complexity:
- The space complexity is O(m * n) due to the `visited` set and the BFS queue, which can store up to m * n elements in the worst case.

Topic: Graphs, Breadth-First Search (BFS)
"""