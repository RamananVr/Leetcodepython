"""
LeetCode Problem #2477: Minimum Fuel Cost to Report to the Capital

Problem Statement:
There is a tree (i.e., a connected, undirected graph with no cycles) structure consisting of `n` cities numbered from `0` to `n - 1`, and exactly `n - 1` roads. The capital city is city `0`. You are given a 2D integer array `roads` where `roads[i] = [ai, bi]` denotes that there exists a bidirectional road connecting cities `ai` and `bi`.

There is a car in each city. You are given an integer `seats` that indicates the number of seats each car can have.

A representative from each city needs to travel to the capital to report to it. The representatives can travel in any car and can share the same car. 

Return the minimum number of liters of fuel needed to reach the capital.

Constraints:
- `1 <= n <= 10^5`
- `roads.length == n - 1`
- `roads[i].length == 2`
- `0 <= ai, bi < n`
- `ai != bi`
- `1 <= seats <= 10^5`
- The input is guaranteed to be a tree.

"""

from collections import defaultdict
import math

def minimumFuelCost(roads, seats):
    def dfs(node, parent):
        # Count the number of representatives in the subtree rooted at `node`
        representatives = 1
        for neighbor in graph[node]:
            if neighbor != parent:
                sub_representatives, sub_fuel = dfs(neighbor, node)
                representatives += sub_representatives
                fuel_cost += sub_fuel
        
        # Calculate the fuel cost for the current node
        if node != 0:  # Exclude the capital itself
            fuel_cost += math.ceil(representatives / seats)
        
        return representatives, fuel_cost

    # Build the graph
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    # Start DFS from the capital (node 0)
    _, total_fuel = dfs(0, -1)
    return total_fuel

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    roads = [[0, 1], [0, 2], [0, 3]]
    seats = 5
    print(minimumFuelCost(roads, seats))  # Output: 3

    # Test Case 2
    roads = [[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]]
    seats = 2
    print(minimumFuelCost(roads, seats))  # Output: 7

    # Test Case 3
    roads = []
    seats = 1
    print(minimumFuelCost(roads, seats))  # Output: 0

"""
Time Complexity:
- Building the graph takes O(n) time, where `n` is the number of nodes.
- The DFS traversal also takes O(n) time since we visit each node and edge exactly once.
- Calculating the fuel cost at each node is O(1).
- Overall time complexity: O(n).

Space Complexity:
- The graph is stored as an adjacency list, which takes O(n) space.
- The recursion stack for DFS can go up to O(n) in the worst case.
- Overall space complexity: O(n).

Topic: Graphs, Tree, DFS
"""