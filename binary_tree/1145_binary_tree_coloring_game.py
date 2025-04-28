"""
LeetCode Question #1145: Binary Tree Coloring Game

Problem Statement:
---------------------------------
Two players play a game on a binary tree. Player 1 starts by picking any node, and Player 2 picks another node. 
Then the players alternate turns, and in each turn, a player colors a node (which hasn't been colored yet) 
and gains control of all the uncolored nodes directly connected to it.

The game ends when all the nodes are colored. The player with the most colored nodes wins.

You are given the root of the binary tree and the number of nodes `n` in the tree. 
Node values are from 1 to n. Initially, Player 1 picks the node with value `x`. 
Player 2 can pick any node except `x`.

Return true if Player 2 can guarantee to win the game, otherwise return false.

Constraints:
- The number of nodes in the tree is `n` (1 <= n <= 100).
- The value of each node is unique (1 <= Node.val <= n).
- The binary tree is a valid binary tree.

"""

# Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        # Helper function to calculate the size of a subtree
        def count_nodes(node):
            if not node:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)
        
        # Helper function to find the node with value x
        def find_node(node, x):
            if not node:
                return None
            if node.val == x:
                return node
            return find_node(node.left, x) or find_node(node.right, x)
        
        # Find the node with value x
        x_node = find_node(root, x)
        
        # Calculate the size of the left and right subtrees of x_node
        left_size = count_nodes(x_node.left)
        right_size = count_nodes(x_node.right)
        
        # Calculate the size of the rest of the tree excluding x_node
        parent_size = n - (left_size + right_size + 1)
        
        # Player 2 can win if they can control more than half of the nodes
        return max(left_size, right_size, parent_size) > n // 2

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(7)
    n1 = 7
    x1 = 3
    print(Solution().btreeGameWinningMove(root1, n1, x1))  # Output: True

    # Example 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    root2.right.left = TreeNode(6)
    root2.right.right = TreeNode(7)
    n2 = 7
    x2 = 4
    print(Solution().btreeGameWinningMove(root2, n2, x2))  # Output: False

# Time and Space Complexity Analysis
"""
Time Complexity:
- The `count_nodes` function visits each node once, so its complexity is O(n).
- The `find_node` function also visits each node once in the worst case, so its complexity is O(n).
- Overall, the solution has a time complexity of O(n).

Space Complexity:
- The space complexity is O(h), where h is the height of the tree, due to the recursive calls in `count_nodes` and `find_node`.
- In the worst case, h = n (for a skewed tree), so the space complexity is O(n).

"""

# Topic: Binary Tree