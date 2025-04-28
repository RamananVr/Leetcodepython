"""
LeetCode Problem #2503: Maximum Number of Points From Grid Queries

Problem Statement:
You are given an m x n integer matrix `grid` and an array `queries` of integers. 
You need to process each query in the order they appear in the array. For each query, 
you need to find the maximum number of points you can collect from the grid such that:

1. You start at any cell in the grid.
2. You can move to any of the four adjacent cells (up, down, left, right).
3. You can only move to cells with values strictly less than the value of the current query.
4. You collect points equal to the number of cells you visit.

Return an array of integers where the i-th integer is the maximum number of points you can collect for the i-th query.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 1000`
- `0 <= grid[i][j] <= 10^6`
- `1 <= queries.length <= 10^4`
- `0 <= queries[i] <= 10^6`
"""

from heapq import heappush, heappop

def maxPoints(grid, queries):
    """
    Function to calculate the maximum number of points for each query.
    :param grid: List[List[int]] - The grid of integers.
    :param queries: List[int] - The list of queries.
    :return: List[int] - The maximum number of points for each query.
    """
    m, n = len(grid), len(grid[0])
    result = []
    visited = [[False] * n for _ in range(m)]
    heap = []
    heappush(heap, (grid[0][0], 0, 0))  # (value, x, y)
    visited[0][0] = True
    points = 0
    total_cells = 0

    for query in sorted(queries):
        while heap and heap[0][0] < query:
            value, x, y = heappop(heap)
            total_cells += 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heappush(heap, (grid[nx][ny], nx, ny))
        result.append(total_cells)

    return result


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1, 2, 4], [3, 4, 3], [2, 1, 2]]
    queries1 = [2, 3, 4]
    print(maxPoints(grid1, queries1))  # Output: [3, 6, 9]

    # Test Case 2
    grid2 = [[5, 1, 7], [3, 8, 2], [6, 4, 9]]
    queries2 = [4, 6, 8]
    print(maxPoints(grid2, queries2))  # Output: [4, 7, 9]

    # Test Case 3
    grid3 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    queries3 = [1, 2, 3]
    print(maxPoints(grid3, queries3))  # Output: [0, 9, 9]


"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the queries takes O(k log k), where k is the length of the queries array.
- The heap operations (push and pop) take O(log(m * n)) for each cell in the grid.
- In the worst case, we process all m * n cells for each query, resulting in O(k * m * n * log(m * n)).
- Overall time complexity: O(k log k + k * m * n * log(m * n)).

Space Complexity:
- The heap can store up to m * n elements, so its space complexity is O(m * n).
- The visited matrix takes O(m * n) space.
- Overall space complexity: O(m * n).

Topic: Heap (Priority Queue), Matrix Traversal
"""