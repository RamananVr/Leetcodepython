"""
LeetCode Problem #133: Clone Graph

Problem Statement:
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

Class Definition for a Node:
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

Test cases are guaranteed to be connected, meaning there is only one connected component in the graph.

Constraints:
- The number of nodes in the graph is in the range [0, 100].
- 1 <= Node.val <= 100
- Node.val is unique for each node.
- There are no repeated edges or self-loops in the graph.
- The graph is undirected.

"""

# Solution
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        # Dictionary to store the mapping from original node to cloned node
        cloned_nodes = {}
        
        # Helper function to perform DFS and clone the graph
        def dfs(node):
            if node in cloned_nodes:
                return cloned_nodes[node]
            
            # Clone the current node
            clone = Node(node.val)
            cloned_nodes[node] = clone
            
            # Recursively clone neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)

# Example Test Cases
def test_clone_graph():
    # Test Case 1: Empty graph
    solution = Solution()
    assert solution.cloneGraph(None) == None

    # Test Case 2: Single node graph
    node1 = Node(1)
    cloned_graph = solution.cloneGraph(node1)
    assert cloned_graph.val == 1
    assert cloned_graph.neighbors == []

    # Test Case 3: Graph with multiple nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    cloned_graph = solution.cloneGraph(node1)
    assert cloned_graph.val == 1
    assert len(cloned_graph.neighbors) == 2
    assert cloned_graph.neighbors[0].val == 2
    assert cloned_graph.neighbors[1].val == 4
    assert cloned_graph.neighbors[0].neighbors[1].val == 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- Each node is visited once, and for each node, we iterate through its neighbors.
- If there are N nodes and E edges, the time complexity is O(N + E).

Space Complexity:
- The space complexity is O(N) for the `cloned_nodes` dictionary and the recursion stack in the DFS.
- Therefore, the overall space complexity is O(N).
"""

# Topic: Graph