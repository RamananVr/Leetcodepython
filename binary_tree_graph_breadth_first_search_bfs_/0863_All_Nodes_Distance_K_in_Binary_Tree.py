"""
LeetCode Problem #863: All Nodes Distance K in Binary Tree

Problem Statement:
Given the `root` of a binary tree, the value of a target node `target`, and an integer `k`, return an array of the values of all nodes that have a distance `k` from the target node.

You can return the answer in any order.

Constraints:
1. The number of nodes in the tree is in the range [1, 500].
2. 0 <= Node.val <= 500
3. All the values Node.val are unique.
4. target is the value of one of the nodes in the tree.
5. 0 <= k <= 100
"""

from collections import defaultdict, deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def distanceK(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    """
    Finds all nodes at distance K from the target node in a binary tree.
    """
    # Step 1: Build the graph representation of the tree
    graph = defaultdict(list)
    
    def build_graph(node: Optional[TreeNode], parent: Optional[TreeNode]):
        if not node:
            return
        if parent:
            graph[node.val].append(parent.val)
            graph[parent.val].append(node.val)
        build_graph(node.left, node)
        build_graph(node.right, node)
    
    build_graph(root, None)
    
    # Step 2: Perform BFS from the target node to find nodes at distance K
    visited = set()
    queue = deque([(target.val, 0)])  # (current_node, current_distance)
    result = []
    
    while queue:
        current_node, current_distance = queue.popleft()
        if current_node in visited:
            continue
        visited.add(current_node)
        
        if current_distance == k:
            result.append(current_node)
        elif current_distance < k:
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, current_distance + 1))
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    
    target = root.left  # Node with value 5
    k = 2
    print(distanceK(root, target, k))  # Output: [7, 4, 1]

    # Example 2
    root = TreeNode(1)
    target = root  # Node with value 1
    k = 3
    print(distanceK(root, target, k))  # Output: []

"""
Time Complexity Analysis:
1. Building the graph takes O(N), where N is the number of nodes in the tree, as we visit each node once.
2. The BFS traversal also takes O(N), as we visit each node at most once.
Overall time complexity: O(N)

Space Complexity Analysis:
1. The graph representation uses O(N) space to store the adjacency list.
2. The BFS queue and visited set also use O(N) space in the worst case.
Overall space complexity: O(N)

Topic: Binary Tree, Graph, Breadth-First Search (BFS)
"""