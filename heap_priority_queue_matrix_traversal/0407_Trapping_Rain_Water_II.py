"""
LeetCode Problem #407: Trapping Rain Water II

Problem Statement:
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, 
return the volume of water it can trap after raining.

The water can only be trapped in cells that are surrounded by higher elevation cells, and the trapped water 
is calculated based on the difference between the height of the current cell and the minimum height of its 
neighboring cells that can trap water.

Constraints:
- m == heightMap.length
- n == heightMap[i].length
- 1 <= m, n <= 200
- 0 <= heightMap[i][j] <= 2 * 10^4
"""

import heapq

def trapRainWater(heightMap):
    """
    Calculate the volume of water that can be trapped in a 2D elevation map.

    :param heightMap: List[List[int]] - 2D matrix representing the height of each cell
    :return: int - Total volume of trapped water
    """
    if not heightMap or not heightMap[0]:
        return 0

    m, n = len(heightMap), len(heightMap[0])
    visited = [[False] * n for _ in range(m)]
    min_heap = []
    
    # Add all boundary cells to the heap
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                heapq.heappush(min_heap, (heightMap[i][j], i, j))
                visited[i][j] = True

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    water_trapped = 0

    while min_heap:
        height, x, y = heapq.heappop(min_heap)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                # Calculate trapped water
                water_trapped += max(0, height - heightMap[nx][ny])
                # Update the cell's height to the max of its own height and the current boundary height
                heapq.heappush(min_heap, (max(height, heightMap[nx][ny]), nx, ny))
                visited[nx][ny] = True

    return water_trapped

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    heightMap1 = [
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]
    ]
    print(trapRainWater(heightMap1))  # Output: 4

    # Test Case 2
    heightMap2 = [
        [3, 3, 3, 3, 3],
        [3, 2, 2, 2, 3],
        [3, 2, 1, 2, 3],
        [3, 2, 2, 2, 3],
        [3, 3, 3, 3, 3]
    ]
    print(trapRainWater(heightMap2))  # Output: 10

    # Test Case 3
    heightMap3 = [
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1]
    ]
    print(trapRainWater(heightMap3))  # Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses a priority queue (min-heap) to process cells, and each cell is pushed and popped from the heap once.
- The heap operations (push and pop) take O(log(m * n)) time, where m * n is the total number of cells.
- Therefore, the overall time complexity is O(m * n * log(m * n)).

Space Complexity:
- The space complexity is O(m * n) due to the `visited` matrix and the heap storage.

Topic: Heap (Priority Queue), Matrix Traversal
"""