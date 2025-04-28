"""
LeetCode Problem #1289: Minimum Falling Path Sum II

Problem Statement:
Given an `n x n` integer matrix `grid`, return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts starts at any element in the first row and chooses one element from each row. 
The next row's choice must be in a column that is different from the previous row's column by at least one.

Constraints:
- `n == grid.length == grid[i].length`
- `1 <= n <= 200`
- `-10^4 <= grid[i][j] <= 10^4`
"""

def minFallingPathSum(grid):
    """
    Function to compute the minimum falling path sum with non-zero shifts.

    :param grid: List[List[int]] - The input n x n grid
    :return: int - The minimum falling path sum
    """
    n = len(grid)
    
    # Initialize the previous row's minimum and second minimum values and their indices
    prev_min = prev_second_min = 0
    prev_min_index = -1

    for i in range(n):
        curr_min = curr_second_min = float('inf')
        curr_min_index = -1

        for j in range(n):
            # If the current column is the same as the previous row's minimum column, use the second minimum
            value = grid[i][j] + (prev_second_min if j == prev_min_index else prev_min)

            # Update the current row's minimum and second minimum
            if value < curr_min:
                curr_second_min = curr_min
                curr_min = value
                curr_min_index = j
            elif value < curr_second_min:
                curr_second_min = value

        # Update the previous row's values for the next iteration
        prev_min, prev_second_min, prev_min_index = curr_min, curr_second_min, curr_min_index

    return prev_min

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1,2,3],[4,5,6],[7,8,9]]
    print(minFallingPathSum(grid1))  # Output: 13

    # Test Case 2
    grid2 = [[7]]
    print(minFallingPathSum(grid2))  # Output: 7

    # Test Case 3
    grid3 = [[2,2,1,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]
    print(minFallingPathSum(grid3))  # Output: 7

    # Test Case 4
    grid4 = [[-19,57],[-40,-5]]
    print(minFallingPathSum(grid4))  # Output: -59

"""
Time Complexity Analysis:
- The algorithm iterates through each row and each column of the grid once.
- For each cell, it performs constant-time operations to compute the minimum and second minimum.
- Therefore, the time complexity is O(n^2), where n is the number of rows (or columns) in the grid.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space to store the minimum, second minimum, and their indices.
- Therefore, the space complexity is O(1).

Topic: Dynamic Programming (DP)
"""