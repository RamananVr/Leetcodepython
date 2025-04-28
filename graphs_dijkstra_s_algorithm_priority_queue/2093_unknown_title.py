"""
LeetCode Problem #2093: Minimum Cost to Reach City With Discounts

Problem Statement:
You are given a weighted undirected graph consisting of `n` cities numbered from `0` to `n - 1`, and an array `edges` where `edges[i] = [u_i, v_i, w_i]` represents a bidirectional road that connects cities `u_i` and `v_i` with a cost of `w_i`.

You are also given an integer `discounts` which represents the number of discounts you can use. You can use at most one discount per road, and a discount allows you to travel a road for half its original cost (rounded down to the nearest integer).

Return the minimum cost to travel from city `0` to city `n - 1`. If it is impossible to reach city `n - 1`, return `-1`.

Constraints:
- `2 <= n <= 1000`
- `1 <= edges.length <= 10000`
- `edges[i].length == 3`
- `0 <= u_i, v_i < n`
- `1 <= w_i <= 10^6`
- `0 <= discounts <= 100`

"""

import heapq
from math import inf

def minimumCost(n: int, edges: list[list[int]], discounts: int) -> int:
    # Build adjacency list
    graph = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Priority queue for Dijkstra's algorithm
    pq = [(0, 0, discounts)]  # (current_cost, current_city, remaining_discounts)
    # Visited dictionary to track the minimum cost to reach a city with a specific number of discounts
    visited = {}
    
    while pq:
        cost, city, remaining_discounts = heapq.heappop(pq)
        
        # If we reach the destination city
        if city == n - 1:
            return cost
        
        # If this state has been visited with a lower cost, skip it
        if (city, remaining_discounts) in visited and visited[(city, remaining_discounts)] <= cost:
            continue
        visited[(city, remaining_discounts)] = cost
        
        # Explore neighbors
        for neighbor, weight in graph[city]:
            # Without using a discount
            heapq.heappush(pq, (cost + weight, neighbor, remaining_discounts))
            
            # Using a discount (if available)
            if remaining_discounts > 0:
                discounted_cost = cost + weight // 2
                heapq.heappush(pq, (discounted_cost, neighbor, remaining_discounts - 1))
    
    # If we exhaust the priority queue without reaching the destination
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 5
    edges1 = [[0, 1, 4], [0, 2, 3], [1, 2, 1], [1, 3, 2], [2, 3, 4], [3, 4, 2]]
    discounts1 = 1
    print(minimumCost(n1, edges1, discounts1))  # Expected Output: 4

    # Test Case 2
    n2 = 3
    edges2 = [[0, 1, 1], [1, 2, 1], [0, 2, 3]]
    discounts2 = 1
    print(minimumCost(n2, edges2, discounts2))  # Expected Output: 1

    # Test Case 3
    n3 = 4
    edges3 = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [0, 3, 100]]
    discounts3 = 2
    print(minimumCost(n3, edges3, discounts3))  # Expected Output: 15

    # Test Case 4
    n4 = 2
    edges4 = [[0, 1, 5]]
    discounts4 = 0
    print(minimumCost(n4, edges4, discounts4))  # Expected Output: 5

    # Test Case 5
    n5 = 2
    edges5 = [[0, 1, 5]]
    discounts5 = 1
    print(minimumCost(n5, edges5, discounts5))  # Expected Output: 2

"""
Time Complexity:
- The algorithm uses Dijkstra's algorithm with a priority queue.
- The number of states is O(n * (discounts + 1)), where `n` is the number of cities and `discounts` is the maximum number of discounts.
- For each state, we process all neighbors, leading to a complexity of O((n + edges.length) * (discounts + 1)).
- In the worst case, this simplifies to O(edges.length * discounts).

Space Complexity:
- The space complexity is dominated by the adjacency list (O(edges.length)) and the visited dictionary (O(n * discounts)).
- Overall space complexity: O(edges.length + n * discounts).

Topic: Graphs, Dijkstra's Algorithm, Priority Queue
"""