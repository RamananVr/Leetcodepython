"""
LeetCode Problem #2476: Closest Nodes Queries in a Binary Search Tree

Problem Statement:
You are given the root of a binary search tree (BST) and an array `queries` of integers. 
Find the closest nodes to each query in the BST. For each query, return a pair of integers 
representing the closest smaller or equal value and the closest greater or equal value in the BST. 
If there is no such value, return -1 for that value.

The BST is guaranteed to have unique values.

Input:
- root: The root of the binary search tree.
- queries: A list of integers.

Output:
- A list of pairs of integers, where each pair corresponds to the closest smaller or equal value 
  and the closest greater or equal value for each query.

Constraints:
- The number of nodes in the tree is in the range [1, 10^5].
- The value of each node is in the range [1, 10^6].
- The number of queries is in the range [1, 10^4].
- The value of each query is in the range [1, 10^6].
"""

# Solution
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def closestNodes(root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
    # Helper function to perform an in-order traversal and collect all node values in sorted order
    def in_order_traversal(node):
        if not node:
            return []
        return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)
    
    # Get all values in the BST in sorted order
    sorted_values = in_order_traversal(root)
    
    # Helper function to find the closest smaller or equal and greater or equal values
    def find_closest(query):
        # Binary search for the closest values
        left, right = 0, len(sorted_values) - 1
        smaller_or_equal, greater_or_equal = -1, -1
        
        while left <= right:
            mid = (left + right) // 2
            if sorted_values[mid] == query:
                return [sorted_values[mid], sorted_values[mid]]
            elif sorted_values[mid] < query:
                smaller_or_equal = sorted_values[mid]
                left = mid + 1
            else:
                greater_or_equal = sorted_values[mid]
                right = mid - 1
        
        return [smaller_or_equal, greater_or_equal]
    
    # Process each query and find the closest nodes
    result = []
    for query in queries:
        result.append(find_closest(query))
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Helper function to build a BST from a list of values
    def insert_into_bst(root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = insert_into_bst(root.left, val)
        else:
            root.right = insert_into_bst(root.right, val)
        return root
    
    # Build the BST
    values = [4, 2, 6, 1, 3, 5, 7]
    root = None
    for val in values:
        root = insert_into_bst(root, val)
    
    # Queries
    queries = [0, 4, 8]
    
    # Expected Output: [[-1, 1], [4, 4], [7, -1]]
    print(closestNodes(root, queries))

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - In-order traversal of the BST takes O(n), where n is the number of nodes in the tree.
   - For each query, we perform a binary search on the sorted list of values, which takes O(log n).
   - If there are q queries, the total time complexity is O(n + q * log n).

2. Space Complexity:
   - The space required to store the sorted list of values is O(n).
   - The recursion stack for the in-order traversal takes O(h), where h is the height of the tree.
   - In the worst case (balanced BST), h = O(log n). In the worst case (skewed BST), h = O(n).
   - Overall space complexity is O(n).

Topic: Binary Search Tree (BST), Binary Search
"""