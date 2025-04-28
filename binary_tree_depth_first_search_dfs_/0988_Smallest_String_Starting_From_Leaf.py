"""
LeetCode Problem #988: Smallest String Starting From Leaf

Problem Statement:
Given the `root` of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z': 
a value of 0 represents 'a', a value of 1 represents 'b', and so on.

Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller: 
- For example, "ab" is lexicographically smaller than "abc".
A leaf of a node is a node that has no children.

Example 1:
Input: root = [0,1,2,3,4,3,4]
Output: "dba"

Example 2:
Input: root = [25,1,3,1,3,0,2]
Output: "adz"

Example 3:
Input: root = [2,2,1,null,1,0,null,0]
Output: "abc"

Constraints:
- The number of nodes in the tree is in the range [1, 8500].
- 0 <= Node.val <= 25
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def dfs(node, path):
            if not node:
                return None
            
            # Prepend the current character to the path
            path = chr(node.val + ord('a')) + path
            
            # If it's a leaf node, return the path
            if not node.left and not node.right:
                return path
            
            # Recurse on left and right children
            left = dfs(node.left, path)
            right = dfs(node.right, path)
            
            # Compare the results and return the lexicographically smaller one
            if left and right:
                return min(left, right)
            return left or right
        
        return dfs(root, "")

# Example Test Cases
if __name__ == "__main__":
    # Helper function to build a binary tree from a list
    def build_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    # Test Case 1
    root1 = build_tree([0, 1, 2, 3, 4, 3, 4])
    print(Solution().smallestFromLeaf(root1))  # Output: "dba"

    # Test Case 2
    root2 = build_tree([25, 1, 3, 1, 3, 0, 2])
    print(Solution().smallestFromLeaf(root2))  # Output: "adz"

    # Test Case 3
    root3 = build_tree([2, 2, 1, None, 1, 0, None, 0])
    print(Solution().smallestFromLeaf(root3))  # Output: "abc"

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each node in the binary tree is visited exactly once during the DFS traversal.
- Therefore, the time complexity is O(N), where N is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack in the DFS traversal.
- In the worst case, the recursion stack can go as deep as the height of the tree.
- For a balanced tree, the height is O(log N), and for a skewed tree, the height is O(N).
- Additionally, the space used to store the path is proportional to the height of the tree.
- Thus, the overall space complexity is O(H), where H is the height of the tree.

Topic: Binary Tree, Depth-First Search (DFS)
"""