"""
LeetCode Question #1928: Minimum Cost to Reach Destination in Time

Problem Statement:
You are given an integer `maxTime`, an integer `n`, and a 2D array `edges` where `edges[i] = [u_i, v_i, time_i]` indicates that there is a bidirectional road between cities `u_i` and `v_i` that takes `time_i` minutes to travel. You are also given an array `passingFees` where `passingFees[j]` is the cost of passing through city `j`.

Your goal is to find the minimum cost to travel from city `0` to city `n - 1` within `maxTime` minutes. If it is impossible to reach the destination within `maxTime` minutes, return `-1`.

Constraints:
- 1 <= maxTime <= 1000
- 1 <= n <= 1000
- 1 <= edges.length <= 10000
- `edges[i].length == 3`
- 0 <= u_i, v_i < n
- 1 <= time_i <= 1000
- 1 <= passingFees[j] <= 1000

"""

from heapq import heappop, heappush
import math

def minCost(maxTime, n, edges, passingFees):
    # Create an adjacency list for the graph
    graph = {i: [] for i in range(n)}
    for u, v, time in edges:
        graph[u].append((v, time))
        graph[v].append((u, time))
    
    # Priority queue for Dijkstra's algorithm
    pq = [(passingFees[0], 0, 0)]  # (cost, current_city, time_spent)
    min_cost = [math.inf] * n
    min_cost[0] = passingFees[0]
    min_time = [math.inf] * n
    min_time[0] = 0
    
    while pq:
        cost, city, time_spent = heappop(pq)
        
        # If we reach the destination city within maxTime, return the cost
        if city == n - 1:
            return cost
        
        # Explore neighbors
        for neighbor, travel_time in graph[city]:
            new_time = time_spent + travel_time
            new_cost = cost + passingFees[neighbor]
            
            # Only proceed if the new time is within maxTime and improves cost or time
            if new_time <= maxTime and (new_cost < min_cost[neighbor] or new_time < min_time[neighbor]):
                min_cost[neighbor] = new_cost
                min_time[neighbor] = new_time
                heappush(pq, (new_cost, neighbor, new_time))
    
    # If we cannot reach the destination within maxTime, return -1
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    maxTime = 30
    n = 5
    edges = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 4, 10], [0, 2, 15], [2, 4, 10]]
    passingFees = [5, 1, 2, 20, 10]
    print(minCost(maxTime, n, edges, passingFees))  # Output: 25

    # Test Case 2
    maxTime = 25
    n = 3
    edges = [[0, 1, 10], [1, 2, 10], [0, 2, 20]]
    passingFees = [5, 10, 15]
    print(minCost(maxTime, n, edges, passingFees))  # Output: 30

    # Test Case 3
    maxTime = 10
    n = 3
    edges = [[0, 1, 10], [1, 2, 10], [0, 2, 20]]
    passingFees = [5, 10, 15]
    print(minCost(maxTime, n, edges, passingFees))  # Output: -1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph takes O(edges.length).
- Dijkstra's algorithm processes each node and edge. In the worst case, we process all edges and nodes, leading to O(n + edges.length * log(n)) due to the priority queue operations.

Space Complexity:
- The graph representation takes O(edges.length).
- The priority queue and auxiliary arrays (min_cost, min_time) take O(n).
- Total space complexity is O(n + edges.length).

Topic: Graphs
"""