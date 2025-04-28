"""
LeetCode Problem #2373: Largest Local Values in a Matrix

Problem Statement:
You are given an n x n integer matrix `grid`. Generate an integer matrix `maxLocal` of size (n - 2) x (n - 2) such that:

- `maxLocal[i][j]` is equal to the largest value of the 3 x 3 matrix in `grid` centered at (i + 1, j + 1).

In other words, we want to find the largest value in every contiguous 3 x 3 submatrix in `grid`.

Return the generated matrix.

Constraints:
- n == grid.length == grid[i].length
- 3 <= n <= 100
- 1 <= grid[i][j] <= 100
"""

def largestLocal(grid):
    """
    Finds the largest local values in a matrix.

    :param grid: List[List[int]] - The input n x n matrix.
    :return: List[List[int]] - The resulting (n-2) x (n-2) matrix with largest local values.
    """
    n = len(grid)
    maxLocal = [[0] * (n - 2) for _ in range(n - 2)]

    for i in range(n - 2):
        for j in range(n - 2):
            # Extract the 3x3 submatrix and find the maximum value
            maxLocal[i][j] = max(
                grid[i][j], grid[i][j + 1], grid[i][j + 2],
                grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2],
                grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2]
            )

    return maxLocal

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [9, 9, 8, 1],
        [5, 6, 2, 6],
        [8, 2, 6, 4],
        [6, 2, 2, 2]
    ]
    print("Test Case 1 Output:", largestLocal(grid1))
    # Expected Output: [[9, 9], [8, 6]]

    # Test Case 2
    grid2 = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 2, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    print("Test Case 2 Output:", largestLocal(grid2))
    # Expected Output: [[2, 2, 2], [2, 2, 2], [2, 2, 2]]

    # Test Case 3
    grid3 = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
    print("Test Case 3 Output:", largestLocal(grid3))
    # Expected Output: [[90]]

"""
Time Complexity Analysis:
- The outer loop runs (n - 2) times, and the inner loop also runs (n - 2) times.
- For each iteration, we compute the maximum of 9 elements (a constant operation).
- Therefore, the time complexity is O((n - 2) * (n - 2) * 9) = O(n^2).

Space Complexity Analysis:
- The space complexity is O((n - 2) * (n - 2)) for the `maxLocal` matrix.
- No additional space is used apart from the output matrix.
- Therefore, the space complexity is O(n^2).

Topic: Arrays
"""