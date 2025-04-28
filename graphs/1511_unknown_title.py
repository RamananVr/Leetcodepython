"""
LeetCode Problem #1511: Maximum Score Of A Path Between Two Cities

Problem Statement:
You are given n cities represented as integers from 0 to n-1. You are also given an array roads, 
where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi 
with a distance of distancei. The score of a path between two cities is defined as the maximum distance 
of any road in the path.

Return the maximum score of a path between any two cities.

Note:
- A path is a sequence of roads connecting two cities.
- There may be multiple roads between two cities.

Constraints:
- 2 <= n <= 100
- 1 <= roads.length <= 1000
- roads[i].length == 3
- 0 <= ai, bi <= n-1
- 1 <= distancei <= 10^4
- There are no repeated roads.
"""

# Solution
from itertools import combinations

def maximumScorePath(n, roads):
    # Create an adjacency list to store the graph
    graph = {i: [] for i in range(n)}
    for a, b, distance in roads:
        graph[a].append((b, distance))
        graph[b].append((a, distance))
    
    # Initialize the maximum score
    max_score = 0
    
    # Iterate over all pairs of cities
    for city1, city2 in combinations(range(n), 2):
        visited = set()
        max_distance = dfs(graph, city1, city2, visited)
        max_score = max(max_score, max_distance)
    
    return max_score

def dfs(graph, current, target, visited):
    if current == target:
        return 0
    
    visited.add(current)
    max_distance = 0
    
    for neighbor, distance in graph[current]:
        if neighbor not in visited:
            max_distance = max(max_distance, max(distance, dfs(graph, neighbor, target, visited)))
    
    visited.remove(current)
    return max_distance

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 4
    roads = [[0, 1, 4], [0, 2, 3], [1, 2, 5], [1, 3, 6]]
    print(maximumScorePath(n, roads))  # Expected Output: 6

    # Test Case 2
    n = 5
    roads = [[0, 1, 1], [0, 2, 2], [1, 3, 3], [2, 4, 4], [3, 4, 5]]
    print(maximumScorePath(n, roads))  # Expected Output: 5

    # Test Case 3
    n = 3
    roads = [[0, 1, 10], [1, 2, 20], [0, 2, 15]]
    print(maximumScorePath(n, roads))  # Expected Output: 20

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates over all pairs of cities, which is O(n^2).
- For each pair, a DFS is performed, which can take up to O(n + roads.length) in the worst case.
- Therefore, the overall time complexity is O(n^2 * (n + roads.length)).

Space Complexity:
- The adjacency list requires O(n + roads.length) space.
- The visited set used in DFS requires O(n) space.
- Therefore, the overall space complexity is O(n + roads.length).
"""

# Topic: Graphs