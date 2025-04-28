"""
LeetCode Question #2123: Minimum Operations to Remove Adjacent Ones in Matrix

Problem Statement:
You are given a binary matrix `grid` of size `m x n`. In one operation, you can choose any two adjacent cells and remove them if they both contain `1`. Adjacent cells are those that share a side (left, right, top, or bottom).

Return the minimum number of operations required to remove all `1`s from the matrix.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `grid[i][j]` is either `0` or `1`.

"""

# Solution
from collections import deque

def minOperations(grid):
    """
    Calculate the minimum number of operations to remove all adjacent ones in the matrix.

    :param grid: List[List[int]] - Binary matrix
    :return: int - Minimum number of operations
    """
    m, n = len(grid), len(grid[0])
    
    # Helper function to check if a cell is valid and contains a 1
    def is_valid(x, y):
        return 0 <= x < m and 0 <= y < n and grid[x][y] == 1
    
    # Directions for adjacent cells (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS to find connected components of 1s
    def bfs(x, y):
        queue = deque([(x, y)])
        grid[x][y] = 0  # Mark as visited
        size = 0
        
        while queue:
            cx, cy = queue.popleft()
            size += 1
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if is_valid(nx, ny):
                    grid[nx][ny] = 0  # Mark as visited
                    queue.append((nx, ny))
        
        return size
    
    # Count the number of connected components and their sizes
    components = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                components.append(bfs(i, j))
    
    # Calculate the minimum number of operations
    operations = 0
    for size in components:
        operations += (size + 1) // 2  # Each operation removes 2 adjacent ones
    
    return operations


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    print(minOperations(grid1))  # Expected Output: 2

    # Test Case 2
    grid2 = [
        [1, 0, 0],
        [0, 1, 1],
        [0, 1, 0]
    ]
    print(minOperations(grid2))  # Expected Output: 2

    # Test Case 3
    grid3 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    print(minOperations(grid3))  # Expected Output: 5

    # Test Case 4
    grid4 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    print(minOperations(grid4))  # Expected Output: 0


"""
Time and Space Complexity Analysis:

Time Complexity:
- The BFS function visits each cell in the matrix at most once. Therefore, the time complexity is O(m * n), where m is the number of rows and n is the number of columns.

Space Complexity:
- The space complexity is O(m * n) due to the queue used in BFS and the storage for the grid.

Topic: Graphs (BFS)
"""