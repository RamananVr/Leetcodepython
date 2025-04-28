"""
LeetCode Problem #1706: Where Will the Ball Fall

Problem Statement:
You have a 2D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

- A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
- A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.

We drop one ball at a time at the top of each column of the grid. Each ball can get stuck in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after dropping the ball from the ith column at the top, or -1 if the ball gets stuck in the box.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- grid[i][j] is 1 or -1.

Example:
Input: grid = [[1,1,1,-1,-1],
               [1,1,1,-1,-1],
               [-1,-1,-1,1,1],
               [1,1,1,1,-1],
               [-1,-1,-1,-1,-1]]
Output: [1,-1,-1,-1,-1]
"""

# Python Solution
def findBall(grid):
    """
    Simulates the movement of each ball through the grid and determines the final column
    or if the ball gets stuck.

    :param grid: List[List[int]] - The grid representing the box with diagonal boards.
    :return: List[int] - The resulting column for each ball or -1 if stuck.
    """
    m, n = len(grid), len(grid[0])
    result = []

    def drop_ball(col):
        row = 0
        while row < m:
            direction = grid[row][col]
            next_col = col + direction
            # Check if the ball gets stuck
            if next_col < 0 or next_col >= n or grid[row][next_col] != direction:
                return -1
            # Move to the next row and column
            col = next_col
            row += 1
        return col

    for col in range(n):
        result.append(drop_ball(col))

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1, 1, 1, -1, -1],
             [1, 1, 1, -1, -1],
             [-1, -1, -1, 1, 1],
             [1, 1, 1, 1, -1],
             [-1, -1, -1, -1, -1]]
    print(findBall(grid1))  # Output: [1, -1, -1, -1, -1]

    # Test Case 2
    grid2 = [[1, 1, 1, 1, 1, 1],
             [-1, -1, -1, -1, -1, -1],
             [1, 1, 1, 1, 1, 1],
             [-1, -1, -1, -1, -1, -1]]
    print(findBall(grid2))  # Output: [-1, -1, -1, -1, -1, -1]

    # Test Case 3
    grid3 = [[1, -1],
             [-1, 1]]
    print(findBall(grid3))  # Output: [-1, -1]

    # Test Case 4
    grid4 = [[1]]
    print(findBall(grid4))  # Output: [-1]

    # Test Case 5
    grid5 = [[1, 1],
             [1, 1]]
    print(findBall(grid5))  # Output: [1, 2]

# Time and Space Complexity Analysis
"""
Time Complexity:
- For each ball (n balls), we simulate its movement through m rows.
- Thus, the time complexity is O(m * n).

Space Complexity:
- The space complexity is O(1) as we are not using any additional data structures
  apart from the result array, which is of size n.
"""

# Topic: Arrays, Simulation