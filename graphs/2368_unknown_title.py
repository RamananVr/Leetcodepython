"""
LeetCode Problem #2368: Reachable Nodes With Restrictions

Problem Statement:
You are given an integer `n` representing the number of nodes in an undirected graph, numbered from `0` to `n - 1`. 
You are also given a 2D integer array `edges`, where `edges[i] = [ai, bi]` indicates that there exists an undirected edge 
connecting nodes `ai` and `bi`.

Additionally, you are given a list `restricted` which represents a subset of nodes that are restricted. 
You cannot visit these nodes or the edges connected to them.

Return the number of nodes that are reachable from node `0` without visiting any restricted node.

Constraints:
- `2 <= n <= 100,000`
- `1 <= edges.length <= min(100,000, n * (n - 1) / 2)`
- `edges[i].length == 2`
- `0 <= ai, bi < n`
- `ai != bi`
- All pairs `(ai, bi)` are distinct.
- `1 <= restricted.length < n`
- `1 <= restricted[i] < n`
- All values of `restricted` are distinct.

"""

from collections import defaultdict, deque

def reachableNodes(n: int, edges: list[list[int]], restricted: list[int]) -> int:
    """
    Returns the number of nodes reachable from node 0 without visiting any restricted nodes.
    """
    # Create an adjacency list for the graph
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # Convert restricted list to a set for O(1) lookups
    restricted_set = set(restricted)
    
    # BFS to count reachable nodes
    visited = set()
    queue = deque([0])
    visited.add(0)
    reachable_count = 0
    
    while queue:
        node = queue.popleft()
        reachable_count += 1
        
        for neighbor in graph[node]:
            if neighbor not in visited and neighbor not in restricted_set:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return reachable_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 7
    edges1 = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
    restricted1 = [4, 5]
    print(reachableNodes(n1, edges1, restricted1))  # Output: 4

    # Test Case 2
    n2 = 7
    edges2 = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
    restricted2 = [4, 5, 6]
    print(reachableNodes(n2, edges2, restricted2))  # Output: 3

    # Test Case 3
    n3 = 4
    edges3 = [[0, 1], [1, 2], [2, 3]]
    restricted3 = [3]
    print(reachableNodes(n3, edges3, restricted3))  # Output: 3

"""
Time Complexity Analysis:
- Building the adjacency list takes O(edges.length).
- BFS traversal visits each node and edge at most once, so it takes O(n + edges.length).
- Overall time complexity: O(n + edges.length).

Space Complexity Analysis:
- The adjacency list requires O(n + edges.length) space.
- The visited set and queue require O(n) space in the worst case.
- The restricted set requires O(restricted.length) space.
- Overall space complexity: O(n + edges.length).

Topic: Graphs
"""