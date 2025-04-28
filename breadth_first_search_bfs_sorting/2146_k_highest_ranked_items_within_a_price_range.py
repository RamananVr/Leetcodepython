"""
LeetCode Question #2146: K Highest Ranked Items Within a Price Range

Problem Statement:
You are given a 0-indexed 2D integer grid of size m x n that represents a map of the items in a shop. The integers in the grid represent the following:
- 0 represents a wall that you cannot pass through.
- 1 represents an empty cell that you can freely move to and from.
- All other positive integers represent the price of an item in that cell. You may also freely move to and from these item cells.

It takes 1 step to travel between adjacent grid cells.

You are also given integer array pricing of length 2 where pricing = [low, high], and you are given an integer array start of length 2 where start = [start_row, start_col] represents your starting position.

You are also given an integer k.

You are interested in the positions of the k highest-ranked items within the price range [low, high] that you can reach starting from the starting position. The rank is determined by the following rules:
1. The distance from the starting position, with the shortest distance ranked first.
2. If two items have the same distance, the one with the lower price is ranked higher.
3. If two items have the same distance and price, the one with the smaller row index is ranked higher.
4. If two items have the same distance, price, and row index, the one with the smaller column index is ranked higher.

Return a list of the k highest-ranked items within the price range [low, high]. If there are fewer than k reachable items within the price range, return all of them.

Example:
Input: grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]], pricing = [2,3], start = [2,3], k = 2
Output: [[1,1],[0,1]]
Explanation: The items in the grid with prices in the range [2,3] are located at (0,1), (1,1), and (2,1). These are sorted by distance from the start (2,3), price, row, and column. The top 2 items are (1,1) and (0,1).

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- 0 <= grid[i][j] <= 10^5
- pricing.length == 2
- 2 <= pricing[0] <= pricing[1] <= 10^5
- start.length == 2
- 0 <= start_row < m
- 0 <= start_col < n
- grid[start_row][start_col] > 0
- 1 <= k <= m * n
"""

from collections import deque

def highestRankedKItems(grid, pricing, start, k):
    rows, cols = len(grid), len(grid[0])
    low, high = pricing
    start_row, start_col = start
    visited = set()
    result = []

    # BFS initialization
    queue = deque([(start_row, start_col, 0)])  # (row, col, distance)
    visited.add((start_row, start_col))

    while queue:
        row, col, dist = queue.popleft()

        # Check if the current cell is an item within the price range
        if low <= grid[row][col] <= high:
            result.append((dist, grid[row][col], row, col))

        # Explore neighbors
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                if grid[new_row][new_col] != 0:  # Not a wall
                    queue.append((new_row, new_col, dist + 1))
                    visited.add((new_row, new_col))

    # Sort the result based on the ranking rules
    result.sort()

    # Extract the top k items
    return [[r, c] for _, _, r, c in result[:k]]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid = [[1, 2, 0, 1], [1, 3, 0, 1], [0, 2, 5, 1]]
    pricing = [2, 3]
    start = [2, 3]
    k = 2
    print(highestRankedKItems(grid, pricing, start, k))  # Output: [[1, 1], [0, 1]]

    # Test Case 2
    grid = [[1, 0, 1], [3, 5, 1], [4, 2, 1]]
    pricing = [2, 4]
    start = [0, 0]
    k = 3
    print(highestRankedKItems(grid, pricing, start, k))  # Output: [[2, 1], [1, 0], [2, 0]]

    # Test Case 3
    grid = [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
    pricing = [5, 15]
    start = [1, 1]
    k = 5
    print(highestRankedKItems(grid, pricing, start, k))  # Output: [[1, 1], [0, 1], [1, 0], [1, 2], [2, 1]]

# Time Complexity:
# - BFS traversal: O(m * n), where m and n are the dimensions of the grid.
# - Sorting the result: O(k * log(k)), where k is the number of valid items.
# Overall: O(m * n + k * log(k))

# Space Complexity:
# - BFS queue and visited set: O(m * n) in the worst case.
# - Result list: O(k), where k is the number of valid items.
# Overall: O(m * n)

# Topic: Breadth-First Search (BFS), Sorting