"""
LeetCode Problem #847: Shortest Path Visiting All Nodes

Problem Statement:
You have an undirected, connected graph of `n` nodes labeled from `0` to `n - 1`. 
You are given an array `graph` where `graph[i]` is a list of all the nodes connected with node `i` by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, and you may revisit nodes multiple times.

Constraints:
- `n == graph.length`
- `1 <= n <= 12`
- `0 <= graph[i].length < n`
- `graph[i]` does not contain `i`.
- If `graph[a]` contains `b`, then `graph[b]` contains `a`.
- The input graph is always connected.

Example:
Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]

Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]
"""

from collections import deque

def shortestPathLength(graph):
    """
    Finds the shortest path that visits every node in the graph.

    :param graph: List[List[int]] - adjacency list representation of the graph
    :return: int - length of the shortest path visiting all nodes
    """
    n = len(graph)
    final_state = (1 << n) - 1  # All nodes visited state (bitmask)
    queue = deque([(i, 1 << i, 0) for i in range(n)])  # (current_node, visited_state, steps)
    visited = set((i, 1 << i) for i in range(n))  # (current_node, visited_state)

    while queue:
        node, state, steps = queue.popleft()

        # If all nodes are visited, return the number of steps
        if state == final_state:
            return steps

        # Explore neighbors
        for neighbor in graph[node]:
            next_state = state | (1 << neighbor)
            if (neighbor, next_state) not in visited:
                visited.add((neighbor, next_state))
                queue.append((neighbor, next_state, steps + 1))

    return -1  # This line should never be reached due to problem constraints


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    graph1 = [[1, 2, 3], [0], [0], [0]]
    print(shortestPathLength(graph1))  # Output: 4

    # Test Case 2
    graph2 = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]
    print(shortestPathLength(graph2))  # Output: 4

    # Test Case 3
    graph3 = [[1, 2], [0, 3], [0, 3], [1, 2]]
    print(shortestPathLength(graph3))  # Output: 4

    # Test Case 4
    graph4 = [[1], [0]]
    print(shortestPathLength(graph4))  # Output: 1


"""
Time and Space Complexity Analysis:

Time Complexity:
- The number of states is O(n * 2^n), where `n` is the number of nodes.
  - There are `n` nodes, and each node can have `2^n` possible visited states (bitmask).
- For each state, we process all neighbors of the current node, which takes O(n) time.
- Thus, the overall time complexity is O(n^2 * 2^n).

Space Complexity:
- The queue can store up to O(n * 2^n) states in the worst case.
- The visited set also stores O(n * 2^n) states.
- Thus, the space complexity is O(n * 2^n).

Topic: Graphs, Breadth-First Search (BFS), Bitmasking
"""