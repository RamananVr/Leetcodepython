"""
LeetCode Problem #1008: Construct Binary Search Tree from Preorder Traversal

Problem Statement:
Given an array of integers `preorder`, which represents the preorder traversal of a binary search tree (BST), 
construct the BST and return its root.

It is guaranteed that for the given test cases there is always possible to find a valid BST with the given 
preorder traversal.

Example 1:
Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Example 2:
Input: preorder = [1,3]
Output: [1,null,3]

Constraints:
- 1 <= preorder.length <= 100
- 1 <= preorder[i] <= 10^8
- All the values of `preorder` are unique.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bstFromPreorder(preorder):
    """
    Constructs a binary search tree (BST) from the given preorder traversal.

    :param preorder: List[int] - The preorder traversal of the BST.
    :return: TreeNode - The root of the constructed BST.
    """
    def helper(lower=float('-inf'), upper=float('inf')):
        nonlocal index
        if index == len(preorder):
            return None

        val = preorder[index]
        if val < lower or val > upper:
            return None

        index += 1
        root = TreeNode(val)
        root.left = helper(lower, val)
        root.right = helper(val, upper)
        return root

    index = 0
    return helper()

# Example Test Cases
def print_tree(root):
    """
    Helper function to print the tree in level-order traversal for testing purposes.
    """
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

if __name__ == "__main__":
    # Test Case 1
    preorder1 = [8, 5, 1, 7, 10, 12]
    root1 = bstFromPreorder(preorder1)
    print(print_tree(root1))  # Output: [8, 5, 10, 1, 7, None, 12]

    # Test Case 2
    preorder2 = [1, 3]
    root2 = bstFromPreorder(preorder2)
    print(print_tree(root2))  # Output: [1, None, 3]

    # Test Case 3
    preorder3 = [10]
    root3 = bstFromPreorder(preorder3)
    print(print_tree(root3))  # Output: [10]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function processes each node exactly once, and the recursive calls divide the problem into smaller subproblems.
- Therefore, the time complexity is O(n), where n is the number of nodes in the BST (or the length of the preorder list).

Space Complexity:
- The space complexity is determined by the recursion stack. In the worst case (when the BST is skewed), the recursion stack
  can go up to O(n). In the best case (balanced BST), the recursion stack depth is O(log n).
- Additionally, the function uses O(1) extra space for variables.

Overall Space Complexity: O(n) in the worst case.

Topic: Binary Tree
"""