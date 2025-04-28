"""
LeetCode Problem #2084: Minimum Number of Flips to Convert Binary Matrix to Zero Matrix

Problem Statement:
Given a m x n binary matrix mat, you can flip the matrix by toggling each cell (changing 0 to 1 and 1 to 0) 
in a submatrix. In one operation, you can choose any submatrix and flip it. A submatrix is a rectangular 
part of the matrix.

Your goal is to find the minimum number of operations required to convert mat to a zero matrix (a matrix 
with all 0s). If it is not possible, return -1.

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 3
- mat[i][j] is either 0 or 1.

Example:
Input: mat = [[0,0],[0,1]]
Output: 3
Explanation: One possible solution is to flip (1,1) -> (0,1) -> (0,0).

Input: mat = [[0]]
Output: 0
Explanation: The matrix is already a zero matrix.

Input: mat = [[1,1,1],[1,0,1],[0,0,0]]
Output: 6

Input: mat = [[1,0,0],[1,0,0]]
Output: -1
"""

from collections import deque

def minFlips(mat):
    """
    Function to find the minimum number of flips to convert the binary matrix to a zero matrix.
    If not possible, return -1.
    """
    def mat_to_int(matrix):
        """Convert the matrix to an integer representation."""
        state = 0
        for row in matrix:
            for cell in row:
                state = (state << 1) | cell
        return state

    def int_to_mat(state, m, n):
        """Convert an integer representation back to a matrix."""
        matrix = [[0] * n for _ in range(m)]
        for i in range(m * n - 1, -1, -1):
            matrix[i // n][i % n] = state & 1
            state >>= 1
        return matrix

    def flip(matrix, i, j):
        """Flip the cell (i, j) and its neighbors."""
        for x, y in [(i, j), (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                matrix[x][y] ^= 1

    m, n = len(mat), len(mat[0])
    start = mat_to_int(mat)
    target = 0  # All zeros matrix

    # BFS to find the minimum number of flips
    queue = deque([(start, 0)])  # (current state, number of flips)
    visited = set()
    visited.add(start)

    while queue:
        state, flips = queue.popleft()
        if state == target:
            return flips

        # Convert the current state back to a matrix
        matrix = int_to_mat(state, m, n)

        # Try flipping each cell
        for i in range(m):
            for j in range(n):
                flip(matrix, i, j)
                new_state = mat_to_int(matrix)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, flips + 1))
                # Undo the flip to restore the original matrix
                flip(matrix, i, j)

    return -1  # If no solution is found

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [[0, 0], [0, 1]]
    print(minFlips(mat1))  # Output: 3

    # Test Case 2
    mat2 = [[0]]
    print(minFlips(mat2))  # Output: 0

    # Test Case 3
    mat3 = [[1, 1, 1], [1, 0, 1], [0, 0, 0]]
    print(minFlips(mat3))  # Output: 6

    # Test Case 4
    mat4 = [[1, 0, 0], [1, 0, 0]]
    print(minFlips(mat4))  # Output: -1

"""
Time Complexity:
- The total number of states is 2^(m*n), where m and n are the dimensions of the matrix.
- For each state, we perform O(m*n) operations to try flipping each cell.
- Therefore, the time complexity is O((m*n) * 2^(m*n)).

Space Complexity:
- The space complexity is O(2^(m*n)) to store the visited states and the queue.

Topic: Breadth-First Search (BFS), Bit Manipulation
"""