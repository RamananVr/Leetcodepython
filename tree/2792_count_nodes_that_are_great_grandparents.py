"""
2792. Count Nodes That Are Great Grandparents

Problem Statement:
Given the root of a binary tree, return the number of nodes that are the great-grandparent 
of at least one node with value x.

A great-grandparent of a node is the parent of its grandparent.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 1 <= Node.val <= 100

Test Cases:
1. Input: root = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], x = 2
   Output: 5
   
2. Input: root = [1,2,3,4], x = 1
   Output: 0
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumEvenGrandparent(root: Optional[TreeNode]) -> int:
    """
    Count nodes that are great-grandparents (have even values and grandchildren).
    
    Algorithm:
    1. DFS traversal with parent and grandparent tracking
    2. When at a node, check if grandparent has even value
    3. If yes, add current node's value to result
    
    Time Complexity: O(n)
    Space Complexity: O(h) where h is height of tree
    """
    def dfs(node, parent, grandparent):
        if not node:
            return 0
        
        result = 0
        
        # If grandparent exists and has even value, add current node's value
        if grandparent and grandparent.val % 2 == 0:
            result += node.val
        
        # Continue DFS with updated parent/grandparent chain
        result += dfs(node.left, node, parent)
        result += dfs(node.right, node, parent)
        
        return result
    
    return dfs(root, None, None)

def sumEvenGrandparentIterative(root: Optional[TreeNode]) -> int:
    """
    Iterative solution using stack with state tracking.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not root:
        return 0
    
    # Stack stores (node, parent, grandparent)
    stack = [(root, None, None)]
    total = 0
    
    while stack:
        node, parent, grandparent = stack.pop()
        
        # Check if current node should be counted
        if grandparent and grandparent.val % 2 == 0:
            total += node.val
        
        # Add children to stack with updated parent chain
        if node.right:
            stack.append((node.right, node, parent))
        if node.left:
            stack.append((node.left, node, parent))
    
    return total

def countGreatGrandparents(root: Optional[TreeNode], x: int) -> int:
    """
    Alternative interpretation: Count nodes that are great-grandparents of nodes with value x.
    
    Time Complexity: O(n)
    Space Complexity: O(h)
    """
    great_grandparents = set()
    
    def dfs(node, parent, grandparent, great_grandparent):
        if not node:
            return
        
        # If current node has value x and great-grandparent exists
        if node.val == x and great_grandparent:
            great_grandparents.add(great_grandparent)
        
        # Continue DFS
        dfs(node.left, node, parent, grandparent)
        dfs(node.right, node, parent, grandparent)
    
    dfs(root, None, None, None)
    return len(great_grandparents)

# Helper function to build tree from array
def build_tree_from_array(arr):
    """Build binary tree from level-order array representation."""
    if not arr or arr[0] is None:
        return None
    
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    
    while queue and i < len(arr):
        node = queue.pop(0)
        
        # Left child
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    
    return root

# Test cases
def test_sum_even_grandparent():
    # Test case 1: Tree with even grandparents
    #       1
    #      / \
    #     7   3
    #    / \   \
    #   2   7   8
    #  / \   \   \
    # 2   9   1   4
    arr1 = [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5]
    root1 = build_tree_from_array(arr1)
    result1 = sumEvenGrandparent(root1)
    print(f"Test 1 - Sum of nodes with even grandparents: {result1}")
    
    # Test case 2: Single node
    root2 = TreeNode(1)
    result2 = sumEvenGrandparent(root2)
    print(f"Test 2 - Single node: {result2}")
    
    # Test case 3: No even grandparents
    #     1
    #    / \
    #   3   5
    #  / \
    # 7   9
    root3 = TreeNode(1)
    root3.left = TreeNode(3)
    root3.right = TreeNode(5)
    root3.left.left = TreeNode(7)
    root3.left.right = TreeNode(9)
    result3 = sumEvenGrandparent(root3)
    print(f"Test 3 - No even grandparents: {result3}")

def test_iterative_solution():
    # Test iterative vs recursive
    arr = [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5]
    root = build_tree_from_array(arr)
    
    result_recursive = sumEvenGrandparent(root)
    result_iterative = sumEvenGrandparentIterative(root)
    
    print(f"Recursive result: {result_recursive}")
    print(f"Iterative result: {result_iterative}")
    print(f"Results match: {result_recursive == result_iterative}")

if __name__ == "__main__":
    test_sum_even_grandparent()
    test_iterative_solution()

"""
Topic Classification: Binary Tree, DFS, Recursion

Key Insights:
1. Track parent and grandparent while traversing the tree
2. When visiting a node, check if grandparent has even value
3. Can be solved both recursively and iteratively
4. Time complexity is O(n) as we visit each node once

Complexity Analysis:
- Time Complexity: O(n), where n is number of nodes
- Space Complexity: O(h) for recursion stack, where h is height of tree
"""
