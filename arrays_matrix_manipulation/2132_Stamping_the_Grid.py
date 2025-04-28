"""
LeetCode Problem #2132: Stamping the Grid

Problem Statement:
You are given two m x n binary matrices `grid1` and `grid2` containing only 0's (representing empty cells) and 1's (representing filled cells). You are also given an integer `stampHeight` and an integer `stampWidth`.

You want to stamp `grid2` onto `grid1`. To do this, you can choose any position in `grid1` and stamp a submatrix of size `stampHeight x stampWidth` onto it. The stamp will overwrite the cells in `grid1` with the corresponding cells in `grid2`. However, you can only stamp if all the cells in the submatrix of `grid1` are 0.

Return `true` if it is possible to stamp `grid2` onto `grid1`. Otherwise, return `false`.

Constraints:
- m == grid1.length == grid2.length
- n == grid1[i].length == grid2[i].length
- 1 <= m, n <= 1000
- 1 <= stampHeight, stampWidth <= min(m, n)
- grid1[i][j] and grid2[i][j] are either 0 or 1.
"""

from collections import deque

def possibleToStamp(grid1, grid2, stampHeight, stampWidth):
    """
    Determines if it is possible to stamp grid2 onto grid1.

    :param grid1: List[List[int]] - The base grid.
    :param grid2: List[List[int]] - The target grid.
    :param stampHeight: int - The height of the stamp.
    :param stampWidth: int - The width of the stamp.
    :return: bool - True if stamping is possible, False otherwise.
    """
    m, n = len(grid1), len(grid1[0])
    
    # Step 1: Calculate the difference grid
    diff = [[grid2[i][j] - grid1[i][j] for j in range(n)] for i in range(m)]
    
    # Step 2: Check if stamping is possible
    can_stamp = [[0] * n for _ in range(m)]
    for i in range(m - stampHeight + 1):
        for j in range(n - stampWidth + 1):
            # Check if we can stamp at (i, j)
            if all(diff[x][y] == 1 for x in range(i, i + stampHeight) for y in range(j, j + stampWidth)):
                # Mark the cells as stamped
                for x in range(i, i + stampHeight):
                    for y in range(j, j + stampWidth):
                        can_stamp[x][y] = 1
    
    # Step 3: Verify if all 1s in grid2 are covered
    for i in range(m):
        for j in range(n):
            if grid2[i][j] == 1 and not can_stamp[i][j]:
                return False
    
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    grid2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    stampHeight = 2
    stampWidth = 2
    print(possibleToStamp(grid1, grid2, stampHeight, stampWidth))  # Output: True

    # Test Case 2
    grid1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    grid2 = [[1, 1, 1], [1, 1, 1], [1, 0, 1]]
    stampHeight = 2
    stampWidth = 2
    print(possibleToStamp(grid1, grid2, stampHeight, stampWidth))  # Output: False

    # Test Case 3
    grid1 = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    grid2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    stampHeight = 2
    stampWidth = 2
    print(possibleToStamp(grid1, grid2, stampHeight, stampWidth))  # Output: False

# Time Complexity Analysis:
# Let m = number of rows, n = number of columns.
# - Calculating the difference grid takes O(m * n).
# - Checking for stamping takes O((m - stampHeight + 1) * (n - stampWidth + 1) * stampHeight * stampWidth).
#   In the worst case, this is O(m * n * stampHeight * stampWidth).
# - Verifying the result takes O(m * n).
# Overall time complexity: O(m * n * stampHeight * stampWidth).

# Space Complexity Analysis:
# - The difference grid and can_stamp grid each take O(m * n) space.
# Overall space complexity: O(m * n).

# Topic: Arrays, Matrix Manipulation