"""
LeetCode Problem #2313: Minimum Flips in Binary Tree to Match Target

Problem Statement:
You are given the root of a binary tree with each node having a value of either 0 or 1. 
Additionally, you are given a target binary tree with the same structure as the input tree. 
Your task is to determine the minimum number of flips required to make the input binary tree 
match the target binary tree. A flip operation changes the value of a node from 0 to 1 or from 1 to 0.

Constraints:
- The number of nodes in the binary tree is in the range [1, 10^5].
- Each node's value is either 0 or 1.

Write a function `minFlips(root, target)` that returns the minimum number of flips required.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minFlips(root: TreeNode, target: TreeNode) -> int:
    """
    Function to calculate the minimum number of flips required to make the input binary tree
    match the target binary tree.
    """
    def dfs(node1, node2):
        # Base case: if both nodes are None, no flips are needed
        if not node1 and not node2:
            return 0
        # If one of the nodes is None, the trees are not compatible
        if not node1 or not node2:
            raise ValueError("Input and target trees must have the same structure.")
        
        # Calculate flips for the current node
        flips = 1 if node1.val != node2.val else 0
        
        # Recursively calculate flips for left and right subtrees
        flips += dfs(node1.left, node2.left)
        flips += dfs(node1.right, node2.right)
        
        return flips
    
    return dfs(root, target)

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(0, TreeNode(1), TreeNode(0))
    target1 = TreeNode(1, TreeNode(0), TreeNode(1))
    print(minFlips(root1, target1))  # Output: 3

    # Example 2
    root2 = TreeNode(1, TreeNode(0, TreeNode(1), TreeNode(0)), TreeNode(1))
    target2 = TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(1)), TreeNode(1))
    print(minFlips(root2, target2))  # Output: 2

    # Example 3
    root3 = TreeNode(0)
    target3 = TreeNode(1)
    print(minFlips(root3, target3))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function performs a depth-first traversal of the binary tree.
- Each node is visited exactly once, so the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack during the DFS traversal.
- In the worst case (a completely unbalanced tree), the recursion stack can go up to O(n).
- In the best case (a balanced tree), the recursion stack depth is O(log n).
- Therefore, the space complexity is O(n) in the worst case.

Topic: Binary Tree
"""