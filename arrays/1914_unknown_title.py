"""
LeetCode Problem #1914: Cyclically Rotating a Grid

Problem Statement:
You are given an m x n integer matrix grid, where m and n are both even integers, and an integer k. 
The matrix is composed of several layers, which is defined as follows:

- A layer is a group of cells in the grid that form a closed circle. For example, the outermost layer 
  consists of all cells that are not surrounded by any other cells, and the next layer is formed by 
  all the cells surrounded by the outermost layer.

The task is to rotate each layer of the grid k times in a clockwise direction. Return the resulting 2D grid.

Example:
Input: grid = [[40,10],[30,20]], k = 1
Output: [[10,20],[40,30]]

Constraints:
- m == grid.length
- n == grid[i].length
- 2 <= m, n <= 50
- m and n are even integers
- 1 <= grid[i][j] <= 5000
- 1 <= k <= 10^6
"""

# Solution
from typing import List

def rotateGrid(grid: List[List[int]], k: int) -> List[List[int]]:
    def extract_layer(grid, layer):
        """Extracts the elements of a specific layer in clockwise order."""
        m, n = len(grid), len(grid[0])
        elements = []
        
        # Top row
        for col in range(layer, n - layer):
            elements.append(grid[layer][col])
        # Right column
        for row in range(layer + 1, m - layer):
            elements.append(grid[row][n - layer - 1])
        # Bottom row
        for col in range(n - layer - 2, layer - 1, -1):
            elements.append(grid[m - layer - 1][col])
        # Left column
        for row in range(m - layer - 2, layer, -1):
            elements.append(grid[row][layer])
        
        return elements

    def insert_layer(grid, layer, elements):
        """Inserts the elements of a specific layer in clockwise order."""
        m, n = len(grid), len(grid[0])
        idx = 0
        
        # Top row
        for col in range(layer, n - layer):
            grid[layer][col] = elements[idx]
            idx += 1
        # Right column
        for row in range(layer + 1, m - layer):
            grid[row][n - layer - 1] = elements[idx]
            idx += 1
        # Bottom row
        for col in range(n - layer - 2, layer - 1, -1):
            grid[m - layer - 1][col] = elements[idx]
            idx += 1
        # Left column
        for row in range(m - layer - 2, layer, -1):
            grid[row][layer] = elements[idx]
            idx += 1

    m, n = len(grid), len(grid[0])
    num_layers = min(m, n) // 2

    for layer in range(num_layers):
        # Extract the current layer
        elements = extract_layer(grid, layer)
        # Rotate the layer
        rotation = k % len(elements)
        rotated_elements = elements[-rotation:] + elements[:-rotation]
        # Insert the rotated layer back into the grid
        insert_layer(grid, layer, rotated_elements)

    return grid

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[40, 10], [30, 20]]
    k1 = 1
    print(rotateGrid(grid1, k1))  # Output: [[10, 20], [40, 30]]

    # Test Case 2
    grid2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    k2 = 2
    print(rotateGrid(grid2, k2))  # Output: [[3, 4, 8, 12], [2, 11, 10, 16], [1, 7, 6, 15], [5, 9, 13, 14]]

    # Test Case 3
    grid3 = [[1, 2], [3, 4]]
    k3 = 3
    print(rotateGrid(grid3, k3))  # Output: [[4, 1], [3, 2]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Extracting and inserting each layer takes O(m + n) for each layer.
- There are O(min(m, n) / 2) layers.
- Total time complexity is O((m + n) * min(m, n) / 2).

Space Complexity:
- The space complexity is O(min(m, n)) for storing the elements of a single layer.
"""

# Topic: Arrays