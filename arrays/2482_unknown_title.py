"""
LeetCode Problem #2482: Difference Between Ones and Zeros in Row and Column

Problem Statement:
You are given a 0-indexed m x n binary matrix grid. A binary matrix has only 0s and 1s as values.

Let onesRow[i] be the number of 1s in the ith row.
Let onesCol[j] be the number of 1s in the jth column.
Let zerosRow[i] be the number of 0s in the ith row.
Let zerosCol[j] be the number of 0s in the jth column.

The difference matrix diff is a matrix of the same size as grid where:
    diff[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]

Return the difference matrix diff.

Example:
Input: grid = [[0,1,1],[1,0,1],[0,0,1]]
Output: [[0,0,4],[0,0,4],[-2,-2,2]]

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 1000
- grid[i][j] is either 0 or 1
"""

# Solution
def ones_and_zeros_difference(grid):
    m, n = len(grid), len(grid[0])
    
    # Calculate onesRow and zerosRow
    onesRow = [sum(row) for row in grid]
    zerosRow = [n - onesRow[i] for i in range(m)]
    
    # Calculate onesCol and zerosCol
    onesCol = [sum(grid[i][j] for i in range(m)) for j in range(n)]
    zerosCol = [m - onesCol[j] for j in range(n)]
    
    # Build the difference matrix
    diff = [[onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j] for j in range(n)] for i in range(m)]
    
    return diff

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[0, 1, 1], [1, 0, 1], [0, 0, 1]]
    print(ones_and_zeros_difference(grid1))  # Expected Output: [[0, 0, 4], [0, 0, 4], [-2, -2, 2]]

    # Test Case 2
    grid2 = [[1, 0], [0, 1]]
    print(ones_and_zeros_difference(grid2))  # Expected Output: [[2, 0], [0, 2]]

    # Test Case 3
    grid3 = [[1, 1], [1, 1]]
    print(ones_and_zeros_difference(grid3))  # Expected Output: [[4, 4], [4, 4]]

    # Test Case 4
    grid4 = [[0, 0], [0, 0]]
    print(ones_and_zeros_difference(grid4))  # Expected Output: [[-4, -4], [-4, -4]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating onesRow and zerosRow takes O(m * n), as we iterate through each row and sum its elements.
- Calculating onesCol and zerosCol takes O(m * n), as we iterate through each column and sum its elements.
- Constructing the diff matrix takes O(m * n), as we iterate through each cell to compute the difference.
- Overall time complexity: O(m * n).

Space Complexity:
- onesRow and zerosRow each take O(m) space.
- onesCol and zerosCol each take O(n) space.
- The diff matrix takes O(m * n) space.
- Overall space complexity: O(m * n).
"""

# Topic: Arrays