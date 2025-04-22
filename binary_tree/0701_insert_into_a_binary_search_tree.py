"""
LeetCode Question #701: Insert into a Binary Search Tree

Problem Statement:
You are given the root node of a binary search tree (BST) and a value to insert into the tree. 
Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. 
You can return any of them.

Example 1:
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]

Example 2:
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]

Example 3:
Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]

Constraints:
- The number of nodes in the tree will be in the range [0, 10^4].
- -10^8 <= Node.val <= 10^8
- All the values Node.val are unique.
- -10^8 <= val <= 10^8
- It's guaranteed that val does not exist in the original BST.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(root: TreeNode, val: int) -> TreeNode:
    """
    Inserts a value into a Binary Search Tree (BST) and returns the root of the updated tree.
    """
    if not root:
        # If the tree is empty, create a new node with the value and return it.
        return TreeNode(val)
    
    # Traverse the tree to find the correct position for the new value.
    if val < root.val:
        # If the value is less than the current node, go to the left subtree.
        root.left = insertIntoBST(root.left, val)
    else:
        # If the value is greater than the current node, go to the right subtree.
        root.right = insertIntoBST(root.right, val)
    
    return root

# Example Test Cases
def print_tree(root):
    """Helper function to print the tree in level-order for testing."""
    if not root:
        return []
    from collections import deque
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
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
    root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    val1 = 5
    updated_root1 = insertIntoBST(root1, val1)
    print(print_tree(updated_root1))  # Output: [4, 2, 7, 1, 3, 5]

    # Test Case 2
    root2 = TreeNode(40, TreeNode(20, TreeNode(10), TreeNode(30)), TreeNode(60, TreeNode(50), TreeNode(70)))
    val2 = 25
    updated_root2 = insertIntoBST(root2, val2)
    print(print_tree(updated_root2))  # Output: [40, 20, 60, 10, 30, 50, 70, None, None, 25]

    # Test Case 3
    root3 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    val3 = 8
    updated_root3 = insertIntoBST(root3, val3)
    print(print_tree(updated_root3))  # Output: [4, 2, 7, 1, 3, None, 8]

"""
Time and Space Complexity Analysis:

Time Complexity:
- In the worst case, we traverse the height of the tree to find the correct position for the new value.
- For a balanced BST, the height is O(log n), where n is the number of nodes.
- For a skewed BST, the height is O(n).
- Therefore, the time complexity is O(h), where h is the height of the tree.

Space Complexity:
- The space complexity is O(h) due to the recursive call stack, where h is the height of the tree.
- In the worst case (skewed tree), the space complexity is O(n).
- In the best case (balanced tree), the space complexity is O(log n).

Topic: Binary Tree
"""