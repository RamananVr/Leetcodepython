"""
LeetCode Problem #2247: Maximum Cost of Trip With K Stops

Problem Statement:
You are given a weighted, directed graph represented as an adjacency list. Each node in the graph represents a city, and each edge represents a direct flight between two cities with a given cost. You are also given three integers: `src` (the starting city), `dst` (the destination city), and `k` (the maximum number of stops you can make).

Your task is to find the maximum cost of a trip from `src` to `dst` with at most `k` stops. If there is no such trip, return -1.

Constraints:
- The number of cities (nodes) is `n`, where `1 <= n <= 100`.
- The number of flights (edges) is `m`, where `0 <= m <= 1000`.
- Each flight is represented as a tuple `(u, v, w)` where `u` is the source city, `v` is the destination city, and `w` is the cost of the flight.
- Costs are non-negative integers, and `0 <= w <= 10^4`.
- `0 <= src, dst < n`.
- `0 <= k < n`.

Example:
Input: flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation: The cheapest trip from city 0 to city 2 with at most 1 stop costs 200 (0 -> 1 -> 2).

Note: This problem is a variation of the "Cheapest Flights Within K Stops" problem, but instead of finding the minimum cost, you are tasked with finding the maximum cost.
"""

from collections import defaultdict
import heapq

def findMaximumCost(flights, src, dst, k):
    # Build the graph as an adjacency list
    graph = defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))
    
    # Priority queue to store (negative cost, current city, stops left)
    pq = [(-0, src, k + 1)]
    
    # While there are nodes to process
    while pq:
        cost, city, stops = heapq.heappop(pq)
        cost = -cost  # Convert back to positive
        
        # If we reach the destination, return the cost
        if city == dst:
            return cost
        
        # If we have stops left, explore neighbors
        if stops > 0:
            for neighbor, weight in graph[city]:
                heapq.heappush(pq, (-(cost + weight), neighbor, stops - 1))
    
    # If no valid path is found, return -1
    return -1

# Example Test Cases
if __name__ == "__main__":
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    print(findMaximumCost(flights, src, dst, k))  # Output: 200

    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 0
    print(findMaximumCost(flights, src, dst, k))  # Output: 500

    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500], [2, 3, 200]]
    src = 0
    dst = 3
    k = 2
    print(findMaximumCost(flights, src, dst, k))  # Output: 800

# Time and Space Complexity Analysis
"""
Time Complexity:
- Building the graph takes O(m), where m is the number of flights.
- The priority queue processes each node and its neighbors, leading to O((n + m) * log(n)) in the worst case.

Space Complexity:
- The graph uses O(m) space.
- The priority queue can hold up to O(n) elements in the worst case.
- Overall space complexity is O(n + m).

Primary Topic: Graphs
"""