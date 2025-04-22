"""
LeetCode Question #892: Surface Area of 3D Shapes

Problem Statement:
You are given an n x n grid where each value represents the height of a tower of cubes. 
You need to calculate the total surface area of the 3D shape formed by these towers.

The surface area is calculated as follows:
- Each cube contributes 6 units of surface area.
- When two cubes are adjacent, they share a face, and the shared face is not counted in the surface area.
- The grid is surrounded by air, so the outer faces of the cubes are always counted.

Input:
- grid: A 2D list of integers where grid[i][j] represents the height of the tower at position (i, j).

Output:
- Return the total surface area of the 3D shape.

Constraints:
- 1 <= n <= 50
- 0 <= grid[i][j] <= 50
"""

def surfaceArea(grid):
    """
    Calculate the total surface area of the 3D shape formed by the grid.

    :param grid: List[List[int]] - 2D grid representing the heights of towers
    :return: int - Total surface area of the 3D shape
    """
    n = len(grid)
    total_area = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                # Add top and bottom surface areas
                total_area += 2
                
                # Add the four side surface areas
                # Check the adjacent cells (up, down, left, right)
                # If adjacent cell is out of bounds or has a smaller height, add the difference
                total_area += max(grid[i][j] - (grid[i-1][j] if i > 0 else 0), 0)  # Up
                total_area += max(grid[i][j] - (grid[i+1][j] if i < n-1 else 0), 0)  # Down
                total_area += max(grid[i][j] - (grid[i][j-1] if j > 0 else 0), 0)  # Left
                total_area += max(grid[i][j] - (grid[i][j+1] if j < n-1 else 0), 0)  # Right

    return total_area

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[2]]
    print(surfaceArea(grid1))  # Expected Output: 10

    # Test Case 2
    grid2 = [[1, 2], [3, 4]]
    print(surfaceArea(grid2))  # Expected Output: 34

    # Test Case 3
    grid3 = [[1, 0], [0, 2]]
    print(surfaceArea(grid3))  # Expected Output: 16

    # Test Case 4
    grid4 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(surfaceArea(grid4))  # Expected Output: 32

    # Test Case 5
    grid5 = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
    print(surfaceArea(grid5))  # Expected Output: 46

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through each cell in the grid, which has dimensions n x n.
- For each cell, we perform constant-time operations to calculate the surface area contributions.
- Therefore, the time complexity is O(n^2), where n is the size of the grid.

Space Complexity:
- The algorithm uses a constant amount of extra space for variables.
- No additional data structures are used, so the space complexity is O(1).

Topic: Arrays
"""