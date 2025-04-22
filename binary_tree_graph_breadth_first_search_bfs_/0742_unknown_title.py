"""
LeetCode Problem #742: Closest Leaf in a Binary Tree

Problem Statement:
Given a binary tree where every node has a unique value, and a target integer `k`, 
return the value of the closest leaf node to the target `k` in the tree.

Here, a leaf is a node with no children. The closest leaf to a node `k` is the leaf 
that is reached first when starting from `k` and moving along the tree edges.

Example 1:
Input: root = [1, 3, 2], k = 1
Output: 2
Explanation: The leaf closest to node 1 is node 2.

Example 2:
Input: root = [1, 2, 3, null, 4, null, null, 5, null], k = 3
Output: 5
Explanation: The leaf closest to node 3 is node 5.

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- Each node has a unique value in the range [1, 1000].
- `k` is guaranteed to be in the tree.
"""

from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findClosestLeaf(root: TreeNode, k: int) -> int:
    """
    Finds the closest leaf to the target node `k` in the binary tree.
    """
    # Step 1: Build a graph representation of the tree
    graph = defaultdict(list)
    
    def build_graph(node, parent=None):
        if not node:
            return
        if parent:
            graph[node.val].append(parent.val)
            graph[parent.val].append(node.val)
        if node.left:
            build_graph(node.left, node)
        if node.right:
            build_graph(node.right, node)
    
    build_graph(root)
    
    # Step 2: Perform BFS starting from the target node `k`
    queue = deque([k])
    visited = set()
    
    while queue:
        current = queue.popleft()
        visited.add(current)
        
        # Check if the current node is a leaf
        if len(graph[current]) == 1 and current != root.val:
            return current
        
        # Add neighbors to the queue
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.right = TreeNode(2)
    k1 = 1
    print(findClosestLeaf(root1, k1))  # Output: 2

    # Example 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.right = TreeNode(4)
    root2.left.right.left = TreeNode(5)
    k2 = 3
    print(findClosestLeaf(root2, k2))  # Output: 5

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph takes O(n), where n is the number of nodes in the tree.
- BFS traversal also takes O(n), as we visit each node once.
- Overall time complexity: O(n).

Space Complexity:
- The graph representation uses O(n) space.
- The BFS queue and visited set also use O(n) space in the worst case.
- Overall space complexity: O(n).

Topic: Binary Tree, Graph, Breadth-First Search (BFS)
"""