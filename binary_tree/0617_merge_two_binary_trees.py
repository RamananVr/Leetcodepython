"""
LeetCode Question #617: Merge Two Binary Trees

Problem Statement:
You are given two binary trees root1 and root2. Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum the values as the new value of the merged node. Otherwise, the non-null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

Constraints:
- The number of nodes in both trees is in the range [0, 10^4].
- -10^4 <= Node.val <= 10^4

Example:
Input: 
    root1 = [1,3,2,5]
    root2 = [2,1,3,null,4,null,7]
Output: 
    [3,4,5,5,4,null,7]

Explanation:
The merged tree is:
    Tree 1:       Tree 2:       Merged Tree:
       1             2              3
      / \           / \            / \
     3   2         1   3          4   5
    /             \     \        / \    \
   5               4     7      5   4    7
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(root1: TreeNode, root2: TreeNode) -> TreeNode:
    """
    Merges two binary trees by summing overlapping nodes and using non-null nodes when one is null.
    """
    if not root1 and not root2:
        return None
    if not root1:
        return root2
    if not root2:
        return root1
    
    # Create a new node with the sum of values from root1 and root2
    merged = TreeNode(root1.val + root2.val)
    
    # Recursively merge the left and right subtrees
    merged.left = mergeTrees(root1.left, root2.left)
    merged.right = mergeTrees(root1.right, root2.right)
    
    return merged

# Example Test Cases
def test_mergeTrees():
    # Helper function to build a tree from a list
    def build_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        for i, node in enumerate(nodes):
            if node:
                if 2 * i + 1 < len(nodes):
                    node.left = nodes[2 * i + 1]
                if 2 * i + 2 < len(nodes):
                    node.right = nodes[2 * i + 2]
        return nodes[0]

    # Helper function to convert a tree to a list (level-order traversal)
    def tree_to_list(root):
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
        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()
        return result

    # Test Case 1
    root1 = build_tree([1, 3, 2, 5])
    root2 = build_tree([2, 1, 3, None, 4, None, 7])
    merged_tree = mergeTrees(root1, root2)
    assert tree_to_list(merged_tree) == [3, 4, 5, 5, 4, None, 7]

    # Test Case 2
    root1 = build_tree([1])
    root2 = build_tree([1, 2])
    merged_tree = mergeTrees(root1, root2)
    assert tree_to_list(merged_tree) == [2, 2]

    # Test Case 3
    root1 = build_tree([])
    root2 = build_tree([1, 2, 3])
    merged_tree = mergeTrees(root1, root2)
    assert tree_to_list(merged_tree) == [1, 2, 3]

    print("All test cases passed!")

# Run the test cases
test_mergeTrees()

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each node in both trees is visited once. Therefore, the time complexity is O(min(N1, N2)), 
  where N1 and N2 are the number of nodes in root1 and root2, respectively.

Space Complexity:
- The space complexity is O(H), where H is the height of the taller tree. This is due to the 
  recursive call stack.

Topic: Binary Tree
"""