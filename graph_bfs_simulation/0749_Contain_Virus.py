"""
LeetCode Problem #749: Contain Virus

Problem Statement:
A virus is spreading rapidly, and your task is to contain it as much as possible. The virus is spreading on a 2D grid. Each cell in the grid can be in one of three states:
- 0: Empty cell.
- 1: Cell infected by the virus.
- 2: Cell that has been blocked (wall).

Every day, the following happens sequentially:
1. Every infected cell (1) spreads the virus to its neighboring cells (up, down, left, right) if they are empty (0). This happens simultaneously for all infected cells.
2. After the virus spreads, you can choose one region (a group of connected infected cells) and build walls around it to prevent the virus from spreading. The cost of building walls is the number of empty cells adjacent to the region. Once a region is walled off, it becomes fully blocked (state 2).

Return the total number of walls used to contain the virus.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is 0, 1, or 2.

"""

from collections import deque

def containVirus(grid):
    def neighbors(x, y):
        """Helper function to get valid neighbors of a cell."""
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                yield nx, ny

    def bfs(x, y, visited):
        """Perform BFS to find a region of connected infected cells."""
        queue = deque([(x, y)])
        region = set()
        frontier = set()
        walls_needed = 0
        while queue:
            cx, cy = queue.popleft()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))
            region.add((cx, cy))
            for nx, ny in neighbors(cx, cy):
                if grid[nx][ny] == 0:
                    frontier.add((nx, ny))
                    walls_needed += 1
                elif grid[nx][ny] == 1 and (nx, ny) not in visited:
                    queue.append((nx, ny))
        return region, frontier, walls_needed

    total_walls = 0

    while True:
        visited = set()
        regions = []
        frontiers = []
        walls = []

        # Step 1: Identify all regions of infection
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    region, frontier, walls_needed = bfs(i, j, visited)
                    regions.append(region)
                    frontiers.append(frontier)
                    walls.append(walls_needed)

        if not regions:
            break

        # Step 2: Find the region with the largest frontier and contain it
        max_frontier_idx = max(range(len(frontiers)), key=lambda i: len(frontiers[i]))
        total_walls += walls[max_frontier_idx]

        # Contain the most dangerous region
        for x, y in regions[max_frontier_idx]:
            grid[x][y] = 2

        # Step 3: Spread the virus in other regions
        for i in range(len(regions)):
            if i == max_frontier_idx:
                continue
            for x, y in frontiers[i]:
                grid[x][y] = 1

    return total_walls

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [0, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    print(containVirus(grid1))  # Output: 10

    # Test Case 2
    grid2 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    print(containVirus(grid2))  # Output: 4

    # Test Case 3
    grid3 = [
        [1, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0]
    ]
    print(containVirus(grid3))  # Output: 13

"""
Time Complexity:
- Let m = number of rows, n = number of columns.
- In the worst case, we perform BFS for every cell in the grid, leading to O(m * n) per BFS.
- Since the virus spreads and we repeat the process until all regions are contained, the overall complexity is O((m * n)^2).

Space Complexity:
- The space complexity is O(m * n) due to the visited set and BFS queue.

Topic: Graph, BFS, Simulation
"""