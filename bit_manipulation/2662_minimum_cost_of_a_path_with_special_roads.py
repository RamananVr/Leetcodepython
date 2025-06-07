"""
LeetCode Question #2662: Minimum Cost of a Path With Special Roads

Problem Statement:
You are given an array start where start = [startX, startY] represents your initial position (startX, startY) in a 2D space. You are also given the array target where target = [targetX, targetY] represents your target position (targetX, targetY).

The cost of going from position (x1, y1) to any other position in the space (x2, y2) is |x1 - x2| + |y1 - y2|.

There are also some special roads. You are given a 2D array specialRoads where specialRoads[i] = [x1i, y1i, x2i, y2i, costi] indicates that the ith special road can take you from (x1i, y1i) to (x2i, y2i) with a cost of costi. You can use each special road any number of times.

Return the minimum cost required to go from (startX, startY) to (targetX, targetY).

Examples:
Example 1:
Input: start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]
Output: 5
Explanation: The optimal path from (1,1) to (4,5) is the following:
- (1,1) -> (1,2). This is a normal move with cost |1-1| + |1-2| = 1.
- (1,2) -> (3,3). This is a special road with cost 2.
- (3,3) -> (3,4). This is a normal move with cost |3-3| + |3-4| = 1.
- (3,4) -> (4,5). This is a special road with cost 1.
So the total cost is 1 + 2 + 1 + 1 = 5.

Example 2:
Input: start = [3,2], target = [5,7], specialRoads = [[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]
Output: 7
Explanation: It is optimal to not use any special road and go directly from start to target with cost |3-5| + |2-7| = 7.

Constraints:
- start.length == target.length == 2
- 1 <= startX, startY, targetX, targetY <= 10^5
- 1 <= specialRoads.length <= 200
- specialRoads[i].length == 5
- startX <= x1i, x2i <= targetX
- startY <= y1i, y2i <= targetY
- 1 <= costi <= 10^5
"""

from typing import List
import heapq

