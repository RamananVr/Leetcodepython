"""
LeetCode Problem #959: Regions Cut By Slashes

Problem Statement:
An n x n grid is composed of 1 x 1 squares. Each square is either empty (' ') or contains a slash ('/' or '\').
These slashes divide the square into regions. A region is a connected group of 1 x 1 squares.

You are tasked to return the number of regions formed in the grid.

Input:
- grid: List[str] - A list of strings representing the n x n grid.

Output:
- int - The number of regions formed in the grid.

Constraints:
- 1 <= n <= 30
- grid[i].length == n
- grid[i][j] is either '/', '\', or ' '.
"""

# Solution
def regionsBySlashes(grid):
    def dfs(x, y):
        if x < 0 or x >= size or y < 0 or y >= size or visited[x][y]:
            return
        visited[x][y] = True
        for dx, dy in directions:
            dfs(x + dx, y + dy)

    n = len(grid)
    size = n * 3  # Expand the grid to 3x3 for finer resolution
    visited = [[False] * size for _ in range(size)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    # Expand the grid
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '/':
                visited[i * 3][j * 3 + 2] = True
                visited[i * 3 + 1][j * 3 + 1] = True
                visited[i * 3 + 2][j * 3] = True
            elif grid[i][j] == '\\':
                visited[i * 3][j * 3] = True
                visited[i * 3 + 1][j * 3 + 1] = True
                visited[i * 3 + 2][j * 3 + 2] = True

    # Count regions using DFS
    regions = 0
    for i in range(size):
        for j in range(size):
            if not visited[i][j]:
                dfs(i, j)
                regions += 1

    return regions

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        " /",
        "/ "
    ]
    print(regionsBySlashes(grid1))  # Output: 2

    # Test Case 2
    grid2 = [
        " /",
        "  "
    ]
    print(regionsBySlashes(grid2))  # Output: 1

    # Test Case 3
    grid3 = [
        "\\/",
        "/\\"
    ]
    print(regionsBySlashes(grid3))  # Output: 4

    # Test Case 4
    grid4 = [
        "/\\",
        "\\/"
    ]
    print(regionsBySlashes(grid4))  # Output: 5

    # Test Case 5
    grid5 = [
        "//",
        "/ "
    ]
    print(regionsBySlashes(grid5))  # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- The grid is expanded to a size of n * 3 x n * 3.
- DFS is performed on each cell of the expanded grid.
- In the worst case, we visit all cells in the expanded grid once.
- Therefore, the time complexity is O((n * 3)^2) = O(9 * n^2) = O(n^2).

Space Complexity:
- The space complexity is dominated by the `visited` array, which is of size (n * 3) x (n * 3).
- Therefore, the space complexity is O((n * 3)^2) = O(9 * n^2) = O(n^2).

Topic: Graphs
"""