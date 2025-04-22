"""
LeetCode Problem #606: Construct String from Binary Tree

Problem Statement:
You need to construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way. 
The null node needs to be represented by an empty pair of parenthesis "()". 
And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   / 
  4  
Output: "1(2(4))(3)"

Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 
Output: "1(2()(4))(3)"

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        if not root:
            return ""
        
        # Convert the root value to string
        result = str(root.val)
        
        # If there is a left child, recursively process it
        if root.left:
            result += f"({self.tree2str(root.left)})"
        # If there is no left child but there is a right child, add empty parenthesis for the left
        elif root.right:
            result += "()"
        
        # If there is a right child, recursively process it
        if root.right:
            result += f"({self.tree2str(root.right)})"
        
        return result

# Example Test Cases
def test_tree2str():
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

    solution = Solution()

    # Test Case 1
    root1 = build_tree([1, 2, 3, 4])
    assert solution.tree2str(root1) == "1(2(4))(3)"

    # Test Case 2
    root2 = build_tree([1, 2, 3, None, 4])
    assert solution.tree2str(root2) == "1(2()(4))(3)"

    # Test Case 3
    root3 = build_tree([1])
    assert solution.tree2str(root3) == "1"

    # Test Case 4
    root4 = build_tree([1, 2, None, 3])
    assert solution.tree2str(root4) == "1(2(3))"

    print("All test cases passed!")

# Run the test cases
if __name__ == "__main__":
    test_tree2str()

"""
Time Complexity:
- Each node in the binary tree is visited exactly once, and the string concatenation for each node is O(1).
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack. In the worst case (a completely unbalanced tree), the recursion stack can go as deep as the height of the tree.
- The height of the tree can be O(n) in the worst case (e.g., a skewed tree), so the space complexity is O(n).

Topic: Binary Tree
"""