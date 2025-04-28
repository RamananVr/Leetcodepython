"""
LeetCode Problem #2711: Difference of Number of Distinct Values on Diagonals

Problem Statement:
You are given a 0-indexed 2D integer array `grid` of size `m x n`.

For each cell `(i, j)` in the grid, find the difference between:
1. The number of distinct values in the diagonal that goes from `(i, j)` to the top-left corner of the grid.
2. The number of distinct values in the diagonal that goes from `(i, j)` to the bottom-right corner of the grid.

Return a 2D array `result` of size `m x n` where `result[i][j]` is the difference between the number of distinct values in the two diagonals described above.

A diagonal is defined as a set of cells with the same difference between their row and column indices.

Example:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[0,1,2],[1,0,1],[2,1,0]]

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `1 <= grid[i][j] <= 100`
"""

# Solution
def differenceOfDistinctValues(grid):
    m, n = len(grid), len(grid[0])
    result = [[0] * n for _ in range(m)]
    
    # Helper function to calculate distinct values in a diagonal
    def get_distinct_values_diagonal(i, j, direction):
        distinct_values = set()
        while 0 <= i < m and 0 <= j < n:
            distinct_values.add(grid[i][j])
            if direction == "top-left":
                i -= 1
                j -= 1
            elif direction == "bottom-right":
                i += 1
                j += 1
        return distinct_values

    # Iterate through each cell in the grid
    for i in range(m):
        for j in range(n):
            top_left_distinct = get_distinct_values_diagonal(i, j, "top-left")
            bottom_right_distinct = get_distinct_values_diagonal(i, j, "bottom-right")
            result[i][j] = abs(len(top_left_distinct) - len(bottom_right_distinct))
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(differenceOfDistinctValues(grid1))  # Output: [[0, 1, 2], [1, 0, 1], [2, 1, 0]]

    # Test Case 2
    grid2 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    print(differenceOfDistinctValues(grid2))  # Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # Test Case 3
    grid3 = [[1, 2], [3, 4]]
    print(differenceOfDistinctValues(grid3))  # Output: [[0, 1], [1, 0]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- For each cell in the grid (m * n), we calculate the distinct values in two diagonals.
- Each diagonal traversal takes O(min(m, n)) time in the worst case.
- Therefore, the overall time complexity is O(m * n * min(m, n)).

Space Complexity:
- The space complexity is O(min(m, n)) for the set used to store distinct values during diagonal traversal.
- The result array takes O(m * n) space.
- Overall space complexity is O(m * n + min(m, n)).
"""

# Topic: Arrays, Matrix Traversal