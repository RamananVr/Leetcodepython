"""
LeetCode Problem #1072: Flip Columns For Maximum Number of Equal Rows

Problem Statement:
You are given an `m x n` binary matrix `matrix`.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., change the value of the cell from 0 to 1 or from 1 to 0).

Return the maximum number of rows that have all values equal after some number of flips.

Example 1:
Input: matrix = [[0,1],[1,0]]
Output: 2
Explanation: Flipping no columns, 0th row and 1st row both are already equal.

Example 2:
Input: matrix = [[0,1],[1,1]]
Output: 1
Explanation: Flipping no columns, only the 1st row is equal.

Example 3:
Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: Flipping column 2 changes the matrix to [[0,0,0],[0,0,0],[1,1,1]], where the 0th and 1st rows are equal.

Constraints:
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 300`
- `matrix[i][j]` is either `0` or `1`.
"""

# Python Solution
from collections import Counter
from typing import List

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        """
        This function calculates the maximum number of rows that can be made equal
        by flipping any number of columns in the given binary matrix.
        """
        pattern_count = Counter()
        
        for row in matrix:
            # Normalize the row by treating it and its complement as the same pattern
            # This ensures that flipping columns is equivalent to matching patterns
            normalized = tuple(row) if row[0] == 0 else tuple(1 - x for x in row)
            pattern_count[normalized] += 1
        
        # The maximum count of any pattern is the answer
        return max(pattern_count.values())

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    matrix1 = [[0, 1], [1, 0]]
    print(solution.maxEqualRowsAfterFlips(matrix1))  # Output: 2
    
    # Test Case 2
    matrix2 = [[0, 1], [1, 1]]
    print(solution.maxEqualRowsAfterFlips(matrix2))  # Output: 1
    
    # Test Case 3
    matrix3 = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]
    print(solution.maxEqualRowsAfterFlips(matrix3))  # Output: 2
    
    # Test Case 4
    matrix4 = [[0, 0], [1, 1], [0, 1]]
    print(solution.maxEqualRowsAfterFlips(matrix4))  # Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let `m` be the number of rows and `n` be the number of columns in the matrix.
- For each row, we compute its normalized pattern, which takes O(n) time.
- We then update the Counter, which is an O(1) operation per row.
- Overall, the time complexity is O(m * n).

Space Complexity:
- We store the normalized patterns in a Counter. In the worst case, there can be up to `m` unique patterns.
- Each pattern is a tuple of length `n`, so the space complexity is O(m * n).
"""

# Topic: Arrays, Hashing