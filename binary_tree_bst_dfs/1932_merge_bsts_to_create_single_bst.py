"""
LeetCode Question #1932: Merge BSTs to Create Single BST

Problem Statement:
You are given n binary search trees (BSTs) represented by the roots array, where each BST is represented by its root node. 
Each node is a structure with three fields: val (the value of the node), left (the left child), and right (the right child).

Your task is to merge these n BSTs into a single BST if possible. A merge is possible if:
1. All the trees in the input are valid BSTs.
2. The merged tree is also a valid BST.
3. No two nodes in the merged tree have the same value.

Return the root of the merged BST if merging is possible. Otherwise, return None.

Constraints:
- The number of trees, n, is in the range [1, 10^4].
- The number of nodes in each tree is in the range [1, 10^5].
- The value of each node is unique across all trees and is in the range [1, 10^6].

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def canMerge(trees):
    """
    Merges multiple BSTs into a single BST if possible.

    :param trees: List[TreeNode] - List of root nodes of BSTs.
    :return: TreeNode or None - Root of the merged BST or None if merging is not possible.
    """
    from collections import Counter, defaultdict

    # Step 1: Count all node values and track roots
    count = Counter()
    root_map = {}
    for root in trees:
        count[root.val] += 1
        root_map[root.val] = root

    # Step 2: Identify potential root of the merged BST
    potential_root = None
    for root in trees:
        if count[root.val] == 1:
            if potential_root is not None:
                return None  # Multiple potential roots
            potential_root = root

    if not potential_root:
        return None  # No valid root found

    # Step 3: Perform DFS to merge trees
    def dfs(node, min_val, max_val):
        if not node:
            return True
        if not (min_val < node.val < max_val):
            return False
        if node.left and node.left.val in root_map:
            node.left = root_map.pop(node.left.val)
        if node.right and node.right.val in root_map:
            node.right = root_map.pop(node.right.val)
        return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

    if not dfs(potential_root, float('-inf'), float('inf')) or root_map:
        return None  # Invalid BST or leftover nodes

    return potential_root


# Example Test Cases
if __name__ == "__main__":
    # Helper function to create a tree from a list
    def create_tree(values):
        if not values:
            return None
        nodes = {val: TreeNode(val) for val in values}
        for val, left, right in values:
            nodes[val].left = nodes.get(left)
            nodes[val].right = nodes.get(right)
        return nodes[values[0][0]]

    # Test Case 1: Valid merge
    tree1 = create_tree([(2, 1, 3)])
    tree2 = create_tree([(3, None, 4)])
    tree3 = create_tree([(4, None, None)])
    print(canMerge([tree1, tree2, tree3]))  # Expected: Root of merged BST

    # Test Case 2: Invalid merge
    tree4 = create_tree([(5, None, None)])
    print(canMerge([tree1, tree2, tree3, tree4]))  # Expected: None

    # Test Case 3: Single tree
    tree5 = create_tree([(1, None, None)])
    print(canMerge([tree5]))  # Expected: Root of the single BST


"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting node values and identifying the potential root: O(n), where n is the total number of nodes across all trees.
- DFS traversal to merge trees: O(n), as each node is visited once.
Overall: O(n)

Space Complexity:
- Storage for the `count` dictionary and `root_map`: O(n), where n is the total number of nodes.
- Recursive DFS stack: O(h), where h is the height of the merged BST.
Overall: O(n)

Topic: Binary Tree, BST, DFS
"""