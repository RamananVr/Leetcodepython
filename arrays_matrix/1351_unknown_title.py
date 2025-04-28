"""
LeetCode Problem #1351: Count Negative Numbers in a Sorted Matrix

Problem Statement:
Given a `m x n` matrix `grid` which is sorted in non-increasing order both row-wise and column-wise, 
return the number of negative numbers in `grid`.

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `-100 <= grid[i][j] <= 100`

Follow up: Could you find an O(n + m) solution?
"""

# Python Solution
def countNegatives(grid):
    """
    Counts the number of negative numbers in a sorted matrix.

    :param grid: List[List[int]] - A 2D matrix sorted in non-increasing order both row-wise and column-wise.
    :return: int - The count of negative numbers in the matrix.
    """
    m, n = len(grid), len(grid[0])
    count = 0
    row, col = 0, n - 1  # Start from the top-right corner

    while row < m and col >= 0:
        if grid[row][col] < 0:
            # All elements below this one in the column are also negative
            count += (m - row)
            col -= 1  # Move left
        else:
            row += 1  # Move down

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    print(countNegatives(grid1))  # Output: 8

    # Test Case 2
    grid2 = [[3, 2], [1, 0]]
    print(countNegatives(grid2))  # Output: 0

    # Test Case 3
    grid3 = [[-1]]
    print(countNegatives(grid3))  # Output: 1

    # Test Case 4
    grid4 = [[5, 1, 0], [-5, -5, -5]]
    print(countNegatives(grid4))  # Output: 3

    # Test Case 5
    grid5 = [[3, 2, 1], [0, -1, -2], [-3, -4, -5]]
    print(countNegatives(grid5))  # Output: 5

"""
Time Complexity Analysis:
- The algorithm starts at the top-right corner of the matrix and moves either left or down.
- In the worst case, it visits each row and column exactly once, resulting in O(m + n) time complexity.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays, Matrix
"""