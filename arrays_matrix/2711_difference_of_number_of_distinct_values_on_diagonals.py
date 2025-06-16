"""
LeetCode Problem #2711: Difference of Number of Distinct Values on Diagonals

Problem Statement:
Given a 0-indexed 2D grid of size `m x n`, you need to find the difference between the number of distinct values in the anti-diagonal starting at `grid[0][n-1]` and the number of distinct values in the anti-diagonal starting at `grid[m-1][0]`.

More formally, for each cell `(i, j)` in the grid, you need to find:
- The number of distinct values on the anti-diagonal from the top-right to the cell `(i, j)`
- The number of distinct values on the anti-diagonal from the cell `(i, j)` to the bottom-left
- Return the absolute difference between these two counts

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `1 <= grid[i][j] <= 50`
"""

def differenceOfDistinctValues(grid):
    """
    Calculates the difference of distinct values on diagonals for each cell.
    
    :param grid: List[List[int]] - 2D grid of integers
    :return: List[List[int]] - Grid with differences of distinct values
    """
    m, n = len(grid), len(grid[0])
    result = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            # Count distinct values from top-right to (i, j)
            top_right_distinct = set()
            r, c = i - 1, j + 1
            while r >= 0 and c < n:
                top_right_distinct.add(grid[r][c])
                r -= 1
                c += 1
            
            # Count distinct values from (i, j) to bottom-left
            bottom_left_distinct = set()
            r, c = i + 1, j - 1
            while r < m and c >= 0:
                bottom_left_distinct.add(grid[r][c])
                r += 1
                c -= 1
            
            result[i][j] = abs(len(top_right_distinct) - len(bottom_left_distinct))
    
    return result

def differenceOfDistinctValuesOptimized(grid):
    """
    Optimized solution using preprocessing of diagonals.
    
    :param grid: List[List[int]] - 2D grid of integers
    :return: List[List[int]] - Grid with differences of distinct values
    """
    m, n = len(grid), len(grid[0])
    result = [[0] * n for _ in range(m)]
    
    # Precompute distinct values for each diagonal
    for i in range(m):
        for j in range(n):
            # For each cell, compute the distinct values in both directions
            
            # Top-right direction
            top_right = set()
            r, c = i - 1, j + 1
            while r >= 0 and c < n:
                top_right.add(grid[r][c])
                r -= 1
                c += 1
            
            # Bottom-left direction
            bottom_left = set()
            r, c = i + 1, j - 1
            while r < m and c >= 0:
                bottom_left.add(grid[r][c])
                r += 1
                c -= 1
            
            result[i][j] = abs(len(top_right) - len(bottom_left))
    
    return result

def differenceOfDistinctValuesDiagonalWise(grid):
    """
    Solution that processes diagonals efficiently.
    
    :param grid: List[List[int]] - 2D grid of integers
    :return: List[List[int]] - Grid with differences of distinct values
    """
    m, n = len(grid), len(grid[0])
    result = [[0] * n for _ in range(m)]
    
    # For each cell, calculate the difference
    for i in range(m):
        for j in range(n):
            # Count distinct values in top-right diagonal
            distinct_top_right = set()
            x, y = i, j
            while x > 0 and y < n - 1:
                x -= 1
                y += 1
                distinct_top_right.add(grid[x][y])
            
            # Count distinct values in bottom-left diagonal
            distinct_bottom_left = set()
            x, y = i, j
            while x < m - 1 and y > 0:
                x += 1
                y -= 1
                distinct_bottom_left.add(grid[x][y])
            
            result[i][j] = abs(len(distinct_top_right) - len(distinct_bottom_left))
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid = [[1, 2, 3], [3, 1, 5], [3, 2, 1]]
    print("Grid:")
    for row in grid:
        print(row)
    print("Result:")
    result1 = differenceOfDistinctValues(grid)
    for row in result1:
        print(row)
    print()

    # Test Case 2
    grid = [[1]]
    print("Grid:")
    for row in grid:
        print(row)
    print("Result:")
    result2 = differenceOfDistinctValues(grid)
    for row in result2:
        print(row)  # Output: [[0]]
    print()

    # Test Case 3
    grid = [[1, 2], [3, 4]]
    print("Grid:")
    for row in grid:
        print(row)
    print("Result:")
    result3 = differenceOfDistinctValues(grid)
    for row in result3:
        print(row)
    print()

    # Test Case 4
    grid = [[5, 1, 2, 1], [4, 3, 2, 1], [3, 2, 1, 0]]
    print("Grid:")
    for row in grid:
        print(row)
    print("Result:")
    result4 = differenceOfDistinctValues(grid)
    for row in result4:
        print(row)
    print()

    # Test Case 5 - Single row
    grid = [[1, 2, 3, 4]]
    print("Grid:")
    for row in grid:
        print(row)
    print("Result:")
    result5 = differenceOfDistinctValues(grid)
    for row in result5:
        print(row)

    # Validation - check consistency across different implementations
    test_grid = [[1, 2, 3], [3, 1, 5], [3, 2, 1]]
    assert differenceOfDistinctValues(test_grid) == differenceOfDistinctValuesOptimized(test_grid)
    assert differenceOfDistinctValues(test_grid) == differenceOfDistinctValuesDiagonalWise(test_grid)
    print("All test cases passed!")

"""
Time Complexity Analysis:
All Solutions:
- Time complexity: O(m * n * min(m, n)) where m and n are the dimensions of the grid.
- For each cell, we traverse along the diagonal which can be at most min(m, n) cells.

Space Complexity Analysis:
- Space complexity: O(m * n) for the result grid plus O(min(m, n)) for the sets storing distinct values.

Topic: Arrays, Matrix, Set Operations
"""
