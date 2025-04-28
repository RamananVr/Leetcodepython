"""
LeetCode Problem #2258: Escape the Spreading Fire

Problem Statement:
You are given a 2D integer grid `grid` of size `m x n` where each cell has one of three values:
- `0` represents an empty cell.
- `1` represents a wall.
- `2` represents a cell containing fire.

You are also given an integer `k`. In one minute, you can move to an adjacent cell (up, down, left, or right). 
You cannot move through walls, and you cannot move into a cell that is on fire or will be on fire in the next `k` minutes.

The fire spreads every minute, and a cell that is adjacent to a cell on fire will catch fire in the next minute.

You start at the top-left corner of the grid (0, 0) and want to reach the bottom-right corner of the grid (m-1, n-1). 
Return the maximum number of minutes you can delay your start such that you can still reach the destination before the fire reaches it. 
If it is impossible to reach the destination, return `-1`.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `2 <= m, n <= 1000`
- `grid[i][j]` is `0`, `1`, or `2`.
- The top-left cell and the bottom-right cell of the grid are always empty (0).

"""

from collections import deque

def maximumMinutes(grid):
    def spread_fire():
        """Simulate fire spreading using BFS."""
        fire_time = [[float('inf')] * n for _ in range(m)]
        queue = deque()
        
        # Initialize fire spread time
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))  # (row, col, time)
                    fire_time[i][j] = 0
        
        while queue:
            x, y, time = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and fire_time[nx][ny] == float('inf'):
                    fire_time[nx][ny] = time + 1
                    queue.append((nx, ny, time + 1))
        
        return fire_time

    def can_escape(start_delay):
        """Check if it's possible to escape with a given start delay."""
        queue = deque([(0, 0, start_delay)])  # (row, col, time)
        visited = set([(0, 0, start_delay)])
        
        while queue:
            x, y, time = queue.popleft()
            
            # If we reach the destination
            if (x, y) == (m - 1, n - 1):
                # Ensure we arrive before or at the same time as the fire
                return time <= fire_time[x][y]
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                    next_time = time + 1
                    if next_time < fire_time[nx][ny] and (nx, ny, next_time) not in visited:
                        visited.add((nx, ny, next_time))
                        queue.append((nx, ny, next_time))
        
        return False

    m, n = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Step 1: Calculate fire spread times
    fire_time = spread_fire()
    
    # Step 2: Binary search for the maximum delay
    left, right, result = 0, m * n, -1
    while left <= right:
        mid = (left + right) // 2
        if can_escape(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [0, 2, 0, 0, 0, 0],
        [0, 2, 0, 1, 1, 0],
        [0, 2, 0, 0, 0, 0],
        [0, 0, 0, 2, 2, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(maximumMinutes(grid1))  # Expected output: 3

    # Test Case 2
    grid2 = [
        [0, 0, 0],
        [0, 1, 0],
        [2, 2, 0]
    ]
    print(maximumMinutes(grid2))  # Expected output: -1

    # Test Case 3
    grid3 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(maximumMinutes(grid3))  # Expected output: 1000000000 (or a very large number)

"""
Time Complexity:
- Fire spread simulation: O(m * n)
- Binary search: O(log(m * n)) iterations
- Escape simulation for each binary search step: O(m * n)
Overall: O((m * n) * log(m * n))

Space Complexity:
- Fire spread time array: O(m * n)
- BFS queue and visited set: O(m * n)
Overall: O(m * n)

Topic: Breadth-First Search (BFS), Binary Search
"""