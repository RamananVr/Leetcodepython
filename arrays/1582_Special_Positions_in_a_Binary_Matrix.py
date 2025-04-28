"""
LeetCode Problem #1582: Special Positions in a Binary Matrix

Problem Statement:
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if:
- mat[i][j] == 1, and
- All other elements in row i are 0, and
- All other elements in column j are 0.

Example 1:
Input: mat = [[1,0,0],
              [0,0,1],
              [1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

Example 2:
Input: mat = [[1,0,0],
              [0,1,0],
              [0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1), and (2, 2) are all special positions.

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 100
- mat[i][j] is either 0 or 1.
"""

def numSpecial(mat):
    """
    Function to count the number of special positions in a binary matrix.

    :param mat: List[List[int]] - The binary matrix
    :return: int - The number of special positions
    """
    # Count the sum of each row and column
    row_sums = [sum(row) for row in mat]
    col_sums = [sum(col) for col in zip(*mat)]
    
    # Initialize the count of special positions
    special_count = 0
    
    # Iterate through the matrix to find special positions
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            # Check if the current position is special
            if mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1:
                special_count += 1
    
    return special_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [[1, 0, 0],
            [0, 0, 1],
            [1, 0, 0]]
    print(numSpecial(mat1))  # Output: 1

    # Test Case 2
    mat2 = [[1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]]
    print(numSpecial(mat2))  # Output: 3

    # Test Case 3
    mat3 = [[0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]]
    print(numSpecial(mat3))  # Output: 1

    # Test Case 4
    mat4 = [[1, 0],
            [0, 1]]
    print(numSpecial(mat4))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating row_sums takes O(m * n), where m is the number of rows and n is the number of columns.
- Calculating col_sums takes O(m * n) (using zip(*mat)).
- Iterating through the matrix to check special positions takes O(m * n).
- Overall time complexity: O(m * n).

Space Complexity:
- row_sums and col_sums each take O(m + n) space.
- No additional space is used apart from these lists.
- Overall space complexity: O(m + n).

Topic: Arrays
"""