"""
LeetCode Problem #864: Shortest Path to Get All Keys

Problem Statement:
You are given an m x n grid grid where:
- '.' is an empty cell.
- '#' is a wall.
- '@' is the starting point.
- Lowercase letters represent keys.
- Uppercase letters represent locks.

You start at the starting point and one move consists of walking one space in one of the four cardinal directions. 
You cannot walk outside the grid, or walk into a wall, or walk into a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. 
This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the minimum number of moves to acquire all keys. If it is impossible, return -1.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 30
- grid[i][j] is either an English letter, '.', '#', or '@'.
- The number of keys in the grid is in the range [1, 6].
- Each key in the grid is unique.
- Each key has a matching lock.

"""

from collections import deque

def shortestPathAllKeys(grid):
    # Dimensions of the grid
    m, n = len(grid), len(grid[0])
    
    # Find the starting point and the number of keys
    start = None
    total_keys = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                start = (i, j)
            elif 'a' <= grid[i][j] <= 'f':
                total_keys += 1
    
    # Directions for moving in the grid
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # BFS queue: (x, y, keys_collected_bitmask, steps)
    queue = deque([(start[0], start[1], 0, 0)])
    visited = set((start[0], start[1], 0))
    
    # Target bitmask when all keys are collected
    target_keys = (1 << total_keys) - 1
    
    while queue:
        x, y, keys, steps = queue.popleft()
        
        # If all keys are collected, return the number of steps
        if keys == target_keys:
            return steps
        
        # Explore all 4 directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check if the new position is within bounds
            if 0 <= nx < m and 0 <= ny < n:
                cell = grid[nx][ny]
                
                # If it's a wall, skip
                if cell == '#':
                    continue
                
                # If it's a lock, check if we have the corresponding key
                if 'A' <= cell <= 'F' and not (keys & (1 << (ord(cell) - ord('A')))):
                    continue
                
                # If it's a key, update the keys bitmask
                new_keys = keys
                if 'a' <= cell <= 'f':
                    new_keys |= (1 << (ord(cell) - ord('a')))
                
                # If this state has not been visited, add it to the queue
                if (nx, ny, new_keys) not in visited:
                    visited.add((nx, ny, new_keys))
                    queue.append((nx, ny, new_keys, steps + 1))
    
    # If we exhaust the queue without collecting all keys, return -1
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = ["@.a.#", "###.#", "b.A.B"]
    print(shortestPathAllKeys(grid1))  # Output: 8

    # Test Case 2
    grid2 = ["@..aA", "..B#.", "....b"]
    print(shortestPathAllKeys(grid2))  # Output: 6

    # Test Case 3
    grid3 = ["@Aa"]
    print(shortestPathAllKeys(grid3))  # Output: -1

"""
Time Complexity:
- The total number of states is O(m * n * 2^k), where m and n are the dimensions of the grid, and k is the number of keys (at most 6).
- For each state, we process it in O(1) time.
- Thus, the overall time complexity is O(m * n * 2^k).

Space Complexity:
- The space required for the visited set and the queue is O(m * n * 2^k).
- Thus, the overall space complexity is O(m * n * 2^k).

Topic: Breadth-First Search (BFS), Bitmasking
"""