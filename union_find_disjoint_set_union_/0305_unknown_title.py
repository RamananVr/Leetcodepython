"""
LeetCode Problem #305: Number of Islands II

Problem Statement:
You are given an empty 2D binary grid `grid` of size `m x n`. The grid represents a map where `0` represents water and `1` represents land. Initially, all the cells of the grid are water (`0`).

We may perform an addLand operation, which turns the water at position (row, col) into land. Given a list of positions to operate on, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

Implement the function:
    def numIslands2(m: int, n: int, positions: List[List[int]]) -> List[int]

Input:
- `m` and `n` represent the dimensions of the grid.
- `positions` is a list of positions where land is added.

Output:
- Return a list of integers representing the number of islands after each addLand operation.

Constraints:
- 1 <= m, n <= 10^4
- 1 <= positions.length <= 10^4
- positions[i].length == 2
- 0 <= positions[i][0] < m
- 0 <= positions[i][1] < n

Example:
Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1, 1, 2, 3]
"""

from typing import List

def numIslands2(m: int, n: int, positions: List[List[int]]) -> List[int]:
    # Helper function to find the root of a node in the Union-Find structure
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    # Helper function to union two nodes
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootX] = rootY
            return True
        return False

    # Initialize variables
    parent = {}
    rank = {}
    count = 0  # Number of islands
    result = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    for r, c in positions:
        if (r, c) in parent:  # Skip if land is already added
            result.append(count)
            continue

        # Add the new land
        parent[(r, c)] = (r, c)
        rank[(r, c)] = 0
        count += 1  # New land means a new island

        # Check all 4 directions to merge islands if necessary
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (nr, nc) in parent:  # If the neighbor is land
                if union((r, c), (nr, nc)):
                    count -= 1  # Merging two islands reduces the count

        result.append(count)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    m = 3
    n = 3
    positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
    print(numIslands2(m, n, positions))  # Output: [1, 1, 2, 3]

    # Test Case 2
    m = 3
    n = 3
    positions = [[0, 0], [1, 1], [0, 1], [1, 0], [1, 2]]
    print(numIslands2(m, n, positions))  # Output: [1, 2, 1, 1, 1]

    # Test Case 3
    m = 1
    n = 1
    positions = [[0, 0]]
    print(numIslands2(m, n, positions))  # Output: [1]

"""
Time Complexity:
- The `find` operation uses path compression, and the `union` operation uses union by rank. 
  These operations are nearly constant time, O(α(N)), where α is the inverse Ackermann function.
- For each position, we perform a constant number of `find` and `union` operations, so the total time complexity is O(P * α(N)), where P is the number of positions.

Space Complexity:
- The space complexity is O(N), where N is the number of cells in the grid, due to the storage of the Union-Find parent and rank dictionaries.

Topic: Union-Find (Disjoint Set Union)
"""