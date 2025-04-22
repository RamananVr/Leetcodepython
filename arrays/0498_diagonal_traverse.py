"""
LeetCode Question #498: Diagonal Traverse

Problem Statement:
Given an `m x n` matrix `mat`, return an array of all the elements of the array in a diagonal order.

You need to traverse the matrix diagonally, starting from the top-left corner. The traversal alternates between moving upwards and downwards along the diagonals. 

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

Constraints:
- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 10^4`
- `1 <= m * n <= 10^4`
- `-10^5 <= mat[i][j] <= 10^5`
"""

def findDiagonalOrder(mat):
    """
    Returns the elements of the matrix in diagonal order.

    :param mat: List[List[int]] - The input matrix
    :return: List[int] - The elements in diagonal order
    """
    if not mat or not mat[0]:
        return []

    m, n = len(mat), len(mat[0])
    result = []
    diagonals = {}

    # Group elements by their diagonal index (i + j)
    for i in range(m):
        for j in range(n):
            if i + j not in diagonals:
                diagonals[i + j] = []
            diagonals[i + j].append(mat[i][j])

    # Traverse diagonals and append elements to the result
    for k in range(len(diagonals)):
        if k % 2 == 0:
            # Reverse the diagonal for upward traversal
            result.extend(diagonals[k][::-1])
        else:
            # Keep the diagonal as is for downward traversal
            result.extend(diagonals[k])

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(findDiagonalOrder(mat1))  # Output: [1, 2, 4, 7, 5, 3, 6, 8, 9]

    # Test Case 2
    mat2 = [[1, 2], [3, 4]]
    print(findDiagonalOrder(mat2))  # Output: [1, 2, 3, 4]

    # Test Case 3
    mat3 = [[1]]
    print(findDiagonalOrder(mat3))  # Output: [1]

    # Test Case 4
    mat4 = [[1, 2, 3, 4]]
    print(findDiagonalOrder(mat4))  # Output: [1, 2, 3, 4]

    # Test Case 5
    mat5 = [[1], [2], [3], [4]]
    print(findDiagonalOrder(mat5))  # Output: [1, 2, 3, 4]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through all elements of the matrix once, so the time complexity is O(m * n), 
  where `m` is the number of rows and `n` is the number of columns.

Space Complexity:
- The space complexity is O(m * n) due to the storage of elements in the `diagonals` dictionary. 
  Additionally, the `result` list will also store all elements of the matrix, which is O(m * n).

Topic: Arrays
"""