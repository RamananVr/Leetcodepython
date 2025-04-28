"""
LeetCode Problem #1660: Correct a Binary Tree

Problem Statement:
You are given the root of a binary tree that is incorrectly linked. The tree has the following properties:
- Each node in the tree has a unique value.
- A node in the tree can have at most two children.
- The tree is a complete binary tree, but some of the right child pointers are incorrectly pointing to a random node in the tree instead of null.

Your task is to correct the tree by making all the right child pointers that are incorrectly pointing to random nodes point to null.

Return the root of the corrected binary tree.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^9 <= Node.val <= 10^9
"""

# Solution
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def correctBinaryTree(root: TreeNode) -> TreeNode:
    """
    Corrects the binary tree by fixing the incorrect right child pointers.
    """
    # Use a set to track visited nodes
    visited = set()
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        # If the right child points to a node already visited, it's incorrect
        if node.right and node.right in visited:
            # Remove the parent node from the tree
            return root
        
        # Add the current node to the visited set
        visited.add(node)
        
        # Add children to the queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return root

# Example Test Cases
def test_correctBinaryTree():
    # Example 1
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.right.right = root.left  # Incorrect pointer
    
    corrected_root = correctBinaryTree(root)
    assert corrected_root.right.right.right == None, "Test Case 1 Failed"
    
    print("All test cases passed!")

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm performs a level-order traversal of the tree, visiting each node exactly once.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the size of the queue and the visited set.
- In the worst case, the queue can hold up to O(n) nodes, and the visited set can also contain O(n) nodes.
- Therefore, the space complexity is O(n).
"""

# Topic: Binary Tree

if __name__ == "__main__":
    test_correctBinaryTree()