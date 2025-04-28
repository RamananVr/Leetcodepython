"""
LeetCode Problem #1284: Minimum Number of Flips to Convert Binary Matrix to Zero Matrix

Problem Statement:
Given a m x n binary matrix mat, you can flip the value of a cell (i, j) in the matrix. 
Flipping a cell changes the value of that cell as well as the values of the four neighboring cells 
(up, down, left, right) if they exist. A binary matrix is a matrix with only 0s and 1s.

Your task is to return the minimum number of flips required to convert mat to a zero matrix 
(a matrix with all 0s). If it is not possible, return -1.

A flip operation is defined as toggling the value of a cell and its neighbors:
- If the value is 0, it becomes 1.
- If the value is 1, it becomes 0.

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 3
- mat[i][j] is either 0 or 1.

Example:
Input: mat = [[0,0],[0,1]]
Output: 3
Explanation: One possible solution is to flip (1, 0) -> (0, 1) -> (1, 1).

Input: mat = [[0]]
Output: 0
Explanation: The matrix is already a zero matrix, so no flips are needed.

Input: mat = [[1,1,1],[1,0,1],[0,0,0]]
Output: 6

Input: mat = [[1,0,0],[1,0,0]]
Output: -1
"""

from collections import deque

def minFlips(mat):
    def flip(state, i, j, m, n):
        """Helper function to flip a cell and its neighbors."""
        directions = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < m and 0 <= y < n:
                state ^= (1 << (x * n + y))
        return state

    m, n = len(mat), len(mat[0])
    start_state = 0

    # Convert the matrix into a bitmask representation
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                start_state |= (1 << (i * n + j))

    # BFS to find the minimum number of flips
    queue = deque([(start_state, 0)])  # (current_state, number_of_flips)
    visited = set()
    visited.add(start_state)

    while queue:
        state, flips = queue.popleft()
        if state == 0:  # If the state is a zero matrix
            return flips

        for i in range(m):
            for j in range(n):
                next_state = flip(state, i, j, m, n)
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, flips + 1))

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
- For each state, we iterate over all cells (m*n) to generate the next states.
- Therefore, the time complexity is O((m*n) * 2^(m*n)).

Space Complexity:
- The space complexity is O(2^(m*n)) to store the visited states and the queue.

Topic: Breadth-First Search (BFS), Bit Manipulation
"""