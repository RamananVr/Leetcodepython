"""
LeetCode Problem #1245: Tree Diameter

Problem Statement:
You are given an undirected tree. You are tasked to find the tree's diameter. 
The diameter of a tree is the number of edges on the longest path between two nodes in the tree.

The tree is given as an array of edges where `edges[i] = [u, v]` indicates that there is an undirected edge 
between nodes `u` and `v`. Return the diameter of the tree.

Constraints:
- 1 <= edges.length < 10^4
- edges[i].length == 2
- 0 <= u, v < edges.length + 1
- The given edges form a valid tree.
"""

from collections import defaultdict, deque

def treeDiameter(edges):
    """
    Function to calculate the diameter of a tree.

    :param edges: List[List[int]] - List of edges representing the tree
    :return: int - Diameter of the tree
    """
    if not edges:
        return 0

    # Step 1: Build the adjacency list for the tree
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Helper function to perform BFS and return the farthest node and its distance
    def bfs(start):
        visited = set()
        queue = deque([(start, 0)])  # (node, distance)
        farthest_node = start
        max_distance = 0

        while queue:
            node, distance = queue.popleft()
            visited.add(node)

            if distance > max_distance:
                max_distance = distance
                farthest_node = node

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))

        return farthest_node, max_distance

    # Step 2: Perform BFS from an arbitrary node (e.g., node 0) to find the farthest node
    arbitrary_node = edges[0][0]
    farthest_node, _ = bfs(arbitrary_node)

    # Step 3: Perform BFS from the farthest node found in Step 2 to find the diameter
    _, diameter = bfs(farthest_node)

    return diameter

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    edges1 = [[0, 1], [0, 2], [1, 3], [1, 4]]
    print(treeDiameter(edges1))  # Expected Output: 4

    # Test Case 2
    edges2 = [[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]
    print(treeDiameter(edges2))  # Expected Output: 4

    # Test Case 3
    edges3 = [[0, 1], [1, 2]]
    print(treeDiameter(edges3))  # Expected Output: 2

    # Test Case 4
    edges4 = [[0, 1]]
    print(treeDiameter(edges4))  # Expected Output: 1

"""
Time Complexity Analysis:
- Building the adjacency list takes O(E), where E is the number of edges.
- Each BFS traversal visits every node and edge once, so each BFS takes O(V + E), where V is the number of nodes.
- Since we perform two BFS traversals, the total time complexity is O(V + E).

Space Complexity Analysis:
- The adjacency list requires O(V + E) space.
- The BFS queue and visited set require O(V) space in the worst case.
- Therefore, the total space complexity is O(V + E).

Topic: Graphs
"""