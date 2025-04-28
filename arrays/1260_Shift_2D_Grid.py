"""
LeetCode Problem #1260: Shift 2D Grid

Problem Statement:
Given a 2D grid of size `m x n` and an integer `k`, you need to shift the grid `k` times. 
In one shift operation:
1. Element at grid[i][j] moves to grid[i][j + 1].
2. Element at grid[i][n - 1] moves to grid[i + 1][0].
3. Element at grid[m - 1][n - 1] moves to grid[0][0].

Return the 2D grid after applying `k` shifts.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m <= 50`
- `1 <= n <= 50`
- `-1000 <= grid[i][j] <= 1000`
- `0 <= k <= 100`

Example:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
"""

# Clean and Correct Python Solution
from typing import List

def shiftGrid(grid: List[List[int]], k: int) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    total_elements = m * n

    # Reduce k to avoid unnecessary full rotations
    k %= total_elements

    # Flatten the grid into a 1D list
    flat_grid = [grid[i][j] for i in range(m) for j in range(n)]

    # Perform the shift on the 1D list
    shifted_flat_grid = flat_grid[-k:] + flat_grid[:-k]

    # Convert the 1D list back into a 2D grid
    new_grid = [[shifted_flat_grid[i * n + j] for j in range(n)] for i in range(m)]

    return new_grid

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k1 = 1
    print(shiftGrid(grid1, k1))  # Output: [[9, 1, 2], [3, 4, 5], [6, 7, 8]]

    # Test Case 2
    grid2 = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
    k2 = 4
    print(shiftGrid(grid2, k2))  # Output: [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]]

    # Test Case 3
    grid3 = [[1]]
    k3 = 100
    print(shiftGrid(grid3, k3))  # Output: [[1]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Flattening the grid into a 1D list takes O(m * n).
- Shifting the 1D list takes O(m * n) (slicing and concatenation).
- Converting the 1D list back into a 2D grid takes O(m * n).
- Overall: O(m * n).

Space Complexity:
- The flattened 1D list and the shifted 1D list both take O(m * n) space.
- The new 2D grid takes O(m * n) space.
- Overall: O(m * n).
"""

# Topic: Arrays