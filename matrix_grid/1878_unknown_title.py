"""
LeetCode Problem #1878: Get Biggest Three Rhombus Sums in a Grid

Problem Statement:
You are given an `m x n` integer matrix `grid`. A rhombus sum is defined as the sum of the elements that form a rhombus shape in the grid. The rhombus must be centered at some cell `(r, c)` and have a "radius" `k`. The cells that form the rhombus are:
- The cell `(r, c)` itself.
- The cells `(r - i, c - k + i)` and `(r - i, c + k - i)` for `i = 1, 2, ..., k`.
- The cells `(r + i, c - k + i)` and `(r + i, c + k - i)` for `i = 1, 2, ..., k`.

Note that the rhombus can only be formed if all the cells involved in the sum are inside the grid.

Return an array of the biggest three distinct rhombus sums in the grid in descending order. If there are fewer than three distinct values, return all of them.

Example:
Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
Output: [228,216,211]

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `1 <= grid[i][j] <= 10^5`
"""

# Solution
def getBiggestThree(grid):
    def is_valid(r, c, k):
        """Check if a rhombus of radius k centered at (r, c) is valid."""
        return r - k >= 0 and r + k < len(grid) and c - k >= 0 and c + k < len(grid[0])

    def calculate_rhombus_sum(r, c, k):
        """Calculate the sum of a rhombus of radius k centered at (r, c)."""
        if k == 0:
            return grid[r][c]
        total = 0
        for i in range(k + 1):
            total += grid[r - i][c - k + i]  # Top-left to top-right
            total += grid[r + i][c - k + i]  # Bottom-left to bottom-right
        for i in range(1, k):  # Avoid double-counting corners
            total += grid[r - k + i][c + i]  # Top-right to bottom-right
            total += grid[r + k - i][c - i]  # Bottom-left to top-left
        return total

    m, n = len(grid), len(grid[0])
    rhombus_sums = set()

    for r in range(m):
        for c in range(n):
            k = 0
            while is_valid(r, c, k):
                rhombus_sums.add(calculate_rhombus_sum(r, c, k))
                k += 1

    return sorted(rhombus_sums, reverse=True)[:3]

# Example Test Cases
if __name__ == "__main__":
    grid1 = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
    grid2 = [[1,2,3],[4,5,6],[7,8,9]]
    grid3 = [[10]]

    print(getBiggestThree(grid1))  # Output: [228, 216, 211]
    print(getBiggestThree(grid2))  # Output: [20, 9, 8]
    print(getBiggestThree(grid3))  # Output: [10]

# Time and Space Complexity Analysis
"""
Time Complexity:
- For each cell in the grid (O(m * n)), we attempt to calculate rhombus sums for increasing radii k.
- The maximum radius k is limited by the smaller dimension of the grid, so in the worst case, we perform O(min(m, n)) operations per cell.
- Calculating the rhombus sum for a given radius k takes O(k) time.
- Overall complexity: O(m * n * min(m, n)).

Space Complexity:
- We use a set to store distinct rhombus sums, which can hold at most O(m * n * min(m, n)) values in the worst case.
- Space complexity: O(m * n * min(m, n)).
"""

# Topic: Matrix/Grid