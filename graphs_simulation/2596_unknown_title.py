"""
LeetCode Problem #2596: Check Knight Tour Configuration

Problem Statement:
An n x n grid is a valid knight tour configuration if the knight can visit every cell on the grid exactly once.

The knight moves in an "L" shape: two cells in one direction and one cell in a perpendicular direction, or one cell in one direction and two cells in a perpendicular direction.

Given a 2D array `grid` of size n x n where `grid[i][j]` is the step number of the knight at cell (i, j), return true if the grid is a valid knight tour configuration. Otherwise, return false.

Constraints:
- n == grid.length == grid[i].length
- 3 <= n <= 100
- 0 <= grid[i][j] < n * n
- All the integers in grid are unique.
"""

def checkValidGrid(grid):
    """
    Function to check if the given grid represents a valid knight tour configuration.

    :param grid: List[List[int]] - 2D grid representing the knight's tour
    :return: bool - True if the grid is a valid knight tour, False otherwise
    """
    n = len(grid)
    
    # Directions for knight moves
    directions = [
        (-2, -1), (-1, -2), (1, -2), (2, -1),
        (2, 1), (1, 2), (-1, 2), (-2, 1)
    ]
    
    # Find the position of each step in the grid
    positions = [None] * (n * n)
    for i in range(n):
        for j in range(n):
            positions[grid[i][j]] = (i, j)
    
    # Check if the first step starts at the top-left corner
    if positions[0] != (0, 0):
        return False
    
    # Validate each step
    for step in range(1, n * n):
        prev_x, prev_y = positions[step - 1]
        curr_x, curr_y = positions[step]
        if (curr_x - prev_x, curr_y - prev_y) not in directions:
            return False
    
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Valid knight tour
    grid1 = [
        [0, 17, 4],
        [15, 2, 19],
        [6, 13, 8]
    ]
    print(checkValidGrid(grid1))  # Output: True

    # Test Case 2: Invalid knight tour (does not start at top-left corner)
    grid2 = [
        [1, 17, 4],
        [15, 2, 19],
        [6, 13, 8]
    ]
    print(checkValidGrid(grid2))  # Output: False

    # Test Case 3: Invalid knight tour (invalid knight move)
    grid3 = [
        [0, 17, 4],
        [15, 2, 19],
        [6, 13, 7]
    ]
    print(checkValidGrid(grid3))  # Output: False

"""
Time Complexity Analysis:
- Finding the positions of all steps: O(n^2), where n is the size of the grid.
- Validating each step: O(n^2), as there are n^2 steps to validate.
- Overall time complexity: O(n^2).

Space Complexity Analysis:
- The `positions` array stores n^2 elements, so the space complexity is O(n^2).
- Overall space complexity: O(n^2).

Topic: Graphs, Simulation
"""