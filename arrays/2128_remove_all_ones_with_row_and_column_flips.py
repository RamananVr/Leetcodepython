"""
LeetCode Question #2128: Remove All Ones With Row and Column Flips

Problem Statement:
You are given an m x n binary matrix grid. In one operation, you can choose any row or column and flip all the values in that row or column (i.e., changing all 0s to 1s and all 1s to 0s).

Return true if it is possible to remove all 1s from grid using any number of operations or false otherwise.

Example 1:
Input: grid = [[0,1,0],[1,0,1],[0,1,0]]
Output: true
Explanation: Flip the middle row, then flip the middle column.

Example 2:
Input: grid = [[1,1,0],[0,0,0],[0,0,0]]
Output: false
Explanation: It is impossible to remove all 1s from grid.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- grid[i][j] is either 0 or 1.
"""

def removeOnes(grid):
    """
    Determines if it is possible to remove all 1s from the grid using row and column flips.

    :param grid: List[List[int]] - The binary matrix.
    :return: bool - True if all 1s can be removed, False otherwise.
    """
    # Get the first row of the grid
    first_row = grid[0]
    
    # Iterate through each row in the grid
    for row in grid:
        # Check if the row matches the first row or its complement
        if row != first_row and row != [1 - x for x in first_row]:
            return False
    
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    print(removeOnes(grid1))  # Output: True

    # Test Case 2
    grid2 = [[1, 1, 0], [0, 0, 0], [0, 0, 0]]
    print(removeOnes(grid2))  # Output: False

    # Test Case 3
    grid3 = [[1, 1], [0, 0]]
    print(removeOnes(grid3))  # Output: True

    # Test Case 4
    grid4 = [[1, 0], [0, 1]]
    print(removeOnes(grid4))  # Output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through each row of the grid and compares it to the first row or its complement.
- Let m be the number of rows and n be the number of columns in the grid.
- The comparison operation takes O(n) time for each row.
- Therefore, the overall time complexity is O(m * n).

Space Complexity:
- The algorithm uses O(n) space to store the complement of the first row.
- No additional data structures are used, so the space complexity is O(n).

Topic: Arrays
"""