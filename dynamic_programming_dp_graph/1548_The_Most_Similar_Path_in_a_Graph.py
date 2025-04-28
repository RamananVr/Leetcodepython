"""
LeetCode Problem #1548: The Most Similar Path in a Graph

Problem Statement:
We have n cities and m bidirectional roads where roads[i] = [ai, bi] connects city ai with city bi. 
Each city has a name consisting of exactly one character. You are given a string array names of length n 
where names[i] is the name of the ith city, and a string array targetPath of length k. You want to find 
the most similar path of length k in the graph such that the ith city in the path has the same name as 
targetPath[i]. If there are multiple answers, return any of them.

The similarity of a path is defined as the number of positions where the city name in the path is the 
same as the corresponding targetPath name.

Return the most similar path of length k in the graph.

Constraints:
- 2 <= n <= 100
- 1 <= m <= 100
- names.length == n
- names[i].length == 1
- 1 <= targetPath.length <= 100
- targetPath[i].length == 1
- 0 <= ai, bi < n
- ai != bi
- All the pairs (ai, bi) are distinct.

"""

from collections import defaultdict, deque
import sys

def mostSimilar(n, roads, names, targetPath):
    # Build the graph
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    # Initialize DP table and path reconstruction table
    k = len(targetPath)
    dp = [[sys.maxsize] * n for _ in range(k)]
    parent = [[-1] * n for _ in range(k)]

    # Base case: Fill the last row of DP table
    for city in range(n):
        dp[k - 1][city] = 0 if names[city] == targetPath[k - 1] else 1

    # Fill the DP table from bottom to top
    for i in range(k - 2, -1, -1):
        for city in range(n):
            for neighbor in graph[city]:
                cost = 0 if names[city] == targetPath[i] else 1
                if dp[i + 1][neighbor] + cost < dp[i][city]:
                    dp[i][city] = dp[i + 1][neighbor] + cost
                    parent[i][city] = neighbor

    # Find the starting city with the minimum cost
    min_cost = sys.maxsize
    start_city = -1
    for city in range(n):
        if dp[0][city] < min_cost:
            min_cost = dp[0][city]
            start_city = city

    # Reconstruct the path
    path = []
    current_city = start_city
    for i in range(k):
        path.append(current_city)
        current_city = parent[i][current_city]

    return path

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 5
    roads = [[0, 2], [0, 3], [1, 2], [1, 3], [1, 4], [2, 4]]
    names = ["A", "B", "A", "C", "D"]
    targetPath = ["A", "C", "D", "A"]
    print(mostSimilar(n, roads, names, targetPath))  # Expected Output: [0, 3, 4, 2] or similar

    # Test Case 2
    n = 4
    roads = [[0, 1], [1, 2], [2, 3], [3, 0]]
    names = ["A", "B", "C", "D"]
    targetPath = ["A", "B", "C", "D"]
    print(mostSimilar(n, roads, names, targetPath))  # Expected Output: [0, 1, 2, 3]

    # Test Case 3
    n = 3
    roads = [[0, 1], [1, 2], [2, 0]]
    names = ["A", "B", "C"]
    targetPath = ["A", "C", "B", "A"]
    print(mostSimilar(n, roads, names, targetPath))  # Expected Output: [0, 2, 1, 0]

"""
Time Complexity:
- Building the graph: O(m), where m is the number of roads.
- Filling the DP table: O(k * n * d), where k is the length of targetPath, n is the number of cities, 
  and d is the average degree of a node in the graph.
- Reconstructing the path: O(k).
Overall: O(k * n * d).

Space Complexity:
- DP table and parent table: O(k * n).
- Graph representation: O(m).
Overall: O(k * n + m).

Topic: Dynamic Programming (DP), Graph
"""