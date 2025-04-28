"""
LeetCode Problem #1267: Count Servers that Communicate

Problem Statement:
You are given a map of a server center, represented as a `m x n` integer matrix `grid`, where `grid[i][j] = 1` represents a server at location `(i, j)`, and `grid[i][j] = 0` means no server is present. Two servers are said to communicate if they are in the same row or in the same column.

Return the number of servers that communicate with at least one other server.

Example 1:
Input: grid = [[1, 0], [0, 1]]
Output: 0
Explanation: No servers can communicate with each other.

Example 2:
Input: grid = [[1, 0], [1, 1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.

Example 3:
Input: grid = [[1, 1, 0], [0, 0, 1], [1, 0, 0]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. 
The server in the third row can communicate with the server in the first column.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m <= 250`
- `1 <= n <= 250`
- `grid[i][j] == 0 or 1`
"""

def countServers(grid):
    """
    Function to count the number of servers that can communicate with at least one other server.

    :param grid: List[List[int]] - 2D grid representing the server center
    :return: int - Number of servers that can communicate
    """
    m, n = len(grid), len(grid[0])
    row_count = [0] * m
    col_count = [0] * n

    # Count the number of servers in each row and column
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                row_count[i] += 1
                col_count[j] += 1

    # Count the servers that can communicate
    result = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                result += 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1, 0], [0, 1]]
    print(countServers(grid1))  # Output: 0

    # Test Case 2
    grid2 = [[1, 0], [1, 1]]
    print(countServers(grid2))  # Output: 3

    # Test Case 3
    grid3 = [[1, 1, 0], [0, 0, 1], [1, 0, 0]]
    print(countServers(grid3))  # Output: 4

    # Test Case 4
    grid4 = [[1, 1], [1, 0]]
    print(countServers(grid4))  # Output: 3

    # Test Case 5
    grid5 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(countServers(grid5))  # Output: 0

"""
Time Complexity:
- Counting servers in rows and columns takes O(m * n), where m is the number of rows and n is the number of columns.
- Iterating through the grid again to count communicable servers also takes O(m * n).
- Overall time complexity: O(m * n).

Space Complexity:
- We use two auxiliary arrays, `row_count` and `col_count`, each of size O(m) and O(n), respectively.
- Overall space complexity: O(m + n).

Topic: Arrays
"""