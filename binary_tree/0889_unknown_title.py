"""
LeetCode Problem #889: Construct Binary Tree from Preorder and Postorder Traversal

Problem Statement:
Given two integer arrays, `preorder` and `postorder`, where `preorder` is the preorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree, reconstruct the binary tree and return its root.

The input arrays are guaranteed to be valid traversals of a binary tree.

Constraints:
- 1 <= preorder.length <= 30
- 1 <= postorder.length <= 30
- preorder and postorder consist of unique values between 1 and 30.

Example:
Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

Note:
The output is the root of the binary tree. You can return the tree in any traversal format (e.g., level order traversal) for testing purposes.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructFromPrePost(preorder, postorder):
    """
    Constructs a binary tree from its preorder and postorder traversals.

    :param preorder: List[int] - Preorder traversal of the binary tree
    :param postorder: List[int] - Postorder traversal of the binary tree
    :return: TreeNode - Root of the constructed binary tree
    """
    if not preorder or not postorder:
        return None
    
    # The first element of preorder is the root
    root = TreeNode(preorder[0])
    
    # If there's only one node, return it
    if len(preorder) == 1:
        return root
    
    # Find the index of the left subtree's root in postorder
    left_subtree_root_index = postorder.index(preorder[1])
    
    # Split preorder and postorder into left and right subtrees
    left_preorder = preorder[1:left_subtree_root_index + 2]
    right_preorder = preorder[left_subtree_root_index + 2:]
    left_postorder = postorder[:left_subtree_root_index + 1]
    right_postorder = postorder[left_subtree_root_index + 1:-1]
    
    # Recursively construct left and right subtrees
    root.left = constructFromPrePost(left_preorder, left_postorder)
    root.right = constructFromPrePost(right_preorder, right_postorder)
    
    return root

# Helper function to perform level order traversal for testing
def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    preorder = [1, 2, 4, 5, 3, 6, 7]
    postorder = [4, 5, 2, 6, 7, 3, 1]
    root = constructFromPrePost(preorder, postorder)
    print(level_order_traversal(root))  # Output: [1, 2, 3, 4, 5, 6, 7]

    # Test Case 2
    preorder = [1, 2, 3]
    postorder = [3, 2, 1]
    root = constructFromPrePost(preorder, postorder)
    print(level_order_traversal(root))  # Output: [1, 2, 3]

    # Test Case 3
    preorder = [1]
    postorder = [1]
    root = constructFromPrePost(preorder, postorder)
    print(level_order_traversal(root))  # Output: [1]

"""
Time Complexity:
- The function splits the preorder and postorder arrays recursively. At each level, the split operation takes O(n) time.
- The recursion depth is proportional to the height of the tree, which is O(log n) for a balanced tree and O(n) for a skewed tree.
- In the worst case, the time complexity is O(n^2).

Space Complexity:
- The space complexity is dominated by the recursion stack. In the worst case (skewed tree), the recursion depth is O(n).
- Additionally, the function creates new lists for left and right subtrees, which also take O(n) space.
- Overall space complexity: O(n).

Topic: Binary Tree
"""