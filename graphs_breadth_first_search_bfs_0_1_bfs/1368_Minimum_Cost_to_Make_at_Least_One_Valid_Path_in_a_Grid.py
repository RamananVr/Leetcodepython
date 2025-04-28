"""
LeetCode Problem #1368: Minimum Cost to Make at Least One Valid Path in a Grid

Problem Statement:
Given an `m x n` grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign can be:
    1. '1' which means go to the cell on the right (east),
    2. '2' which means go to the cell on the left (west),
    3. '3' which means go to the cell on the down (south),
    4. '4' which means go to the cell on the up (north).

You start at the upper-left corner of the grid (0, 0) and you want to reach the bottom-right corner (m-1, n-1) with the minimum cost.

You can change the direction of the sign in a cell with a cost of 1. The cost of changing the direction of a cell is independent of the cell's original direction.

Return the minimum cost to make at least one valid path in the grid.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `1 <= grid[i][j] <= 4`

Example:
Input: grid = [[1,1,1],[1,1,1],[1,1,1]]
Output: 0
Explanation: You don't need to change any cell's direction.

Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
Output: 2
"""

from collections import deque

def minCost(grid):
    """
    Function to calculate the minimum cost to make at least one valid path in the grid.
    :param grid: List[List[int]] - The input grid with directions.
    :return: int - The minimum cost to reach the bottom-right corner.
    """
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
    cost = [[float('inf')] * n for _ in range(m)]
    cost[0][0] = 0
    dq = deque([(0, 0, 0)])  # (row, col, current_cost)

    while dq:
        x, y, c = dq.popleft()
        if c > cost[x][y]:
            continue
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                new_cost = c if grid[x][y] == i + 1 else c + 1
                if new_cost < cost[nx][ny]:
                    cost[nx][ny] = new_cost
                    if grid[x][y] == i + 1:
                        dq.appendleft((nx, ny, new_cost))  # Prioritize no-cost moves
                    else:
                        dq.append((nx, ny, new_cost))  # Add cost moves to the end

    return cost[m - 1][n - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print(minCost(grid1))  # Output: 0

    # Test Case 2
    grid2 = [[1, 1, 3], [3, 2, 2], [1, 1, 4]]
    print(minCost(grid2))  # Output: 2

    # Test Case 3
    grid3 = [[4, 1], [3, 3]]
    print(minCost(grid3))  # Output: 1

    # Test Case 4
    grid4 = [[2, 2, 2], [2, 2, 2]]
    print(minCost(grid4))  # Output: 3

    # Test Case 5
    grid5 = [[1]]
    print(minCost(grid5))  # Output: 0

"""
Time Complexity:
- The algorithm uses a deque to perform a 0-1 BFS. Each cell is processed at most twice (once for a no-cost move and once for a cost move).
- Therefore, the time complexity is O(m * n), where m is the number of rows and n is the number of columns.

Space Complexity:
- The space complexity is O(m * n) due to the cost matrix and the deque.

Topic: Graphs, Breadth-First Search (BFS), 0-1 BFS
"""