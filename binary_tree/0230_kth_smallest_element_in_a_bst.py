"""
LeetCode Question #230: Kth Smallest Element in a BST

Problem Statement:
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:
- The number of nodes in the tree is n.
- 1 <= k <= n
- 0 <= Node.val <= 10^4

Follow up:
If the BST is modified often (i.e., we can insert and delete nodes), and you need to repeatedly find the kth smallest, how would you optimize?
"""

# Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: TreeNode, k: int) -> int:
    """
    Finds the kth smallest element in a BST using an in-order traversal.
    """
    def in_order_traversal(node):
        if not node:
            return []
        return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)
    
    # Perform in-order traversal to get sorted elements
    sorted_elements = in_order_traversal(root)
    return sorted_elements[k - 1]

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.right = TreeNode(2)
    k1 = 1
    print(kthSmallest(root1, k1))  # Output: 1

    # Example 2
    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.left.left.left = TreeNode(1)
    k2 = 3
    print(kthSmallest(root2, k2))  # Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- The in-order traversal visits each node exactly once, so the time complexity is O(n), where n is the number of nodes in the BST.

Space Complexity:
- The space complexity is O(n) due to the storage of the in-order traversal result in the `sorted_elements` list.
- Additionally, the recursion stack in the worst case (for a completely unbalanced tree) can go up to O(n).

Overall: Time = O(n), Space = O(n)
"""

# Topic: Binary Tree