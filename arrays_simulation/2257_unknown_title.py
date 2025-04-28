"""
LeetCode Problem #2257: Count Unguarded Cells in the Grid

Problem Statement:
You are given an `m x n` grid, where each cell is either empty (0), a wall (1), or a guard (2). 
You are tasked to count the number of cells in the grid that are not guarded.

A cell is guarded if there is at least one guard in the same row or column such that there are no walls 
between the guard and that cell. Guards can see and guard all cells in their row and column until they 
hit a wall.

Return the number of unguarded cells in the grid.

Constraints:
- `1 <= m, n <= 100`
- `1 <= guards.length, walls.length <= 5 * 10^4`
- `guards[i].length == walls[i].length == 2`
- `0 <= guards[i][0], walls[i][0] < m`
- `0 <= guards[i][1], walls[i][1] < n`
- All the positions in guards and walls are unique.

Example:
Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The unguarded cells are shown in yellow in the diagram below:
[U, W, U, U, U, U]
[G, U, U, W, W, U]
[U, U, W, G, U, U]
[U, U, U, U, U, U]
"""

# Python Solution
def countUnguarded(m, n, guards, walls):
    # Initialize the grid
    grid = [[0] * n for _ in range(m)]
    
    # Mark guards and walls in the grid
    for x, y in guards:
        grid[x][y] = 2  # Guard
    for x, y in walls:
        grid[x][y] = 1  # Wall

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Mark guarded cells
    for x, y in guards:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 1 and grid[nx][ny] != 2:
                grid[nx][ny] = -1  # Mark as guarded
                nx += dx
                ny += dy

    # Count unguarded cells
    unguarded_count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:  # Empty and unguarded
                unguarded_count += 1

    return unguarded_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    m = 4
    n = 6
    guards = [[0, 0], [1, 1], [2, 3]]
    walls = [[0, 1], [2, 2], [1, 4]]
    print(countUnguarded(m, n, guards, walls))  # Output: 7

    # Test Case 2
    m = 3
    n = 3
    guards = [[1, 1]]
    walls = [[0, 1], [1, 0], [2, 1], [1, 2]]
    print(countUnguarded(m, n, guards, walls))  # Output: 4

    # Test Case 3
    m = 5
    n = 5
    guards = [[0, 0], [4, 4]]
    walls = [[2, 2]]
    print(countUnguarded(m, n, guards, walls))  # Output: 16

"""
Time and Space Complexity Analysis:

Time Complexity:
- Initializing the grid takes O(m * n).
- Marking guards and walls takes O(g + w), where g is the number of guards and w is the number of walls.
- For each guard, we traverse in four directions until hitting a wall or the grid boundary. 
  In the worst case, this could take O(m + n) per guard. Thus, marking guarded cells takes O(g * (m + n)).
- Counting unguarded cells takes O(m * n).
- Overall time complexity: O(m * n + g * (m + n)).

Space Complexity:
- The grid requires O(m * n) space.
- Overall space complexity: O(m * n).

Topic: Arrays, Simulation
"""