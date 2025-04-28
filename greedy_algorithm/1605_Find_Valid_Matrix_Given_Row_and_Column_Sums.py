"""
LeetCode Problem #1605: Find Valid Matrix Given Row and Column Sums

Problem Statement:
You are given two arrays `rowSum` and `colSum` of non-negative integers where 
`rowSum[i]` is the sum of the elements in the `i-th` row and `colSum[j]` is the 
sum of the elements in the `j-th` column of a 2D matrix. In other words, you do 
not know the elements of the matrix, but you do know the sums of each row and 
column.

Find any matrix of non-negative integers of size `rowSum.length x colSum.length` 
that satisfies the given `rowSum` and `colSum` requirements.

Return a 2D array representing any matrix that fulfills the requirements. It is 
guaranteed that at least one matrix that fulfills the requirements exists.

Constraints:
- `1 <= rowSum.length, colSum.length <= 500`
- `0 <= rowSum[i], colSum[i] <= 10^8`
- The sum of all elements in `rowSum` is equal to the sum of all elements in `colSum`.

Example:
Input: rowSum = [3, 8], colSum = [4, 7]
Output: [[3, 0],
         [1, 7]]

Input: rowSum = [5, 7, 10], colSum = [8, 6, 8]
Output: [[5, 0, 0],
         [3, 4, 0],
         [0, 2, 8]]
"""

def restoreMatrix(rowSum, colSum):
    """
    Function to restore a matrix given row and column sums.

    Args:
    rowSum (List[int]): List of row sums.
    colSum (List[int]): List of column sums.

    Returns:
    List[List[int]]: A 2D matrix satisfying the row and column sums.
    """
    rows = len(rowSum)
    cols = len(colSum)
    matrix = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            # Take the minimum of the current rowSum and colSum
            val = min(rowSum[i], colSum[j])
            matrix[i][j] = val
            # Update rowSum and colSum
            rowSum[i] -= val
            colSum[j] -= val

    return matrix

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    rowSum1 = [3, 8]
    colSum1 = [4, 7]
    print("Test Case 1 Output:")
    print(restoreMatrix(rowSum1, colSum1))  # Expected: [[3, 0], [1, 7]]

    # Test Case 2
    rowSum2 = [5, 7, 10]
    colSum2 = [8, 6, 8]
    print("Test Case 2 Output:")
    print(restoreMatrix(rowSum2, colSum2))  # Expected: [[5, 0, 0], [3, 4, 0], [0, 2, 8]]

    # Test Case 3
    rowSum3 = [14, 9]
    colSum3 = [6, 9, 8]
    print("Test Case 3 Output:")
    print(restoreMatrix(rowSum3, colSum3))  # Expected: [[6, 8, 0], [0, 1, 8]]

    # Test Case 4
    rowSum4 = [1, 1, 1]
    colSum4 = [1, 1, 1]
    print("Test Case 4 Output:")
    print(restoreMatrix(rowSum4, colSum4))  # Expected: [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

"""
Time Complexity Analysis:
- The algorithm iterates through each cell of the matrix once.
- If `m` is the number of rows and `n` is the number of columns, the time complexity is O(m * n).

Space Complexity Analysis:
- The algorithm uses a 2D matrix of size `m x n` to store the result.
- The space complexity is O(m * n).

Topic: Greedy Algorithm
"""