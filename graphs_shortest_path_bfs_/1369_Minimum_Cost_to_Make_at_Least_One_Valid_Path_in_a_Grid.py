"""
LeetCode Problem #1369: Minimum Cost to Make at Least One Valid Path in a Grid

Problem Statement:
You are given a m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign can be:
    1. '>' which means go to the cell to the right.
    2. '<' which means go to the cell to the left.
    3. '^' which means go to the cell above.
    4. 'v' which means go to the cell below.

You start at the upper-left corner (0, 0) and you want to reach the bottom-right corner (m-1, n-1). You can change the direction of the sign at a cost of 1. Return the minimum cost to make at least one valid path in the grid.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- grid[i][j] is one of {1, 2, 3, 4}.

"""

from collections import deque

def minCost(grid):
    """
    Function to calculate the minimum cost to make at least one valid path in the grid.
    
    :param grid: List[List[int]] - The grid with directional signs.
    :return: int - Minimum cost to reach the bottom-right corner.
    """
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # right, left, up, down
    cost = [[float('inf')] * n for _ in range(m)]
    cost[0][0] = 0
    dq = deque([(0, 0, 0)])  # (x, y, current_cost)

    while dq:
        x, y, c = dq.popleft()
        if c > cost[x][y]:
            continue
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                new_cost = c + (1 if grid[x][y] != i + 1 else 0)
                if new_cost < cost[nx][ny]:
                    cost[nx][ny] = new_cost
                    if grid[x][y] == i + 1:
                        dq.appendleft((nx, ny, new_cost))  # prioritize no-cost moves
                    else:
                        dq.append((nx, ny, new_cost))
    return cost[m-1][n-1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1,1,3],[3,2,2],[1,1,4]]
    print(minCost(grid1))  # Expected Output: 0

    # Test Case 2
    grid2 = [[1,2],[4,3]]
    print(minCost(grid2))  # Expected Output: 1

    # Test Case 3
    grid3 = [[2,2,2],[2,2,2]]
    print(minCost(grid3))  # Expected Output: 3

    # Test Case 4
    grid4 = [[4]]
    print(minCost(grid4))  # Expected Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses a deque to perform a modified BFS. Each cell is processed at most once, and there are m * n cells in the grid.
- For each cell, we check up to 4 directions, so the total complexity is O(m * n * 4) = O(m * n).

Space Complexity:
- The space complexity is dominated by the `cost` matrix and the deque, both of which can store up to m * n elements.
- Therefore, the space complexity is O(m * n).

Topic: Graphs (Shortest Path, BFS)
"""