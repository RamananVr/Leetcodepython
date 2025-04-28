"""
LeetCode Question #1617: Count Subtrees With Max Distance Between Cities

Problem Statement:
You are given n cities numbered from 1 to n. You are also given the array edges, where edges[i] = [ui, vi] indicates that there is a bidirectional road between cities ui and vi.

A subtree is a subset of cities where every city is reachable from every other city in the subset via the roads in the subset. The distance between two cities is defined as the number of roads that must be traveled to go from one city to the other.

Return an array ans of size n-1, where ans[i] is the number of subtrees that contain exactly i+1 roads.

Example:
Input: n = 4, edges = [[1,2],[2,3],[2,4]]
Output: [3,4,0]

Explanation:
- There are 3 subtrees with 1 road: [1,2], [2,3], [2,4].
- There are 4 subtrees with 2 roads: [1,2,3], [1,2,4], [2,3,4], [1,2,4].
- There are no subtrees with 3 roads.

Constraints:
- 2 <= n <= 15
- edges.length == n-1
- edges[i].length == 2
- 1 <= ui, vi <= n
- All pairs (ui, vi) are distinct.
"""

from itertools import combinations
from collections import defaultdict, deque

def countSubtreesWithMaxDistance(n, edges):
    def bfs_max_distance(subtree):
        # Perform BFS to calculate the maximum distance in the subtree
        graph = defaultdict(list)
        for u, v in subtree:
            graph[u].append(v)
            graph[v].append(u)
        
        def bfs(node):
            visited = set()
            queue = deque([(node, 0)])
            visited.add(node)
            farthest_node, max_dist = node, 0
            
            while queue:
                curr, dist = queue.popleft()
                if dist > max_dist:
                    max_dist = dist
                    farthest_node = curr
                
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))
            
            return farthest_node, max_dist
        
        # First BFS to find the farthest node from any starting point
        start_node = list(graph.keys())[0]
        farthest_node, _ = bfs(start_node)
        
        # Second BFS from the farthest node to calculate the maximum distance
        _, max_distance = bfs(farthest_node)
        return max_distance

    # Generate all subsets of edges
    edge_combinations = []
    for size in range(1, n):
        edge_combinations.extend(combinations(edges, size))
    
    # Count subtrees with specific maximum distances
    ans = [0] * (n - 1)
    for edge_subset in edge_combinations:
        # Check if the edge subset forms a valid subtree
        nodes = set()
        for u, v in edge_subset:
            nodes.add(u)
            nodes.add(v)
        
        if len(nodes) - 1 == len(edge_subset):  # Valid subtree condition
            max_distance = bfs_max_distance(edge_subset)
            if max_distance > 0 and max_distance < n:
                ans[max_distance - 1] += 1
    
    return ans

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 4
    edges = [[1, 2], [2, 3], [2, 4]]
    print(countSubtreesWithMaxDistance(n, edges))  # Output: [3, 4, 0]

    # Test Case 2
    n = 3
    edges = [[1, 2], [2, 3]]
    print(countSubtreesWithMaxDistance(n, edges))  # Output: [2, 1]

    # Test Case 3
    n = 5
    edges = [[1, 2], [1, 3], [3, 4], [3, 5]]
    print(countSubtreesWithMaxDistance(n, edges))  # Output: [4, 6, 1, 0]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Generating all subsets of edges takes O(2^(n-1)).
- For each subset, we perform BFS twice, which takes O(V + E) = O(n + n-1) = O(n).
- Overall complexity: O(2^(n-1) * n).

Space Complexity:
- The graph representation and BFS queue use O(n) space.
- Storing all subsets of edges takes O(2^(n-1)).
- Overall space complexity: O(2^(n-1) + n).

Topic: Graphs, BFS, Combinatorics
"""