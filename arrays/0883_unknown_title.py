"""
LeetCode Problem #883: Projection Area of 3D Shapes

Problem Statement:
You are given an `n x n` grid where we have placed some cubes. Each value `grid[i][j]` represents the number of cubes stacked at position `(i, j)`.

- A projection is like taking a shadow of the cubes when looking at the grid from a specific direction.
- We need to find the total projection area of the cubes.

There are three projections:
1. The "top" projection is the number of non-zero values in the grid.
2. The "front" projection is the sum of the maximum values in each row.
3. The "side" projection is the sum of the maximum values in each column.

Return the total projection area of the cubes.

Constraints:
- `n == grid.length == grid[i].length`
- `1 <= n <= 50`
- `0 <= grid[i][j] <= 50`
"""

def projectionArea(grid):
    """
    Calculate the total projection area of 3D shapes represented by the grid.

    :param grid: List[List[int]] - 2D grid representing the number of cubes stacked at each position
    :return: int - Total projection area
    """
    # Top projection: Count all non-zero values in the grid
    top_projection = sum(1 for row in grid for val in row if val > 0)
    
    # Front projection: Sum of the maximum values in each row
    front_projection = sum(max(row) for row in grid)
    
    # Side projection: Sum of the maximum values in each column
    side_projection = sum(max(col) for col in zip(*grid))
    
    # Total projection area
    return top_projection + front_projection + side_projection

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1, 2], [3, 4]]
    print(projectionArea(grid1))  # Expected Output: 17

    # Test Case 2
    grid2 = [[2]]
    print(projectionArea(grid2))  # Expected Output: 5

    # Test Case 3
    grid3 = [[1, 0], [0, 2]]
    print(projectionArea(grid3))  # Expected Output: 8

    # Test Case 4
    grid4 = [[0, 0], [0, 0]]
    print(projectionArea(grid4))  # Expected Output: 0

"""
Time Complexity Analysis:
- Top projection: O(n^2), as we iterate through all elements in the grid.
- Front projection: O(n^2), as we compute the maximum for each of the n rows.
- Side projection: O(n^2), as we compute the maximum for each of the n columns.
- Overall: O(n^2), since all operations are linear with respect to the number of elements in the grid.

Space Complexity Analysis:
- The space complexity is O(1), as we use a constant amount of extra space.

Topic: Arrays
"""