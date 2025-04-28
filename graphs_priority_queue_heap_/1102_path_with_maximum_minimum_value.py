"""
LeetCode Question #1102: Path With Maximum Minimum Value

Problem Statement:
You are given an `m x n` integer matrix `grid`. You can move from a cell to any adjacent cell in all 4 directions: up, down, left, or right. 

Return the maximum score of a path starting at the top-left cell `(0, 0)` and ending at the bottom-right cell `(m - 1, n - 1)`.

The score of a path is the minimum value in that path. For example, the score of the path `8 → 4 → 5 → 9` is `4`.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `2 <= m, n <= 100`
- `0 <= grid[i][j] <= 10^9`

You can assume that there is at least one valid path.

---

Solution:
We will use a **priority queue (max-heap)** to implement a modified Dijkstra's algorithm. The idea is to maximize the minimum value along the path. At each step, we explore the neighboring cells and push them into the heap with the minimum value encountered so far along the path.

---

Python Solution:
"""

from heapq import heappush, heappop

def maximumMinimumPath(grid):
    # Dimensions of the grid
    m, n = len(grid), len(grid[0])
    
    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Max-heap to store (-score, x, y), where score is the minimum value along the path
    max_heap = [(-grid[0][0], 0, 0)]
    
    # Visited set to track visited cells
    visited = set()
    visited.add((0, 0))
    
    # While there are cells to process
    while max_heap:
        # Pop the cell with the current maximum score
        score, x, y = heappop(max_heap)
        score = -score  # Convert back to positive
        
        # If we reach the bottom-right cell, return the score
        if x == m - 1 and y == n - 1:
            return score
        
        # Explore all 4 possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                # Push the new cell with the updated score (minimum value along the path)
                heappush(max_heap, (-min(score, grid[nx][ny]), nx, ny))

"""
Example Test Cases:
"""

# Test Case 1
grid1 = [
    [5, 4, 5],
    [1, 2, 6],
    [7, 4, 6]
]
print(maximumMinimumPath(grid1))  # Expected Output: 4

# Test Case 2
grid2 = [
    [2, 2, 1, 2, 2, 2],
    [1, 2, 2, 2, 1, 2]
]
print(maximumMinimumPath(grid2))  # Expected Output: 2

# Test Case 3
grid3 = [
    [3, 4, 6, 3, 4],
    [0, 2, 1, 1, 7],
    [8, 8, 3, 2, 7],
    [3, 2, 4, 9, 8],
    [4, 1, 2, 0, 0],
    [4, 6, 5, 4, 3]
]
print(maximumMinimumPath(grid3))  # Expected Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm processes each cell at most once, and for each cell, we perform a heap operation (push or pop).
- The total number of cells is `m * n`, and each heap operation takes O(log(m * n)).
- Therefore, the time complexity is O(m * n * log(m * n)).

Space Complexity:
- The space required for the heap is O(m * n) in the worst case (all cells are added to the heap).
- The space required for the visited set is also O(m * n).
- Therefore, the space complexity is O(m * n).

---

Topic: Graphs, Priority Queue (Heap)
"""