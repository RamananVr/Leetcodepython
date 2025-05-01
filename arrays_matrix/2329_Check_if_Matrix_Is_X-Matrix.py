"""
LeetCode Problem #2329: "Check if Matrix Is X-Matrix"

Problem Statement:
A square matrix is said to be an X-Matrix if both of the following conditions hold:
1. All the elements in the diagonals of the matrix are non-zero.
2. All other elements are 0.

Given a 2D integer array `grid` of size `n x n` representing a square matrix, return `true` if `grid` is an X-Matrix. Otherwise, return `false`.

Example 1:
Input: grid = [[2,0,0,1],
               [0,3,1,0],
               [0,5,2,0],
               [4,0,0,2]]
Output: true
Explanation: The diagonals of the grid are:
- The main diagonal: [2, 3, 2, 2]
- The secondary diagonal: [1, 1, 5, 4]
All the elements in the diagonals are non-zero, and all other elements are 0.

Example 2:
Input: grid = [[5,7,0],
               [0,3,1],
               [0,5,0]]
Output: false
Explanation: The grid is not an X-Matrix because grid[0][1] is 7, which is not 0.

Constraints:
- n == grid.length == grid[i].length
- 3 <= n <= 100
- 0 <= grid[i][j] <= 10^5
"""

def checkXMatrix(grid):
    """
    Function to check if a given square matrix is an X-Matrix.

    :param grid: List[List[int]] - 2D integer array representing the square matrix
    :return: bool - True if the matrix is an X-Matrix, False otherwise
    """
    n = len(grid)
    
    for i in range(n):
        for j in range(n):
            # Check if the current element is on a diagonal
            if i == j or i + j == n - 1:
                # Diagonal elements must be non-zero
                if grid[i][j] == 0:
                    return False
            else:
                # Non-diagonal elements must be zero
                if grid[i][j] != 0:
                    return False
    
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[2, 0, 0, 1],
             [0, 3, 1, 0],
             [0, 5, 2, 0],
             [4, 0, 0, 2]]
    print(checkXMatrix(grid1))  # Output: True

    # Test Case 2
    grid2 = [[5, 7, 0],
             [0, 3, 1],
             [0, 5, 0]]
    print(checkXMatrix(grid2))  # Output: False

    # Test Case 3
    grid3 = [[1, 0, 0, 0, 1],
             [0, 1, 0, 1, 0],
             [0, 0, 1, 0, 0],
             [0, 1, 0, 1, 0],
             [1, 0, 0, 0, 1]]
    print(checkXMatrix(grid3))  # Output: True

    # Test Case 4
    grid4 = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    print(checkXMatrix(grid4))  # Output: False

"""
Time Complexity Analysis:
- The function iterates through all elements of the grid, which has a size of n x n.
- Therefore, the time complexity is O(n^2), where n is the size of the grid.

Space Complexity Analysis:
- The function uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays, Matrix
"""