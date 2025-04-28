"""
LeetCode Problem #1080: Insufficient Nodes in Root to Leaf Paths

Problem Statement:
Given the `root` of a binary tree and an integer `limit`, delete all insufficient nodes in the tree simultaneously, and return the root of the resulting binary tree.

A node is "insufficient" if every root-to-leaf path intersecting this node has a sum strictly less than `limit`.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Constraints:
- The number of nodes in the tree is in the range [1, 5000].
- -10^5 <= Node.val <= 10^5
- -10^9 <= limit <= 10^9
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sufficientSubset(root: TreeNode, limit: int) -> TreeNode:
    """
    Removes insufficient nodes from the binary tree.
    """
    def dfs(node, current_sum):
        # Base case: if the node is None, return None
        if not node:
            return None
        
        # Update the current sum
        current_sum += node.val
        
        # If it's a leaf node, check if the path sum is sufficient
        if not node.left and not node.right:
            return None if current_sum < limit else node
        
        # Recursively process left and right subtrees
        node.left = dfs(node.left, current_sum)
        node.right = dfs(node.right, current_sum)
        
        # If both children are pruned, prune this node as well
        if not node.left and not node.right:
            return None
        
        return node
    
    # Start DFS from the root
    return dfs(root, 0)

# Example Test Cases
def print_tree(root):
    """Helper function to print the tree in level order for testing."""
    if not root:
        return "[]"
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

if __name__ == "__main__":
    # Test Case 1
    root1 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(-99)), TreeNode(3, TreeNode(-99), TreeNode(7, TreeNode(12), TreeNode(13))))
    limit1 = 1
    result1 = sufficientSubset(root1, limit1)
    print(print_tree(result1))  # Expected: [1, 2, 3, 4, None, None, 7, 8, 9, None, 13]

    # Test Case 2
    root2 = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(1))), TreeNode(8, TreeNode(17), TreeNode(4, None, TreeNode(5))))
    limit2 = 22
    result2 = sufficientSubset(root2, limit2)
    print(print_tree(result2))  # Expected: [5, 4, 8, 11, None, 17, 4, 7, None, None, None, None, 5]

    # Test Case 3
    root3 = TreeNode(1, TreeNode(2, TreeNode(-5)), TreeNode(-3, TreeNode(4)))
    limit3 = -1
    result3 = sufficientSubset(root3, limit3)
    print(print_tree(result3))  # Expected: [1, None, -3, 4]

"""
Time Complexity:
- Each node in the tree is visited exactly once during the DFS traversal.
- Let `n` be the number of nodes in the tree. The time complexity is O(n).

Space Complexity:
- The space complexity is determined by the recursion stack. In the worst case, the recursion stack can go as deep as the height of the tree.
- For a balanced tree, the height is O(log n). For a skewed tree, the height is O(n).
- Thus, the space complexity is O(h), where `h` is the height of the tree.

Topic: Binary Tree
"""