"""
LeetCode Problem #2714: Find Shortest Path with K Hops

Problem Statement:
You are given a positive integer `n` representing `n` cities numbered from `0` to `n - 1`. You are also given a 2D array `roads` where `roads[i] = [ai, bi, timei]` indicates that there is a road between cities `ai` and `bi` that takes `timei` minutes to travel.

You want to know the minimum time to travel from city `0` to city `n - 1` when you can eliminate at most `k` roads (i.e., set their travel times to `0`).

Return the minimum travel time to go from city `0` to city `n - 1`, or return `-1` if it's not possible.

Constraints:
- `n == roads.length + 1`
- `1 <= n <= 50`
- `0 <= k <= 50`
- `roads[i].length == 3`
- `0 <= ai, bi <= n - 1`
- `ai != bi`
- `1 <= timei <= 10^4`
- There are no duplicate roads between any two cities.
"""

import heapq
from collections import defaultdict

def shortestPathWithKHops(n, roads, k):
    """
    Finds the shortest path from city 0 to city n-1 with at most k road eliminations.
    
    :param n: int - Number of cities
    :param roads: List[List[int]] - Roads with [from, to, time]
    :param k: int - Maximum number of roads that can be eliminated
    :return: int - Minimum travel time or -1 if impossible
    """
    # Build adjacency list
    graph = defaultdict(list)
    for a, b, time in roads:
        graph[a].append((b, time))
        graph[b].append((a, time))
    
    # Dijkstra's algorithm with state (city, eliminations_used)
    # Priority queue: (time, city, eliminations_used)
    pq = [(0, 0, 0)]  # (time, city, eliminations_used)
    
    # visited[city][eliminations_used] = minimum time to reach city with eliminations_used
    visited = {}
    
    while pq:
        time, city, eliminations = heapq.heappop(pq)
        
        # If we reached the destination
        if city == n - 1:
            return time
        
        # Skip if we've seen this state with better time
        if (city, eliminations) in visited and visited[(city, eliminations)] <= time:
            continue
        
        visited[(city, eliminations)] = time
        
        # Explore neighbors
        for next_city, road_time in graph[city]:
            # Option 1: Use the road normally
            next_time = time + road_time
            if (next_city, eliminations) not in visited or visited[(next_city, eliminations)] > next_time:
                heapq.heappush(pq, (next_time, next_city, eliminations))
            
            # Option 2: Eliminate this road (if we have eliminations left)
            if eliminations < k:
                if (next_city, eliminations + 1) not in visited or visited[(next_city, eliminations + 1)] > time:
                    heapq.heappush(pq, (time, next_city, eliminations + 1))
    
    return -1

def shortestPathWithKHopsDP(n, roads, k):
    """
    Dynamic programming approach using Floyd-Warshall with modifications.
    
    :param n: int - Number of cities
    :param roads: List[List[int]] - Roads with [from, to, time]
    :param k: int - Maximum number of roads that can be eliminated
    :return: int - Minimum travel time or -1 if impossible
    """
    # Initialize distance matrix
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    
    # Set distances for direct roads
    for i in range(n):
        dist[i][i] = 0
    
    for a, b, time in roads:
        dist[a][b] = min(dist[a][b], time)
        dist[b][a] = min(dist[b][a], time)
    
    # dp[i][j][eliminations] = minimum time from city i to city j using at most eliminations
    dp = [[[INF] * (k + 1) for _ in range(n)] for _ in range(n)]
    
    # Initialize base cases
    for i in range(n):
        for j in range(n):
            if dist[i][j] != INF:
                dp[i][j][0] = dist[i][j]
                # With one elimination, we can make any direct connection free
                if k > 0:
                    dp[i][j][1] = 0 if i != j else 0
    
    # Fill DP table
    for eliminations in range(k + 1):
        for intermediate in range(n):
            for i in range(n):
                for j in range(n):
                    if i != j:
                        # Path through intermediate without using elimination
                        if dp[i][intermediate][eliminations] != INF and dp[intermediate][j][0] != INF:
                            dp[i][j][eliminations] = min(dp[i][j][eliminations], 
                                                       dp[i][intermediate][eliminations] + dp[intermediate][j][0])
                        
                        # Path through intermediate using one elimination on second segment
                        if eliminations > 0 and dp[i][intermediate][eliminations - 1] != INF:
                            dp[i][j][eliminations] = min(dp[i][j][eliminations], dp[i][intermediate][eliminations - 1])
    
    # Find minimum time to reach destination with at most k eliminations
    result = INF
    for eliminations in range(k + 1):
        result = min(result, dp[0][n - 1][eliminations])
    
    return result if result != INF else -1

