"""
LeetCode Problem #2385: Amount of Time for Binary Tree to Be Infected

Problem Statement:
You are given the root of a binary tree with `n` nodes labeled from `1` to `n`. Each node has a unique value in the range `[1, n]`, and a target node `start`.

At minute 0, the infection starts from the node with the value `start`. Each minute, a node becomes infected if at least one of its neighbors is infected.

Return the amount of time in minutes it takes for the entire tree to be infected.

Constraints:
- The number of nodes in the tree is `n`.
- `2 <= n <= 10^5`
- `1 <= Node.val <= n`
- Each node has a unique value.
- A node's value is between `1` and `n`.
- `start` is a valid node value in the tree.
"""

from collections import defaultdict, deque

# Solution
def amountOfTime(root, start):
    """
    Calculate the time required to infect the entire binary tree starting from the given node.

    :param root: TreeNode, the root of the binary tree
    :param start: int, the value of the starting node
    :return: int, the time in minutes to infect the entire tree
    """
    # Step 1: Build an adjacency list representation of the tree
    def build_graph(node, parent):
        if not node:
            return
        if parent:
            graph[node.val].append(parent.val)
            graph[parent.val].append(node.val)
        build_graph(node.left, node)
        build_graph(node.right, node)

    graph = defaultdict(list)
    build_graph(root, None)

    # Step 2: Perform BFS to calculate the time to infect the entire tree
    visited = set()
    queue = deque([(start, 0)])  # (current_node, time)
    max_time = 0

    while queue:
        node, time = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        max_time = max(max_time, time)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, time + 1))

    return max_time

# Example Test Cases
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(6)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(8)
    start1 = 4
    print(amountOfTime(root1, start1))  # Output: 4

    # Example 2
    root2 = TreeNode(1)
    root2.left = TreeNode(5)
    start2 = 5
    print(amountOfTime(root2, start2))  # Output: 1

"""
Time Complexity Analysis:
- Building the graph takes O(n) time, where n is the number of nodes in the tree, as we visit each node once.
- The BFS traversal also takes O(n) time, as we visit each node once during the traversal.
- Overall time complexity: O(n).

Space Complexity Analysis:
- The adjacency list (graph) requires O(n) space to store the tree structure.
- The BFS queue and visited set also require O(n) space in the worst case.
- Overall space complexity: O(n).

Topic: Binary Tree, Graph, Breadth-First Search (BFS)
"""