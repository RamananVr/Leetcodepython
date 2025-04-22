"""
LeetCode Question #361: Bomb Enemy

Problem Statement:
Given a 2D grid, each cell is either a wall 'W', an enemy 'E', or empty '0' (the number zero), return the maximum enemies you can kill using one bomb. 
The bomb kills all the enemies in the same row and column from the planted cell, but cannot go through walls.

You can only place the bomb in an empty cell.

Example:
Input: grid = [
    ["0","E","0","0"],
    ["E","0","W","E"],
    ["0","E","0","0"]
]
Output: 3
Explanation: Placing a bomb at (1,1) kills 3 enemies.

Constraints:
- The grid is a 2D array of characters with dimensions m x n.
- 1 <= m, n <= 500
- Each cell in the grid is either 'W', 'E', or '0'.
"""

def maxKilledEnemies(grid):
    """
    Function to calculate the maximum number of enemies that can be killed using one bomb.
    :param grid: List[List[str]] - 2D grid containing 'W', 'E', and '0'.
    :return: int - Maximum number of enemies killed.
    """
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    max_kills = 0

    # Initialize arrays to store the number of enemies in rows and columns
    row_hits = 0
    col_hits = [0] * n

    for i in range(m):
        for j in range(n):
            # Calculate row_hits if we are at the start of a row or after a wall
            if j == 0 or grid[i][j - 1] == 'W':
                row_hits = 0
                for k in range(j, n):
                    if grid[i][k] == 'W':
                        break
                    elif grid[i][k] == 'E':
                        row_hits += 1

            # Calculate col_hits if we are at the start of a column or after a wall
            if i == 0 or grid[i - 1][j] == 'W':
                col_hits[j] = 0
                for k in range(i, m):
                    if grid[k][j] == 'W':
                        break
                    elif grid[k][j] == 'E':
                        col_hits[j] += 1

            # If the cell is empty, calculate the total kills
            if grid[i][j] == '0':
                max_kills = max(max_kills, row_hits + col_hits[j])

    return max_kills

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        ["0", "E", "0", "0"],
        ["E", "0", "W", "E"],
        ["0", "E", "0", "0"]
    ]
    print(maxKilledEnemies(grid1))  # Output: 3

    # Test Case 2
    grid2 = [
        ["0", "E", "W", "0"],
        ["E", "0", "E", "E"],
        ["0", "W", "0", "E"]
    ]
    print(maxKilledEnemies(grid2))  # Output: 2

    # Test Case 3
    grid3 = [
        ["W", "W", "W"],
        ["W", "0", "W"],
        ["W", "W", "W"]
    ]
    print(maxKilledEnemies(grid3))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through each cell in the grid once (O(m * n)).
- For each cell, it calculates row_hits and col_hits by scanning the row and column, but only when necessary (O(m + n) in total for all cells).
- Thus, the overall time complexity is O(m * n).

Space Complexity:
- The algorithm uses O(n) space for the col_hits array.
- No additional space is used apart from a few variables.
- Thus, the space complexity is O(n).

Topic: Arrays
"""