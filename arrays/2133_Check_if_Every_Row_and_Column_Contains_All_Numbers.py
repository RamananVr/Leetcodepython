"""
LeetCode Problem #2133: Check if Every Row and Column Contains All Numbers

Problem Statement:
An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive). 
Given an n x n integer matrix `matrix`, return true if the matrix is valid. Otherwise, return false.

Example 1:
Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
Output: true
Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.

Example 2:
Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
Output: false
Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 1, 2, and 3.

Constraints:
- n == matrix.length == matrix[i].length
- 1 <= n <= 100
- 1 <= matrix[i][j] <= n
"""

def checkValid(matrix):
    """
    Function to check if every row and column in the matrix contains all integers from 1 to n.

    :param matrix: List[List[int]] - The n x n matrix to validate
    :return: bool - True if the matrix is valid, False otherwise
    """
    n = len(matrix)
    expected_set = set(range(1, n + 1))
    
    # Check each row
    for row in matrix:
        if set(row) != expected_set:
            return False
    
    # Check each column
    for col in range(n):
        column_set = {matrix[row][col] for row in range(n)}
        if column_set != expected_set:
            return False
    
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    matrix1 = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
    print(checkValid(matrix1))  # Output: True

    # Test Case 2
    matrix2 = [[1, 1, 1], [1, 2, 3], [1, 2, 3]]
    print(checkValid(matrix2))  # Output: False

    # Test Case 3
    matrix3 = [[1]]
    print(checkValid(matrix3))  # Output: True

    # Test Case 4
    matrix4 = [[1, 2], [2, 1]]
    print(checkValid(matrix4))  # Output: True

    # Test Case 5
    matrix5 = [[1, 2], [1, 2]]
    print(checkValid(matrix5))  # Output: False

"""
Time Complexity Analysis:
- Checking each row takes O(n^2) time because there are n rows, and converting each row to a set takes O(n).
- Checking each column also takes O(n^2) time because there are n columns, and constructing a set for each column takes O(n).
- Overall time complexity: O(n^2).

Space Complexity Analysis:
- The space complexity is O(n) because we use a set to store the expected values (1 to n) and a temporary set for each row/column.
- Overall space complexity: O(n).

Topic: Arrays
"""