def minimumCost(start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
    """
    Find minimum cost path using Dijkstra's algorithm.
    
    We treat this as a shortest path problem where:
    - Nodes are important points (start, target, special road endpoints)
    - Edges are either Manhattan distance or special roads
    """
    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    # Collect all important points
    points = set()
    points.add(tuple(start))
    points.add(tuple(target))
    
    for road in specialRoads:
        points.add((road[0], road[1]))  # start of special road
        points.add((road[2], road[3]))  # end of special road
    
    points = list(points)
    point_to_idx = {point: i for i, point in enumerate(points)}
    n = len(points)
    
    # Build graph
    graph = [[] for _ in range(n)]
    
    # Add normal movement edges (Manhattan distance)
    for i in range(n):
        for j in range(n):
            if i != j:
                cost = manhattan_distance(points[i], points[j])
                graph[i].append((j, cost))
    
    # Add special road edges
    for x1, y1, x2, y2, cost in specialRoads:
        start_idx = point_to_idx[(x1, y1)]
        end_idx = point_to_idx[(x2, y2)]
        # Only add if special road is cheaper than Manhattan distance
        manhattan_cost = manhattan_distance((x1, y1), (x2, y2))
        if cost < manhattan_cost:
            graph[start_idx].append((end_idx, cost))
    
    # Dijkstra's algorithm
    start_idx = point_to_idx[tuple(start)]
    target_idx = point_to_idx[tuple(target)]
    
    dist = [float('inf')] * n
    dist[start_idx] = 0
    pq = [(0, start_idx)]
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if current_dist > dist[u]:
            continue
        
        if u == target_idx:
            return current_dist
        
        for v, weight in graph[u]:
            new_dist = current_dist + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    
    return dist[target_idx]

def minimumCostSimplified(start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
    """
    Simplified approach - directly compute minimum cost without building explicit graph.
    """
    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    # Direct path cost
    direct_cost = manhattan_distance(start, target)
    min_cost = direct_cost
    
    # Try using each special road
    for x1, y1, x2, y2, road_cost in specialRoads:
        # Cost: start -> road_start + road_cost + road_end -> target
        cost_to_road_start = manhattan_distance(start, [x1, y1])
        cost_from_road_end = manhattan_distance([x2, y2], target)
        total_cost = cost_to_road_start + road_cost + cost_from_road_end
        min_cost = min(min_cost, total_cost)
    
    # Try combinations of special roads (simplified approach)
    # This doesn't handle all cases optimally but works for most inputs
    return min_cost

def minimumCostDP(start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
    """
    Dynamic programming approach with state compression.
    """
    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    # Collect unique points
    points = {tuple(start), tuple(target)}
    for road in specialRoads:
        points.add((road[0], road[1]))
        points.add((road[2], road[3]))
    
    points = list(points)
    n = len(points)
    
    # DP: minimum cost to reach each point
    dp = [float('inf')] * n
    start_idx = points.index(tuple(start))
    target_idx = points.index(tuple(target))
    dp[start_idx] = 0
    
    # Relax edges multiple times (Bellman-Ford style)
    for _ in range(n):
        updated = False
        
        # Normal movement
        for i in range(n):
            if dp[i] == float('inf'):
                continue
            for j in range(n):
                cost = manhattan_distance(points[i], points[j])
                if dp[i] + cost < dp[j]:
                    dp[j] = dp[i] + cost
                    updated = True
        
        # Special roads
        for x1, y1, x2, y2, cost in specialRoads:
            start_pt_idx = points.index((x1, y1))
            end_pt_idx = points.index((x2, y2))
            if dp[start_pt_idx] + cost < dp[end_pt_idx]:
                dp[end_pt_idx] = dp[start_pt_idx] + cost
                updated = True
        
        if not updated:
            break
    
    return dp[target_idx]

# Test Cases
if __name__ == "__main__":
    test_cases = [
        ([1, 1], [4, 5], [[1, 2, 3, 3, 2], [3, 4, 4, 5, 1]], 5),
        ([3, 2], [5, 7], [[3, 2, 3, 4, 4], [3, 3, 5, 5, 5], [3, 4, 5, 6, 6]], 7),
        ([1, 1], [10, 10], [], 18),  # No special roads
        ([0, 0], [2, 2], [[0, 0, 2, 2, 1]], 1),  # Special road is optimal
        ([0, 0], [5, 5], [[0, 0, 3, 3, 8], [3, 3, 5, 5, 2]], 10)  # Use both special roads
    ]
    
    print("Testing Dijkstra approach:")
    for start, target, specialRoads, expected in test_cases:
        result = minimumCost(start, target, specialRoads)
        print(f"minimumCost({start}, {target}, {specialRoads}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting simplified approach:")
    for start, target, specialRoads, expected in test_cases:
        result = minimumCostSimplified(start, target, specialRoads)
        print(f"minimumCostSimplified({start}, {target}, {specialRoads}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting DP approach:")
    for start, target, specialRoads, expected in test_cases:
        result = minimumCostDP(start, target, specialRoads)
        print(f"minimumCostDP({start}, {target}, {specialRoads}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")

"""
Time and Space Complexity Analysis:

Dijkstra Approach:
Time Complexity: O(V^2 log V + E) where V = number of unique points, E = edges
- V ≤ 2 + 2*R where R = number of special roads
- Building graph: O(V^2)
- Dijkstra: O(V^2 log V)
Space Complexity: O(V^2) - for storing the graph

Simplified Approach:
Time Complexity: O(R) where R = number of special roads
Space Complexity: O(1) - only using constant extra space
Note: This doesn't handle chaining special roads optimally

DP Approach:
Time Complexity: O(V^3 + V*R) - Bellman-Ford style relaxation
Space Complexity: O(V) - DP array

Key Insights:
1. This is a shortest path problem on a graph
2. Important points are start, target, and special road endpoints
3. Need to consider both Manhattan distance and special roads
4. Dijkstra's algorithm gives optimal solution
5. Special roads should only be used if they're beneficial

Topic: Graph, Shortest Path, Dijkstra, Dynamic Programming, Manhattan Distance
"""
