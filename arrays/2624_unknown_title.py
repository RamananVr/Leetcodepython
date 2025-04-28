"""
LeetCode Problem #2624: Snail Traversal

Problem Statement:
Given a 2D matrix, return all elements of the matrix in a snail traversal order. 
The snail traversal order starts from the top-left corner and proceeds in a clockwise 
spiral pattern until all elements are visited.

Example:
Input: matrix = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

Constraints:
- The matrix will have dimensions m x n where 1 <= m, n <= 100.
- The elements of the matrix are integers.
"""

def snail_traversal(matrix):
    """
    Returns the elements of the matrix in snail traversal order.

    :param matrix: List[List[int]] - 2D matrix of integers
    :return: List[int] - List of integers in snail traversal order
    """
    if not matrix or not matrix[0]:
        return []

    result = []
    while matrix:
        # Add the first row
        result += matrix.pop(0)
        
        # Add the last element of each remaining row
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        
        # Add the last row in reverse order
        if matrix:
            result += matrix.pop()[::-1]
        
        # Add the first element of each remaining row in reverse order
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    matrix1 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    print(snail_traversal(matrix1))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

    # Test Case 2
    matrix2 = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12]]
    print(snail_traversal(matrix2))  # Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    # Test Case 3
    matrix3 = [[1]]
    print(snail_traversal(matrix3))  # Output: [1]

    # Test Case 4
    matrix4 = [[1, 2],
               [3, 4]]
    print(snail_traversal(matrix4))  # Output: [1, 2, 4, 3]

    # Test Case 5
    matrix5 = []
    print(snail_traversal(matrix5))  # Output: []

"""
Time Complexity Analysis:
- Let m be the number of rows and n be the number of columns in the matrix.
- Each element of the matrix is visited exactly once, so the time complexity is O(m * n).

Space Complexity Analysis:
- The space complexity is O(1) additional space (excluding the output list), as we modify the input matrix in place.

Topic: Arrays
"""