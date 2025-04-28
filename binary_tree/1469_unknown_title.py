"""
LeetCode Problem #1469: Find All the Lonely Nodes

Problem Statement:
In a binary tree, a lonely node is a node that is the only child of its parent node. 
The root of the tree is not lonely because it does not have a parent node.

Given the `root` of a binary tree, return an array containing the values of all lonely nodes in the tree. 
Return the list in any order.

Example 1:
Input: root = [1,2,3,null,4]
Output: [4]
Explanation: Node 4 is a lonely node because it is the only child of its parent node 2.

Example 2:
Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2]
Output: [6,2]
Explanation: Node 6 and 2 are lonely nodes. Node 5 and 3 are not lonely because they have siblings.

Example 3:
Input: root = [11,99,88,77,null,null,66,55,null,null,null,null,44]
Output: [77,55,66,44]

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- Each node's value is between [1, 10^6].
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getLonelyNodes(root: TreeNode) -> list[int]:
    """
    This function finds all lonely nodes in a binary tree.
    A lonely node is a node that is the only child of its parent.
    """
    lonely_nodes = []

    def dfs(node):
        if not node:
            return
        # Check if the current node has only one child
        if node.left and not node.right:
            lonely_nodes.append(node.left.val)
        elif node.right and not node.left:
            lonely_nodes.append(node.right.val)
        # Recur for left and right children
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return lonely_nodes

# Example Test Cases
if __name__ == "__main__":
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

    # Test Case 1
    root1 = build_tree([1, 2, 3, None, 4])
    print(getLonelyNodes(root1))  # Output: [4]

    # Test Case 2
    root2 = build_tree([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2])
    print(getLonelyNodes(root2))  # Output: [6, 2]

    # Test Case 3
    root3 = build_tree([11, 99, 88, 77, None, None, 66, 55, None, None, None, None, 44])
    print(getLonelyNodes(root3))  # Output: [77, 55, 66, 44]

# Time Complexity Analysis:
# The function performs a Depth-First Search (DFS) traversal of the binary tree.
# Since each node is visited exactly once, the time complexity is O(n), where n is the number of nodes in the tree.

# Space Complexity Analysis:
# The space complexity is O(h), where h is the height of the tree. This is due to the recursive call stack.
# In the worst case (a skewed tree), h = n, so the space complexity becomes O(n).
# In the best case (a balanced tree), h = log(n), so the space complexity is O(log(n)).

# Topic: Binary Tree