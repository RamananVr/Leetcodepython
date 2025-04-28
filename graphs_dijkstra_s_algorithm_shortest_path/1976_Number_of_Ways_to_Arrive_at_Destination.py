"""
LeetCode Problem #1976: Number of Ways to Arrive at Destination

Problem Statement:
You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. 
The inputs are:
- n: the number of intersections.
- roads: a 2D array where each roads[i] = [u, v, time] indicates that there is a road between intersections u and v that takes time minutes to travel.

You want to know in how many different ways you can arrive at intersection n - 1 starting from intersection 0. 
You can only travel on roads and you can only move to a neighboring intersection.

Return the number of ways you can arrive at the destination in the shortest amount of time. 
Since the answer may be large, return it modulo 10^9 + 7.

Constraints:
- 1 <= n <= 200
- 1 <= roads.length <= n * (n - 1) / 2
- roads[i].length == 3
- 0 <= u, v <= n - 1
- 1 <= time <= 10^9
- u != v
- There is at most one road between any two intersections.
- There is at least one path from intersection 0 to intersection n - 1.
"""

from heapq import heappop, heappush
from collections import defaultdict
import sys

def countPaths(n: int, roads: list[list[int]]) -> int:
    MOD = 10**9 + 7

    # Step 1: Build the graph as an adjacency list
    graph = defaultdict(list)
    for u, v, time in roads:
        graph[u].append((v, time))
        graph[v].append((u, time))

    # Step 2: Dijkstra's algorithm to find shortest paths
    min_heap = [(0, 0)]  # (time, node)
    shortest_time = [sys.maxsize] * n
    ways = [0] * n
    shortest_time[0] = 0
    ways[0] = 1

    while min_heap:
        curr_time, node = heappop(min_heap)

        # If the current time is greater than the shortest time, skip
        if curr_time > shortest_time[node]:
            continue

        for neighbor, travel_time in graph[node]:
            new_time = curr_time + travel_time

            # If a shorter path is found
            if new_time < shortest_time[neighbor]:
                shortest_time[neighbor] = new_time
                ways[neighbor] = ways[node]
                heappush(min_heap, (new_time, neighbor))
            # If another shortest path is found
            elif new_time == shortest_time[neighbor]:
                ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

    return ways[n - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 7
    roads1 = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
    print(countPaths(n1, roads1))  # Output: 4

    # Test Case 2
    n2 = 5
    roads2 = [[0, 1, 2], [0, 2, 2], [1, 2, 1], [1, 3, 1], [2, 3, 2], [3, 4, 3]]
    print(countPaths(n2, roads2))  # Output: 3

    # Test Case 3
    n3 = 3
    roads3 = [[0, 1, 1], [1, 2, 1], [0, 2, 2]]
    print(countPaths(n3, roads3))  # Output: 2

"""
Time Complexity:
- Building the graph takes O(E), where E is the number of roads.
- Dijkstra's algorithm takes O((V + E) * log(V)), where V is the number of intersections (nodes).
- Overall: O((V + E) * log(V)).

Space Complexity:
- The graph uses O(V + E) space.
- The shortest_time and ways arrays use O(V) space.
- The priority queue (min_heap) can grow up to O(V) in size.
- Overall: O(V + E).

Topic: Graphs, Dijkstra's Algorithm, Shortest Path
"""