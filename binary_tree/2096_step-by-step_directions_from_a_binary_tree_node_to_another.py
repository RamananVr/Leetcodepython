"""
LeetCode Question #2096: Step-By-Step Directions From a Binary Tree Node to Another

Problem Statement:
You are given the root of a binary tree with `n` nodes. Each node is uniquely assigned a value from `1` to `n`. 
You are also given an integer `startValue`, representing the value of the start node, and an integer `destValue`, 
representing the value of the destination node.

Find the shortest path from the node with value `startValue` to the node with value `destValue`. Return a string 
consisting of only the characters `'L'`, `'R'`, and `'U'` that represents the directions to go from the start node 
to the destination node:
- `'L'` means to go from a node to its left child.
- `'R'` means to go from a node to its right child.
- `'U'` means to go from a node to its parent.

Note:
- The test cases are generated such that there is always a path from `startValue` to `destValue`.

Constraints:
- The number of nodes in the tree is `n`.
- `2 <= n <= 10^5`
- `1 <= Node.val <= n`
- All `Node.val` are unique.
- `1 <= startValue, destValue <= n`

"""

# Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getDirections(root: TreeNode, startValue: int, destValue: int) -> str:
    def findPath(node, target, path):
        """Helper function to find the path from the root to a target node."""
        if not node:
            return False
        if node.val == target:
            return True
        path.append('L')
        if findPath(node.left, target, path):
            return True
        path.pop()
        path.append('R')
        if findPath(node.right, target, path):
            return True
        path.pop()
        return False

    # Find paths from root to startValue and destValue
    startPath, destPath = [], []
    findPath(root, startValue, startPath)
    findPath(root, destValue, destPath)

    # Find the common prefix length
    i = 0
    while i < len(startPath) and i < len(destPath) and startPath[i] == destPath[i]:
        i += 1

    # Directions: 'U' for moving up from startValue, then append remaining destPath
    return 'U' * (len(startPath) - i) + ''.join(destPath[i:])

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(4)
    startValue = 3
    destValue = 6
    print(getDirections(root, startValue, destValue))  # Output: "UUUR"

    # Example 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    startValue = 4
    destValue = 7
    print(getDirections(root, startValue, destValue))  # Output: "UUUR"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The `findPath` function traverses the tree to find the path to a target node. In the worst case, it visits all nodes, 
  so its time complexity is O(n), where n is the number of nodes in the tree.
- Since we call `findPath` twice (once for `startValue` and once for `destValue`), the total time complexity is O(n).

Space Complexity:
- The space complexity is determined by the recursion stack used in `findPath`. In the worst case, the tree is skewed, 
  and the recursion stack can go up to O(n). Additionally, the `startPath` and `destPath` lists store the paths, which 
  can also have a length of O(n) in the worst case. Therefore, the overall space complexity is O(n).

Topic: Binary Tree
"""