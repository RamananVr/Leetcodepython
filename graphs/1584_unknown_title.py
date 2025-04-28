"""
LeetCode Problem #1584: Min Cost to Connect All Points

Problem Statement:
You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`.

The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the Manhattan distance between them:
    |xi - xj| + |yi - yj|.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Constraints:
- 1 <= points.length <= 1000
- -10^6 <= xi, yi <= 10^6
- All pairs `(xi, yi)` are distinct.
"""

from heapq import heappop, heappush

def minCostConnectPoints(points):
    """
    Function to calculate the minimum cost to connect all points using Prim's algorithm.
    :param points: List[List[int]] - List of points on a 2D plane.
    :return: int - Minimum cost to connect all points.
    """
    n = len(points)
    visited = [False] * n
    min_heap = [(0, 0)]  # (cost, point_index)
    total_cost = 0
    edges_used = 0

    while edges_used < n:
        cost, curr = heappop(min_heap)
        if visited[curr]:
            continue
        visited[curr] = True
        total_cost += cost
        edges_used += 1

        for next_point in range(n):
            if not visited[next_point]:
                next_cost = abs(points[curr][0] - points[next_point][0]) + abs(points[curr][1] - points[next_point][1])
                heappush(min_heap, (next_cost, next_point))

    return total_cost

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    points1 = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(minCostConnectPoints(points1))  # Expected Output: 20

    # Test Case 2
    points2 = [[3, 12], [-2, 5], [-4, 1]]
    print(minCostConnectPoints(points2))  # Expected Output: 18

    # Test Case 3
    points3 = [[0, 0], [1, 1], [1, 0], [-1, 1]]
    print(minCostConnectPoints(points3))  # Expected Output: 4

    # Test Case 4
    points4 = [[-1000000, -1000000], [1000000, 1000000]]
    print(minCostConnectPoints(points4))  # Expected Output: 4000000

    # Test Case 5
    points5 = [[0, 0]]
    print(minCostConnectPoints(points5))  # Expected Output: 0

"""
Time Complexity Analysis:
- The algorithm uses Prim's algorithm with a priority queue (min-heap).
- For each of the `n` points, we push and pop from the heap, which takes O(log n) time.
- For each point, we calculate the Manhattan distance to all other points, which takes O(n) time.
- Overall, the time complexity is O(n^2 log n), where `n` is the number of points.

Space Complexity Analysis:
- The space complexity is O(n^2) for storing all possible edges in the heap in the worst case.
- Additionally, we use O(n) space for the visited array.
- Overall, the space complexity is O(n^2).

Topic: Graphs
"""