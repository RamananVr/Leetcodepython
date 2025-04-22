"""
LeetCode Question #814: Binary Tree Pruning

Problem Statement:
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node `node` is `node` plus every node that is a descendant of `node`.

Example 1:
Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]

Explanation:
Only the red nodes satisfy the property "contains a 1".
The diagram on the left shows the initial tree.
The diagram on the right shows the pruned tree.

Example 2:
Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]

Example 3:
Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]

Constraints:
- The number of nodes in the tree is in the range [1, 200].
- Node values are either 0 or 1.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        """
        Prunes the binary tree by removing all subtrees that do not contain a 1.
        """
        if not root:
            return None
        
        # Recursively prune left and right subtrees
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        # If the current node is 0 and both subtrees are None, prune this node
        if root.val == 0 and not root.left and not root.right:
            return None
        
        return root

# Helper function to build a binary tree from a list
def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

# Helper function to serialize a binary tree to a list
def serialize_tree(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    root1 = build_tree([1, None, 0, 0, 1])
    pruned1 = solution.pruneTree(root1)
    print(serialize_tree(pruned1))  # Output: [1, None, 0, None, 1]

    # Test Case 2
    root2 = build_tree([1, 0, 1, 0, 0, 0, 1])
    pruned2 = solution.pruneTree(root2)
    print(serialize_tree(pruned2))  # Output: [1, None, 1, None, 1]

    # Test Case 3
    root3 = build_tree([1, 1, 0, 1, 1, 0, 1, 0])
    pruned3 = solution.pruneTree(root3)
    print(serialize_tree(pruned3))  # Output: [1, 1, 0, 1, 1, None, 1]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each node in the binary tree is visited exactly once during the recursive traversal.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack. In the worst case, the height of the tree is O(h), where h is the height of the tree.
- For a balanced binary tree, h = O(log n). For a skewed binary tree, h = O(n).
- Therefore, the space complexity is O(h).

Topic: Binary Tree
"""