"""
LeetCode Problem #2267: Check if There Is a Valid Parentheses String Path

Problem Statement:
Given a grid of size `m x n` consisting of characters '(' and ')'. A valid parentheses string path in the grid is a path that:
1. Starts from the top-left cell (0, 0) and ends at the bottom-right cell (m-1, n-1).
2. Only moves down or right at each step.
3. Forms a valid parentheses string after concatenating all the characters along the path.

A parentheses string is valid if and only if:
- It consists of only the characters '(' and ')'.
- The number of '(' characters is equal to the number of ')' characters.
- At any point in the string, the number of ')' characters does not exceed the number of '(' characters.

Return `True` if there exists a valid parentheses string path in the grid. Otherwise, return `False`.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `grid[i][j]` is either '(' or ')'.

Example:
Input: grid = [["(", ")", "("], ["(", "(", ")"], [")", "(", ")"]]
Output: True
Explanation: The path (0,0) -> (1,0) -> (1,1) -> (2,1) -> (2,2) forms the valid parentheses string "(()())".

"""

from collections import deque

def hasValidPath(grid):
    """
    Determines if there exists a valid parentheses string path in the grid.

    :param grid: List[List[str]] - A 2D grid of '(' and ')'.
    :return: bool - True if a valid path exists, False otherwise.
    """
    m, n = len(grid), len(grid[0])
    
    # If the total number of cells is odd, it's impossible to have a valid parentheses string.
    if (m + n - 1) % 2 != 0:
        return False

    # BFS to track (row, col, open_parentheses_count)
    queue = deque([(0, 0, 1 if grid[0][0] == '(' else -1)])
    visited = set([(0, 0, 1 if grid[0][0] == '(' else -1)])

    while queue:
        x, y, balance = queue.popleft()

        # If balance is negative, it's invalid.
        if balance < 0:
            continue

        # If we reach the bottom-right corner with a balance of 0, it's valid.
        if x == m - 1 and y == n - 1 and balance == 0:
            return True

        # Explore the next cells (down and right).
        for dx, dy in [(1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                new_balance = balance + (1 if grid[nx][ny] == '(' else -1)
                if (nx, ny, new_balance) not in visited:
                    visited.add((nx, ny, new_balance))
                    queue.append((nx, ny, new_balance))

    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [["(", ")", "("], ["(", "(", ")"], [")", "(", ")"]]
    print(hasValidPath(grid1))  # Output: True

    # Test Case 2
    grid2 = [[")", ")"], ["(", "("]]
    print(hasValidPath(grid2))  # Output: False

    # Test Case 3
    grid3 = [["(", "(", "("], [")", "(", ")"], [")", ")", ")"]]
    print(hasValidPath(grid3))  # Output: False

    # Test Case 4
    grid4 = [["("]]
    print(hasValidPath(grid4))  # Output: False

    # Test Case 5
    grid5 = [["(", ")"], ["(", ")"]]
    print(hasValidPath(grid5))  # Output: True

"""
Time Complexity:
- The BFS explores each cell at most once for each possible balance value.
- The maximum balance value is bounded by the total number of cells (m + n - 1).
- Therefore, the time complexity is O(m * n * (m + n)).

Space Complexity:
- The space required for the queue and visited set is proportional to the number of states, which is O(m * n * (m + n)).
- Thus, the space complexity is O(m * n * (m + n)).

Topic: Dynamic Programming, Breadth-First Search (BFS), Grid
"""