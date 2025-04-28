"""
LeetCode Problem #1970: Last Day Where You Can Still Cross

Problem Statement:
You are given an m x n binary matrix grid, where 0 represents a land cell and 1 represents a water cell.

You are also given an integer array cells, where cells[i] = [rowi, coli] represents that the cell at position 
(rowi, coli) will be filled with water on the (i + 1)th day. A cell is considered accessible if it is a land 
cell (0) and it is not filled with water.

You want to find the last day where it is possible to walk from the top row to the bottom row by only walking 
on land cells. You can move up, down, left, or right, and you cannot step outside the grid.

Return the last day where it is possible to walk from the top row to the bottom row.

Constraints:
- 2 <= row, col <= 2 * 10^4
- 1 <= rowi <= row
- 1 <= coli <= col
- row * col == cells.length
- cells is a permutation of the integers from 1 to row * col.

"""

from collections import deque

def canCross(row, col, grid):
    """
    Helper function to check if it's possible to cross the grid from the top row to the bottom row.
    Uses BFS to traverse the grid.
    """
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque()
    
    # Add all land cells in the top row to the queue
    for c in range(col):
        if grid[0][c] == 0:
            queue.append((0, c))
            grid[0][c] = -1  # Mark as visited
    
    while queue:
        r, c = queue.popleft()
        
        # If we reach the bottom row, return True
        if r == row - 1:
            return True
        
        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                queue.append((nr, nc))
                grid[nr][nc] = -1  # Mark as visited
    
    return False

def latestDayToCross(row, col, cells):
    """
    Main function to find the last day where it is possible to cross the grid.
    Uses binary search to optimize the solution.
    """
    left, right = 1, len(cells)
    
    while left <= right:
        mid = (left + right) // 2
        
        # Create the grid for the current day
        grid = [[0] * col for _ in range(row)]
        for i in range(mid):
            r, c = cells[i]
            grid[r - 1][c - 1] = 1  # Mark as water
        
        # Check if it's possible to cross
        if canCross(row, col, grid):
            left = mid + 1  # Try later days
        else:
            right = mid - 1  # Try earlier days
    
    return right

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    row1, col1, cells1 = 3, 3, [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 1], [3, 2]]
    print(latestDayToCross(row1, col1, cells1))  # Expected Output: 3

    # Test Case 2
    row2, col2, cells2 = 2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]]
    print(latestDayToCross(row2, col2, cells2))  # Expected Output: 2

    # Test Case 3
    row3, col3, cells3 = 3, 3, [[1, 1], [2, 2], [3, 3], [1, 2], [2, 1], [3, 2], [2, 3], [1, 3], [3, 1]]
    print(latestDayToCross(row3, col3, cells3))  # Expected Output: 3

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The binary search runs in O(log(row * col)) iterations.
   - For each iteration, we construct the grid in O(row * col) time.
   - The BFS traversal runs in O(row * col) time in the worst case.
   - Overall time complexity: O((row * col) * log(row * col)).

2. Space Complexity:
   - The grid requires O(row * col) space.
   - The BFS queue can hold up to O(row * col) elements in the worst case.
   - Overall space complexity: O(row * col).

Topic: Binary Search, Breadth-First Search (BFS)
"""