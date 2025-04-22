"""
LeetCode Question #113: Path Sum II

Problem Statement:
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Constraints:
- The number of nodes in the tree is in the range [0, 5000].
- -1000 <= Node.val <= 1000
- -1000 <= targetSum <= 1000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root: TreeNode, targetSum: int) -> list[list[int]]:
    """
    Finds all root-to-leaf paths in the binary tree where the sum of the node values equals targetSum.

    :param root: TreeNode, the root of the binary tree
    :param targetSum: int, the target sum to match
    :return: List of lists, where each list represents a valid path
    """
    def dfs(node, current_path, current_sum):
        if not node:
            return
        
        # Add the current node's value to the path and update the sum
        current_path.append(node.val)
        current_sum += node.val

        # Check if it's a leaf node and the sum matches targetSum
        if not node.left and not node.right and current_sum == targetSum:
            result.append(list(current_path))
        else:
            # Recurse on the left and right children
            dfs(node.left, current_path, current_sum)
            dfs(node.right, current_path, current_sum)
        
        # Backtrack: remove the current node from the path
        current_path.pop()

    result = []
    dfs(root, [], 0)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Example 1:
    # Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    # Output: [[5,4,11,2],[5,8,4,5]]
    root1 = TreeNode(5)
    root1.left = TreeNode(4)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(11)
    root1.left.left.left = TreeNode(7)
    root1.left.left.right = TreeNode(2)
    root1.right.left = TreeNode(13)
    root1.right.right = TreeNode(4)
    root1.right.right.left = TreeNode(5)
    root1.right.right.right = TreeNode(1)
    targetSum1 = 22
    print(pathSum(root1, targetSum1))  # Expected: [[5,4,11,2],[5,8,4,5]]

    # Example 2:
    # Input: root = [1,2,3], targetSum = 5
    # Output: []
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    targetSum2 = 5
    print(pathSum(root2, targetSum2))  # Expected: []

    # Example 3:
    # Input: root = [1,2], targetSum = 0
    # Output: []
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    targetSum3 = 0
    print(pathSum(root3, targetSum3))  # Expected: []

"""
Time Complexity:
- Each node is visited once, and for each node, we perform constant-time operations (appending to a list, checking conditions, etc.).
- Therefore, the time complexity is O(N), where N is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack and the space used to store the paths.
- In the worst case, the recursion stack can go as deep as the height of the tree, which is O(H), where H is the height of the tree.
- Additionally, the result list can store up to O(N) nodes in the worst case (if all nodes are part of valid paths).
- Therefore, the overall space complexity is O(N + H).

Topic: Binary Tree, Depth-First Search (DFS), Backtracking
"""