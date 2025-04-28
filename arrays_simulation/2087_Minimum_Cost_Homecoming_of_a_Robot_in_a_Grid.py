"""
LeetCode Problem #2087: Minimum Cost Homecoming of a Robot in a Grid

Problem Statement:
There is an `m x n` grid, where `(0, 0)` is the top-left cell and `(m - 1, n - 1)` is the bottom-right cell. 
You are given an integer array `startPos` where `startPos = [startrow, startcol]` indicates the starting position of a robot. 
You are also given an integer array `homePos` where `homePos = [homerow, homecol]` indicates the home position of the robot. 
All the cells of the grid have a cost associated with them, and you are given two 1-indexed integer arrays `rowCosts` and `colCosts` 
where `rowCosts[r]` is the cost of moving to any cell in row `r` from any cell in row `r - 1` or row `r + 1`, and `colCosts[c]` is the 
cost of moving to any cell in column `c` from any cell in column `c - 1` or column `c + 1`.

The robot can only travel either up, down, left, or right. Return the minimum total cost for the robot to return home.

Constraints:
- `m == rowCosts.length`
- `n == colCosts.length`
- `1 <= m, n <= 10^5`
- `0 <= rowCosts[r], colCosts[c] <= 10^4`
- `startPos.length == 2`
- `homePos.length == 2`
- `0 <= startrow, homerow < m`
- `0 <= startcol, homecol < n`
"""

def minCost(startPos, homePos, rowCosts, colCosts):
    """
    Calculate the minimum cost for the robot to return home.

    :param startPos: List[int] - Starting position [startrow, startcol]
    :param homePos: List[int] - Home position [homerow, homecol]
    :param rowCosts: List[int] - Cost of moving between rows
    :param colCosts: List[int] - Cost of moving between columns
    :return: int - Minimum total cost
    """
    start_row, start_col = startPos
    home_row, home_col = homePos

    # Calculate the cost of moving vertically (row-wise)
    row_cost = 0
    if start_row < home_row:
        for r in range(start_row + 1, home_row + 1):
            row_cost += rowCosts[r]
    else:
        for r in range(start_row - 1, home_row - 1, -1):
            row_cost += rowCosts[r]

    # Calculate the cost of moving horizontally (column-wise)
    col_cost = 0
    if start_col < home_col:
        for c in range(start_col + 1, home_col + 1):
            col_cost += colCosts[c]
    else:
        for c in range(start_col - 1, home_col - 1, -1):
            col_cost += colCosts[c]

    # Total cost is the sum of row and column costs
    return row_cost + col_cost

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    startPos = [1, 0]
    homePos = [2, 3]
    rowCosts = [5, 4, 3]
    colCosts = [8, 2, 6, 7]
    print(minCost(startPos, homePos, rowCosts, colCosts))  # Output: 18

    # Test Case 2
    startPos = [0, 0]
    homePos = [0, 0]
    rowCosts = [5]
    colCosts = [5]
    print(minCost(startPos, homePos, rowCosts, colCosts))  # Output: 0

    # Test Case 3
    startPos = [0, 0]
    homePos = [3, 3]
    rowCosts = [1, 2, 3, 4]
    colCosts = [1, 2, 3, 4]
    print(minCost(startPos, homePos, rowCosts, colCosts))  # Output: 20

"""
Time Complexity:
- Moving row-wise: O(|startrow - homerow|) = O(m), where m is the number of rows.
- Moving column-wise: O(|startcol - homecol|) = O(n), where n is the number of columns.
- Total: O(m + n), where m and n are the dimensions of the grid.

Space Complexity:
- O(1), as we are using a constant amount of extra space.

Topic: Arrays, Simulation
"""