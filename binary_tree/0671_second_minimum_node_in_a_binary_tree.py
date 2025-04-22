"""
LeetCode Question #671: Second Minimum Node In a Binary Tree

Problem Statement:
Given a non-empty special binary tree consisting of nodes with the non-negative value, 
where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, 
then this node's value is the smaller value among its two sub-nodes. More formally, the property 
root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the 
nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Constraints:
- The number of nodes in the tree is in the range [1, 25].
- 1 <= Node.val <= 2^31 - 1
- root.val == min(root.left.val, root.right.val) for each internal node of the tree with two children.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findSecondMinimumValue(root: TreeNode) -> int:
    """
    This function finds the second minimum value in a special binary tree.
    If no such value exists, it returns -1.
    """
    # Helper function to traverse the tree and collect unique values
    def dfs(node):
        if not node:
            return
        unique_values.add(node.val)
        dfs(node.left)
        dfs(node.right)

    # Use a set to store unique values in the tree
    unique_values = set()
    dfs(root)

    # Remove the smallest value (root value) and find the second smallest
    min_val = root.val
    unique_values.discard(min_val)

    return min(unique_values) if unique_values else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    root1 = TreeNode(2)
    root1.left = TreeNode(2)
    root1.right = TreeNode(5)
    root1.right.left = TreeNode(5)
    root1.right.right = TreeNode(7)
    print(findSecondMinimumValue(root1))  # Output: 5

    # Test Case 2
    root2 = TreeNode(2)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    print(findSecondMinimumValue(root2))  # Output: -1

    # Test Case 3
    root3 = TreeNode(1)
    root3.left = TreeNode(1)
    root3.right = TreeNode(3)
    print(findSecondMinimumValue(root3))  # Output: 3

    # Test Case 4
    root4 = TreeNode(2)
    print(findSecondMinimumValue(root4))  # Output: -1

"""
Time Complexity Analysis:
- The function performs a Depth-First Search (DFS) traversal of the binary tree.
- In the worst case, we visit all nodes exactly once. Let n be the number of nodes in the tree.
- Time complexity: O(n), where n is the number of nodes in the tree.

Space Complexity Analysis:
- The space complexity is determined by the recursion stack and the set used to store unique values.
- In the worst case, the recursion stack can go as deep as the height of the tree, which is O(h), where h is the height of the tree.
- The set can store up to n unique values, so its space complexity is O(n).
- Overall space complexity: O(n).

Topic: Binary Tree
"""