def shortestPathWithKHopsBFS(n, roads, k):
    """
    BFS-based solution exploring all possible paths.
    
    :param n: int - Number of cities
    :param roads: List[List[int]] - Roads with [from, to, time]
    :param k: int - Maximum number of roads that can be eliminated
    :return: int - Minimum travel time or -1 if impossible
    """
    # Build adjacency list
    graph = defaultdict(list)
    for a, b, time in roads:
        graph[a].append((b, time))
        graph[b].append((a, time))
    
    # Use modified Dijkstra with state compression
    # State: (current_time, city, eliminations_left)
    pq = [(0, 0, k)]
    best = {}  # (city, eliminations_left) -> best_time
    
    while pq:
        time, city, eliminations_left = heapq.heappop(pq)
        
        # Check if we've reached the destination
        if city == n - 1:
            return time
        
        # Skip if we've seen this state with better or equal time
        state = (city, eliminations_left)
        if state in best and best[state] <= time:
            continue
        best[state] = time
        
        # Explore all neighbors
        for next_city, road_time in graph[city]:
            # Option 1: Use the road normally
            new_time = time + road_time
            new_state = (next_city, eliminations_left)
            if new_state not in best or best[new_state] > new_time:
                heapq.heappush(pq, (new_time, next_city, eliminations_left))
            
            # Option 2: Eliminate this road (if possible)
            if eliminations_left > 0:
                new_state = (next_city, eliminations_left - 1)
                if new_state not in best or best[new_state] > time:
                    heapq.heappush(pq, (time, next_city, eliminations_left - 1))
    
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 4
    roads = [[0, 1, 4], [0, 2, 2], [2, 3, 6], [1, 3, 1]]
    k = 1
    print(f"n: {n}, roads: {roads}, k: {k}")
    print(f"shortestPathWithKHops: {shortestPathWithKHops(n, roads, k)}")  # Output: 3
    print(f"shortestPathWithKHopsBFS: {shortestPathWithKHopsBFS(n, roads, k)}")  # Output: 3
    print()

    # Test Case 2
    n = 3
    roads = [[0, 1, 10], [1, 2, 10]]
    k = 1
    print(f"n: {n}, roads: {roads}, k: {k}")
    print(f"shortestPathWithKHops: {shortestPathWithKHops(n, roads, k)}")  # Output: 10
    print(f"shortestPathWithKHopsBFS: {shortestPathWithKHopsBFS(n, roads, k)}")  # Output: 10
    print()

    # Test Case 3
    n = 4
    roads = [[0, 1, 1], [1, 2, 1], [2, 3, 1]]
    k = 0
    print(f"n: {n}, roads: {roads}, k: {k}")
    print(f"shortestPathWithKHops: {shortestPathWithKHops(n, roads, k)}")  # Output: 3
    print(f"shortestPathWithKHopsBFS: {shortestPathWithKHopsBFS(n, roads, k)}")  # Output: 3
    print()

    # Test Case 4
    n = 2
    roads = [[0, 1, 5]]
    k = 1
    print(f"n: {n}, roads: {roads}, k: {k}")
    print(f"shortestPathWithKHops: {shortestPathWithKHops(n, roads, k)}")  # Output: 0
    print(f"shortestPathWithKHopsBFS: {shortestPathWithKHopsBFS(n, roads, k)}")  # Output: 0
    print()

    # Test Case 5 - No path exists
    n = 3
    roads = [[0, 1, 1]]
    k = 0
    print(f"n: {n}, roads: {roads}, k: {k}")
    print(f"shortestPathWithKHops: {shortestPathWithKHops(n, roads, k)}")  # Output: -1
    print(f"shortestPathWithKHopsBFS: {shortestPathWithKHopsBFS(n, roads, k)}")  # Output: -1

    # Validation
    assert shortestPathWithKHops(4, [[0, 1, 4], [0, 2, 2], [2, 3, 6], [1, 3, 1]], 1) == 3
    assert shortestPathWithKHopsBFS(3, [[0, 1, 10], [1, 2, 10]], 1) == 10
    assert shortestPathWithKHops(2, [[0, 1, 5]], 1) == 0
    print("All test cases passed!")

"""
Time Complexity Analysis:
Dijkstra with State:
- Time complexity: O((n * k) * log(n * k) + |E|) where |E| is the number of edges.

DP Approach:
- Time complexity: O(n^3 * k) for the Floyd-Warshall-style DP.

Space Complexity Analysis:
- Space complexity: O(n * k) for storing visited states or DP table.

Topic: Graph, Shortest Path, Dijkstra, Dynamic Programming
"""
