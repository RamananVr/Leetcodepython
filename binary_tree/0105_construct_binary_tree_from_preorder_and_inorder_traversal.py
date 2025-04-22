"""
LeetCode Question #105: Construct Binary Tree from Preorder and Inorder Traversal

Problem Statement:
Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- `preorder` and `inorder` consist of unique values.
- Each value of `inorder` also appears in `preorder`.
- `preorder` is guaranteed to be the preorder traversal of a binary tree.
- `inorder` is guaranteed to be the inorder traversal of the same tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    """
    Constructs a binary tree from preorder and inorder traversal arrays.

    :param preorder: List[int] - Preorder traversal of the binary tree
    :param inorder: List[int] - Inorder traversal of the binary tree
    :return: TreeNode - Root of the constructed binary tree
    """
    if not preorder or not inorder:
        return None

    # The first element of preorder is the root of the tree
    root_val = preorder[0]
    root = TreeNode(root_val)

    # Find the index of the root in inorder traversal
    root_index = inorder.index(root_val)

    # Recursively construct the left and right subtrees
    root.left = buildTree(preorder[1:1 + root_index], inorder[:root_index])
    root.right = buildTree(preorder[1 + root_index:], inorder[root_index + 1:])

    return root

# Helper function to print the tree in level order for testing
def level_order_traversal(root):
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
    # Remove trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = buildTree(preorder, inorder)
    print(level_order_traversal(root))  # Output: [3, 9, 20, None, None, 15, 7]

    # Test Case 2
    preorder = [-1]
    inorder = [-1]
    root = buildTree(preorder, inorder)
    print(level_order_traversal(root))  # Output: [-1]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Constructing the binary tree involves finding the root index in the inorder list, which takes O(n) in the worst case for each recursive call.
- Since there are n nodes, the overall time complexity is O(n^2) in the worst case.
- However, if we use a hashmap to store the indices of inorder elements, the lookup becomes O(1), and the time complexity improves to O(n).

Space Complexity:
- The space complexity is O(n) due to the recursion stack in the worst case (when the tree is skewed).
- Additionally, if we use a hashmap for inorder indices, it requires O(n) extra space.

Topic: Binary Tree
"""