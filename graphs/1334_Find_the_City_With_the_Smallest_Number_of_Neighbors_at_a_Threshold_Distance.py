"""
LeetCode Problem #1334: Find the City With the Smallest Number of Neighbors at a Threshold Distance

Problem Statement:
There are n cities numbered from 0 to n-1. You are given an array `edges` where `edges[i] = [from_i, to_i, weight_i]` represents a bidirectional and weighted edge between cities `from_i` and `to_i` with distance `weight_i`.

You are also given an integer `distanceThreshold`.

Return the city number with the smallest number of neighbors that the city can reach at a distance threshold or less. If there are multiple such cities, return the city with the greatest number.

The distance between two cities is defined as the minimum distance between them. A city is considered reachable if the distance is less than or equal to `distanceThreshold`.

Constraints:
- 2 <= n <= 100
- 1 <= edges.length <= 4600
- edges[i].length == 3
- 0 <= from_i, to_i < n
- 1 <= weight_i <= 10^4
- All pairs `(from_i, to_i)` are distinct.
- 1 <= distanceThreshold <= 10^4
"""

# Solution
def findTheCity(n, edges, distanceThreshold):
    # Initialize the distance matrix with infinity
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Distance to self is 0
    for i in range(n):
        dist[i][i] = 0
    
    # Populate the distance matrix with edge weights
    for from_i, to_i, weight_i in edges:
        dist[from_i][to_i] = weight_i
        dist[to_i][from_i] = weight_i
    
    # Floyd-Warshall Algorithm to find shortest paths between all pairs of cities
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    # Find the city with the smallest number of reachable neighbors
    min_neighbors = float('inf')
    result_city = -1
    
    for city in range(n):
        reachable_neighbors = sum(1 for neighbor in range(n) if dist[city][neighbor] <= distanceThreshold)
        
        # Update result based on the problem requirements
        if reachable_neighbors < min_neighbors or (reachable_neighbors == min_neighbors and city > result_city):
            min_neighbors = reachable_neighbors
            result_city = city
    
    return result_city

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 4
    edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
    distanceThreshold = 4
    print(findTheCity(n, edges, distanceThreshold))  # Output: 3

    # Test Case 2
    n = 5
    edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
    distanceThreshold = 2
    print(findTheCity(n, edges, distanceThreshold))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- Floyd-Warshall Algorithm runs in O(n^3), where n is the number of cities.
- Counting reachable neighbors for each city takes O(n^2).
- Overall time complexity: O(n^3).

Space Complexity:
- The distance matrix `dist` requires O(n^2) space.
- Overall space complexity: O(n^2).

Topic: Graphs
"""