"""
LeetCode Question #1727: Largest Submatrix With Rearrangements

Problem Statement:
You are given a binary matrix `matrix` (a matrix consisting of only 0s and 1s) of size m x n. You can rearrange the columns of the matrix in any order.

Return the area of the largest submatrix that can be formed after rearranging the columns.

Example:
Input: matrix = [[0,0,1],[1,1,1],[0,1,0]]
Output: 4
Explanation: Rearrange the columns as [[1,0,0],[1,1,1],[0,1,0]].
The largest submatrix is:
[[1,1],
 [1,1]]
Its area is 4.

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10^5
- matrix[i][j] is either 0 or 1.
"""

# Solution
def largestSubmatrix(matrix):
    """
    Finds the area of the largest submatrix that can be formed after rearranging columns.

    :param matrix: List[List[int]] - Binary matrix of size m x n
    :return: int - Area of the largest submatrix
    """
    m, n = len(matrix), len(matrix[0])
    
    # Step 1: Compute the height of consecutive 1s for each column
    for i in range(1, m):
        for j in range(n):
            if matrix[i][j] == 1:
                matrix[i][j] += matrix[i - 1][j]
    
    # Step 2: Calculate the maximum area by sorting each row
    max_area = 0
    for row in matrix:
        row.sort(reverse=True)  # Sort heights in descending order
        for k in range(n):
            max_area = max(max_area, row[k] * (k + 1))  # Area = height * width
    
    return max_area

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    matrix1 = [[0, 0, 1], [1, 1, 1], [0, 1, 0]]
    print(largestSubmatrix(matrix1))  # Output: 4

    # Test Case 2
    matrix2 = [[1, 0, 1, 0], [1, 1, 1, 1], [0, 1, 0, 1]]
    print(largestSubmatrix(matrix2))  # Output: 6

    # Test Case 3
    matrix3 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print(largestSubmatrix(matrix3))  # Output: 9

    # Test Case 4
    matrix4 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(largestSubmatrix(matrix4))  # Output: 0

    # Test Case 5
    matrix5 = [[1]]
    print(largestSubmatrix(matrix5))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Computing the height matrix: O(m * n), where m is the number of rows and n is the number of columns.
- Sorting each row: O(m * n * log(n)), as each row of size n is sorted.
- Calculating the maximum area: O(m * n), as we iterate through each row and column.
Overall: O(m * n * log(n))

Space Complexity:
- The algorithm modifies the input matrix in-place, so no additional space is used.
Overall: O(1) additional space.
"""

# Topic: Arrays, Sorting