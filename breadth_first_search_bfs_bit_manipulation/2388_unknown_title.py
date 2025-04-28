"""
LeetCode Problem #2388: Minimum Number of Flips to Convert Binary Matrix to Zero Matrix

Problem Statement:
Given a m x n binary matrix mat, you can flip the value of any cell (i, j) in the matrix. 
Flipping a cell changes the value of mat[i][j] from 0 to 1 or from 1 to 0. 
You must also flip the values of all four neighboring cells (if they exist). 
A binary matrix is a matrix where each cell contains either 0 or 1.

Return the minimum number of flips required to convert mat to a zero matrix. 
If it is not possible, return -1.

A binary matrix is a zero matrix if all the cells are 0.

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 3
- mat[i][j] is either 0 or 1.

"""

from collections import deque

def minFlips(mat):
    """
    Function to find the minimum number of flips to convert the binary matrix to a zero matrix.
    If not possible, return -1.
    """
    m, n = len(mat), len(mat[0])
    
    # Helper function to convert matrix to a bitmask
    def matrix_to_bitmask(matrix):
        bitmask = 0
        for i in range(m):
            for j in range(n):
                bitmask |= (matrix[i][j] << (i * n + j))
        return bitmask

    # Helper function to flip a cell and its neighbors
    def flip(bitmask, i, j):
        for x, y in [(i, j), (i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < m and 0 <= y < n:
                bitmask ^= (1 << (x * n + y))
        return bitmask

    # Initial state
    start = matrix_to_bitmask(mat)
    if start == 0:
        return 0

    # BFS to find the minimum flips
    queue = deque([(start, 0)])  # (current bitmask, number of flips)
    visited = set()
    visited.add(start)

    while queue:
        current, flips = queue.popleft()
        for i in range(m):
            for j in range(n):
                next_state = flip(current, i, j)
                if next_state == 0:
                    return flips + 1
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, flips + 1))

    return -1


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
Time and Space Complexity Analysis:

Time Complexity:
- The total number of states is 2^(m*n), where m and n are the dimensions of the matrix.
- For each state, we iterate over all cells (m*n) to compute the next states.
- Therefore, the worst-case time complexity is O((m*n) * 2^(m*n)).

Space Complexity:
- The space required to store the visited states is O(2^(m*n)).
- The queue can also grow up to O(2^(m*n)) in the worst case.
- Therefore, the space complexity is O(2^(m*n)).

Topic: Breadth-First Search (BFS), Bit Manipulation
"""