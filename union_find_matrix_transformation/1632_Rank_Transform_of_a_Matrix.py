"""
LeetCode Problem #1632: Rank Transform of a Matrix

Problem Statement:
Given an m x n matrix, return a new matrix answer where answer[i][j] is the rank of matrix[i][j].

The rank is an integer that represents how large an element is compared to other elements. It is calculated using the following rules:
1. The rank is an integer starting from 1.
2. If two elements are in the same row or column, then they must not have the same rank.
3. The rank should be as small as possible.

The rank of an element is determined by considering all elements in its row and column. If an element is larger than another element in its row or column, its rank should be greater. If two elements are equal, they should have the same rank.

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 500
- -10^9 <= matrix[i][j] <= 10^9
"""

from collections import defaultdict

def matrixRankTransform(matrix):
    m, n = len(matrix), len(matrix[0])
    rank = [0] * (m + n)  # Keeps track of the rank for rows and columns

    # Step 1: Group all elements by their value
    value_to_positions = defaultdict(list)
    for i in range(m):
        for j in range(n):
            value_to_positions[matrix[i][j]].append((i, j))

    # Step 2: Process each value in sorted order
    for value in sorted(value_to_positions):
        # Union-Find to manage connected components
        parent = {}
        size = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_y] = root_x
                size[root_x] = max(size[root_x], size[root_y])

        # Initialize Union-Find for rows and columns
        for i, j in value_to_positions[value]:
            if i not in parent:
                parent[i] = i
                size[i] = rank[i]
            if j + m not in parent:
                parent[j + m] = j + m
                size[j + m] = rank[j + m]
            union(i, j + m)

        # Determine the rank for each group
        rank2 = {}
        for i, j in value_to_positions[value]:
            root = find(i)
            rank2[root] = size[root] + 1

        # Update the rank and the answer matrix
        for i, j in value_to_positions[value]:
            root = find(i)
            rank[i] = rank[j + m] = matrix[i][j] = rank2[root]

    return matrix

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    matrix1 = [[1, 2], [3, 4]]
    print(matrixRankTransform(matrix1))  # Expected Output: [[1, 2], [2, 3]]

    # Test Case 2
    matrix2 = [[7, 7], [7, 7]]
    print(matrixRankTransform(matrix2))  # Expected Output: [[1, 1], [1, 1]]

    # Test Case 3
    matrix3 = [[20, -21, 14], [-19, 4, 19], [22, -47, 24], [-19, 4, 19]]
    print(matrixRankTransform(matrix3))  # Expected Output: [[4, 2, 3], [1, 3, 4], [5, 1, 6], [1, 3, 4]]

    # Test Case 4
    matrix4 = [[-37, -50, -3, 44], [-37, 46, 13, -32], [47, -42, -3, -40], [-17, -22, -39, 24]]
    print(matrixRankTransform(matrix4))  # Expected Output: [[2, 1, 4, 6], [2, 6, 5, 3], [7, 2, 4, 1], [4, 3, 1, 5]]

# Time and Space Complexity Analysis
# Time Complexity: O((m * n) * log(m * n))
# - Sorting the values takes O(m * n * log(m * n)).
# - Union-Find operations are nearly constant time due to path compression and union by rank.

# Space Complexity: O(m + n)
# - The rank array and Union-Find structures use O(m + n) space.

# Topic: Union-Find, Matrix Transformation