"""
LeetCode Problem 2812: Find the Safest Path in a Grid

You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:
- A cell containing a thief if grid[r][c] = 1
- An empty cell if grid[r][c] = 0

You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

The safeness factor of a path is the minimum manhattan distance from any cell in the path to any thief.

Return the maximum safeness factor of a path from (0, 0) to (n - 1, n - 1).

Constraints:
- 1 <= n <= 400
- grid[i][j] is either 0 or 1.
- There is at least one thief in the grid.

Example 1:
Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
Output: 0
Explanation: All paths from (0,0) to (2,2) go through the thieves at (0,0) or (2,2).

Example 2:
Input: grid = [[0,0,1],[0,0,0],[0,0,0]]
Output: 2
Explanation: The path depicted in the above diagram has a safeness factor of 2 since it is the closest we can get to the thief at (2,0).

Example 3:
Input: grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
Output: 2
Explanation: The path depicted in the above diagram has a safeness factor of 2 since it is the closest we can get to the thieves at (0,3) and (3,0).
"""

def maximum_safeness_factor(grid):
    """
    Approach 1: BFS + Binary Search
    
    Use BFS to compute distances to thieves, then binary search on safeness factor.
    
    Time Complexity: O(n^2 * log(n))
    Space Complexity: O(n^2)
    """
    from collections import deque
    
    n = len(grid)
    
    # Step 1: Find all thieves and compute minimum distance to any thief for each cell
    thieves = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                thieves.append((i, j))
    
    # BFS to compute minimum distances
    distances = [[float('inf')] * n for _ in range(n)]
    queue = deque()
    
    for r, c in thieves:
        distances[r][c] = 0
        queue.append((r, c, 0))
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        r, c, dist = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and distances[nr][nc] > dist + 1:
                distances[nr][nc] = dist + 1
                queue.append((nr, nc, dist + 1))
    
    # Step 2: Binary search on the safeness factor
    def can_reach_with_safeness(min_safeness):
        """Check if we can reach destination with given minimum safeness"""
        if distances[0][0] < min_safeness or distances[n-1][n-1] < min_safeness:
            return False
        
        visited = [[False] * n for _ in range(n)]
        queue = deque([(0, 0)])
        visited[0][0] = True
        
        while queue:
            r, c = queue.popleft()
            
            if r == n - 1 and c == n - 1:
                return True
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < n and 0 <= nc < n and 
                    not visited[nr][nc] and distances[nr][nc] >= min_safeness):
                    visited[nr][nc] = True
                    queue.append((nr, nc))
        
        return False
    
    # Binary search on safeness factor
    left, right = 0, n
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if can_reach_with_safeness(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def maximum_safeness_factor_dijkstra(grid):
    """
    Approach 2: Dijkstra's Algorithm
    
    Use Dijkstra to find path with maximum minimum distance.
    
    Time Complexity: O(n^2 * log(n^2))
    Space Complexity: O(n^2)
    """
    import heapq
    from collections import deque
    
    n = len(grid)
    
    # Step 1: Compute distances to nearest thief using multi-source BFS
    distances = [[float('inf')] * n for _ in range(n)]
    queue = deque()
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                distances[i][j] = 0
                queue.append((i, j))
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        r, c = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and distances[nr][nc] == float('inf'):
                distances[nr][nc] = distances[r][c] + 1
                queue.append((nr, nc))
    
    # Step 2: Use Dijkstra to find path with maximum minimum safeness
    # Use negative values in max heap (since Python has min heap)
    pq = [(-distances[0][0], 0, 0)]  # (-safeness, row, col)
    visited = [[False] * n for _ in range(n)]
    
    while pq:
        neg_safeness, r, c = heapq.heappop(pq)
        safeness = -neg_safeness
        
        if visited[r][c]:
            continue
        
        visited[r][c] = True
        
        if r == n - 1 and c == n - 1:
            return safeness
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                new_safeness = min(safeness, distances[nr][nc])
                heapq.heappush(pq, (-new_safeness, nr, nc))
    
    return 0

def maximum_safeness_factor_union_find(grid):
    """
    Approach 3: Union-Find with Sorting
    
    Sort cells by distance and use union-find to check connectivity.
    
    Time Complexity: O(n^2 * log(n^2))
    Space Complexity: O(n^2)
    """
    from collections import deque
    
    n = len(grid)
    
    # Compute distances to nearest thief
    distances = [[float('inf')] * n for _ in range(n)]
    queue = deque()
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                distances[i][j] = 0
                queue.append((i, j))
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and distances[nr][nc] == float('inf'):
                distances[nr][nc] = distances[r][c] + 1
                queue.append((nr, nc))
    
    # Create list of cells sorted by distance
    cells = []
    for i in range(n):
        for j in range(n):
            cells.append((distances[i][j], i, j))
    
    cells.sort(reverse=True)  # Sort by distance in descending order
    
    # Union-Find class
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n
        
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        def union(self, x, y):
            px, py = self.find(x), self.find(y)
            if px == py:
                return
            if self.rank[px] < self.rank[py]:
                px, py = py, px
            self.parent[py] = px
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1
        
        def connected(self, x, y):
            return self.find(x) == self.find(y)
    
    uf = UnionFind(n * n)
    used = [[False] * n for _ in range(n)]
    
    def get_id(r, c):
        return r * n + c
    
    # Process cells in order of decreasing distance
    for dist, r, c in cells:
        used[r][c] = True
        
        # Connect to adjacent used cells
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and used[nr][nc]:
                uf.union(get_id(r, c), get_id(nr, nc))
        
        # Check if start and end are connected
        if uf.connected(get_id(0, 0), get_id(n-1, n-1)):
            return dist
    
    return 0

def maximum_safeness_factor_dp(grid):
    """
    Approach 4: Dynamic Programming
    
    Use DP with state compression for smaller grids.
    
    Time Complexity: O(n^4)
    Space Complexity: O(n^2)
    """
    from collections import deque
    
    n = len(grid)
    
    # Compute distances to nearest thief
    distances = [[float('inf')] * n for _ in range(n)]
    queue = deque()
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                distances[i][j] = 0
                queue.append((i, j))
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and distances[nr][nc] == float('inf'):
                distances[nr][nc] = distances[r][c] + 1
                queue.append((nr, nc))
    
    # DP: dp[r][c] = maximum safeness factor to reach (r, c)
    dp = [[-1] * n for _ in range(n)]
    dp[0][0] = distances[0][0]
    
    # Process in order that ensures we visit cells optimally
    changed = True
    while changed:
        changed = False
        for r in range(n):
            for c in range(n):
                current_safeness = min(dp[r][c] if dp[r][c] != -1 else 0, distances[r][c])
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        new_safeness = min(current_safeness, distances[nr][nc])
                        if dp[nr][nc] < new_safeness:
                            dp[nr][nc] = new_safeness
                            changed = True
    
    return dp[n-1][n-1]

# Test cases
def test_maximum_safeness_factor():
    test_cases = [
        ([[1,0,0],[0,0,0],[0,0,1]], 0),
        ([[0,0,1],[0,0,0],[0,0,0]], 2),
        ([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]], 2),
        ([[1]], 0),
        ([[0,1],[0,0]], 1),
        ([[0,0],[1,0]], 1),
        ([[0,0,0],[0,1,0],[0,0,0]], 1)
    ]
    
    approaches = [
        ("BFS + Binary Search", maximum_safeness_factor),
        ("Dijkstra", maximum_safeness_factor_dijkstra),
        ("Union-Find", maximum_safeness_factor_union_find)
    ]
    
    for approach_name, func in approaches:
        print(f"Testing {approach_name} approach:")
        all_passed = True
        
        for grid, expected in test_cases:
            try:
                result = func([row[:] for row in grid])  # Deep copy
                passed = result == expected
                if not passed:
                    all_passed = False
                
                print(f"  Grid: {grid}")
                print(f"  Expected: {expected}, Got: {result}")
                print(f"  {'✓' if passed else '✗'}")
            except Exception as e:
                print(f"  Grid: {grid}")
                print(f"  Error: {e}")
                print(f"  ✗")
                all_passed = False
        
        print(f"  Overall: {'✓ All Passed' if all_passed else '✗ Some Failed'}\n")

if __name__ == "__main__":
    test_maximum_safeness_factor()

"""
Topics: Arrays, BFS, Binary Search, Dijkstra, Union Find, Graph
Difficulty: Medium

Key Insights:
1. Two-step approach: compute distances to thieves, then find optimal path
2. Multi-source BFS efficiently computes minimum distances
3. Binary search on safeness factor with reachability check
4. Dijkstra finds path with maximum minimum distance
5. Union-Find processes cells by decreasing distance

Companies: Google, Microsoft, Amazon, Meta
"""
