"""
LeetCode Question #1516: Move Sub-Tree of N-Ary Tree

Problem Statement:
You are given the root of an N-ary tree `root` and two integers `p` and `q` representing two nodes in the tree. 
The nodes are guaranteed to exist in the tree. You need to move the subtree of the node with value `p` to become 
a direct child of the node with value `q`. If `p` is already a child of `q`, do nothing.

Return the root of the modified tree.

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- Each node has a unique value in the range [1, 1000].
- Both `p` and `q` are guaranteed to exist in the tree.

Follow-up:
Can you solve this problem in O(n) time complexity?

"""

# Definition for a Node in the N-ary tree.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def moveSubTree(self, root: 'Node', p: int, q: int) -> 'Node':
        # Helper function to find a node and its parent in the tree
        def find_node_and_parent(node, parent, target):
            if not node:
                return None, None
            if node.val == target:
                return node, parent
            for child in node.children:
                found_node, found_parent = find_node_and_parent(child, node, target)
                if found_node:
                    return found_node, found_parent
            return None, None

        # Find nodes p and q along with their parents
        p_node, p_parent = find_node_and_parent(root, None, p)
        q_node, _ = find_node_and_parent(root, None, q)

        # If p is already a child of q, do nothing
        if p_node in q_node.children:
            return root

        # Remove p from its current parent's children
        if p_parent:
            p_parent.children.remove(p_node)

        # If q is a descendant of p, we need to reattach q to p's parent
        if self.is_descendant(p_node, q_node):
            q_parent, _ = find_node_and_parent(root, None, q)
            if q_parent:
                q_parent.children.remove(q_node)
            p_node.children.append(q_node)

        # Attach p as a child of q
        q_node.children.append(p_node)

        # Return the root of the modified tree
        return root

    # Helper function to check if a node is a descendant of another node
    def is_descendant(self, root, target):
        if not root:
            return False
        if root == target:
            return True
        for child in root.children:
            if self.is_descendant(child, target):
                return True
        return False

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root = Node(1, [
        Node(2, [
            Node(4),
            Node(5)
        ]),
        Node(3)
    ])
    p = 2
    q = 3
    solution = Solution()
    new_root = solution.moveSubTree(root, p, q)
    # Expected Output: Node 1 with structure:
    # 1 -> [3 -> [2 -> [4, 5]], 2]

    # Example 2
    root = Node(1, [
        Node(2, [
            Node(4),
            Node(5)
        ]),
        Node(3)
    ])
    p = 4
    q = 5
    new_root = solution.moveSubTree(root, p, q)
    # Expected Output: Node 1 with structure:
    # 1 -> [2 -> [5 -> [4]], 3]

"""
Time Complexity:
- The time complexity is O(n), where n is the number of nodes in the tree. This is because we traverse the tree to find the nodes p and q, and potentially traverse it again to check for descendants.

Space Complexity:
- The space complexity is O(h), where h is the height of the tree. This is due to the recursive stack used during the traversal.

Topic: Tree
"""