"""
LeetCode Problem #1430: Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree

Problem Statement:
Given a binary tree where each node contains an integer value, and a sequence represented by an array of integers, 
write a function to check whether the sequence is a valid sequence from the root to a leaf node in the binary tree.

A valid sequence is defined as follows:
- The sequence must start at the root node of the tree.
- The sequence must end at a leaf node.
- The sequence must match the values of the nodes along the path from the root to the leaf.

Return true if the given sequence is a valid sequence, otherwise return false.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^4 <= Node.val <= 10^4
- The sequence is an array of integers with a length in the range [1, 10^4].
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidSequence(root: TreeNode, arr: list[int]) -> bool:
    """
    Function to check if the given sequence is a valid sequence from root to leaf in the binary tree.
    """
    def dfs(node, index):
        # If the node is None or the index is out of bounds, return False
        if not node or index >= len(arr):
            return False
        
        # If the current node's value does not match the current sequence value, return False
        if node.val != arr[index]:
            return False
        
        # If we are at the last index of the sequence, check if the current node is a leaf
        if index == len(arr) - 1:
            return not node.left and not node.right
        
        # Recursively check the left and right subtrees
        return dfs(node.left, index + 1) or dfs(node.right, index + 1)
    
    # Start the DFS from the root and the first index of the sequence
    return dfs(root, 0)

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(0)
    root1.left = TreeNode(1)
    root1.right = TreeNode(0)
    root1.left.left = TreeNode(0)
    root1.left.right = TreeNode(1)
    root1.right.left = TreeNode(0)
    root1.left.left.right = TreeNode(1)
    root1.left.right.left = TreeNode(0)
    root1.left.right.right = TreeNode(0)
    arr1 = [0, 1, 0, 1]
    print(isValidSequence(root1, arr1))  # Output: True

    # Example 2
    arr2 = [0, 0, 1]
    print(isValidSequence(root1, arr2))  # Output: False

    # Example 3
    arr3 = [0, 1, 1]
    print(isValidSequence(root1, arr3))  # Output: True

    # Example 4
    root2 = TreeNode(1)
    arr4 = [1]
    print(isValidSequence(root2, arr4))  # Output: True

    # Example 5
    arr5 = [1, 2]
    print(isValidSequence(root2, arr5))  # Output: False

"""
Time and Space Complexity Analysis:
1. Time Complexity:
   - In the worst case, we traverse all nodes in the binary tree. 
   - If the tree has N nodes, the time complexity is O(N).

2. Space Complexity:
   - The space complexity is determined by the recursion stack. 
   - In the worst case, the recursion stack can go as deep as the height of the tree.
   - For a balanced binary tree, the height is O(log N). For a skewed tree, the height is O(N).
   - Therefore, the space complexity is O(H), where H is the height of the tree.

Topic: Binary Tree
"""