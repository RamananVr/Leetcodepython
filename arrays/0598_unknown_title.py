"""
LeetCode Problem #598: Range Addition II

Problem Statement:
You are given an `m x n` matrix initialized with all 0's and several update operations.

Operations are represented by a 2D array, where each operation is represented as an array with two positive integers `a` and `b`. 
Each operation adds 1 to all cells in the rectangle defined by the coordinates `(0, 0)` to `(a-1, b-1)` inclusive.

You need to return the number of maximum integers in the matrix after performing all the operations.

Example:
Input: m = 3, n = 3, ops = [[2,2],[3,3]]
Output: 4
Explanation: 
After performing [2,2], the top-left 2x2 submatrix becomes:
[[1,1,0],
 [1,1,0],
 [0,0,0]]
After performing [3,3], the entire 3x3 matrix becomes:
[[2,2,2],
 [2,2,2],
 [2,2,2]]
The maximum integers are located in the top-left 2x2 submatrix.

Constraints:
- 1 <= m, n <= 4 * 10^4
- 0 <= ops.length <= 10^4
- ops[i].length == 2
- 1 <= ops[i][0] <= m
- 1 <= ops[i][1] <= n
"""

# Clean, Correct Python Solution
def maxCount(m: int, n: int, ops: list[list[int]]) -> int:
    """
    Returns the number of maximum integers in the matrix after performing all operations.

    :param m: Number of rows in the matrix
    :param n: Number of columns in the matrix
    :param ops: List of operations, where each operation is a list [a, b]
    :return: Number of maximum integers in the matrix
    """
    if not ops:
        return m * n
    
    # Find the minimum dimensions affected by all operations
    min_row = m
    min_col = n
    for a, b in ops:
        min_row = min(min_row, a)
        min_col = min(min_col, b)
    
    # The maximum integers are located in the rectangle defined by (0, 0) to (min_row-1, min_col-1)
    return min_row * min_col

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    m = 3
    n = 3
    ops = [[2, 2], [3, 3]]
    print(maxCount(m, n, ops))  # Output: 4

    # Test Case 2
    m = 3
    n = 3
    ops = []
    print(maxCount(m, n, ops))  # Output: 9

    # Test Case 3
    m = 5
    n = 5
    ops = [[3, 3], [2, 2], [4, 4]]
    print(maxCount(m, n, ops))  # Output: 4

    # Test Case 4
    m = 10
    n = 10
    ops = [[1, 1], [2, 2], [3, 3]]
    print(maxCount(m, n, ops))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution iterates through the `ops` list once to find the minimum dimensions affected by all operations.
- Let `k` be the length of `ops`. The time complexity is O(k).

Space Complexity:
- The solution uses a constant amount of extra space, so the space complexity is O(1).
"""

# Topic: Arrays