"""
LeetCode Problem #1530: Number of Good Leaf Nodes Pairs

Problem Statement:
Given the root of a binary tree and an integer distance, a pair of two different leaf nodes of a binary tree is considered good 
if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.

Example 1:
Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes are 4 and 3, and the length of the shortest path between them is 3. This is the only good pair.

Example 2:
Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The leaf nodes pairs are (4,5) and (6,7), and the lengths of their paths are 2 and 2 respectively.

Constraints:
- The number of nodes in the tree is in the range [1, 2 * 10^4].
- 1 <= Node.val <= 100
- 1 <= distance <= 10
"""

# Python Solution
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]  # Leaf node, return distance 1
            
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            # Count good pairs
            for l in left_distances:
                for r in right_distances:
                    if l + r <= distance:
                        self.result += 1
            
            # Return updated distances for the current node
            return [d + 1 for d in left_distances + right_distances if d + 1 <= distance]
        
        self.result = 0
        dfs(root)
        return self.result

# Example Test Cases
def test():
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
    root1 = build_tree([1, 2, 3, None, 4])
    distance1 = 3
    assert solution.countPairs(root1, distance1) == 1

    # Test Case 2
    root2 = build_tree([1, 2, 3, 4, 5, 6, 7])
    distance2 = 3
    assert solution.countPairs(root2, distance2) == 2

    # Test Case 3
    root3 = build_tree([1])
    distance3 = 1
    assert solution.countPairs(root3, distance3) == 0

    print("All test cases passed!")

# Run the tests
if __name__ == "__main__":
    test()

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each node in the tree is visited once during the DFS traversal, so the time complexity is O(n), where n is the number of nodes in the tree.
- For each node, we compare distances from its left and right subtrees, which is bounded by the maximum distance (10). Thus, the comparison step is O(1).
- Overall, the time complexity is O(n).

Space Complexity:
- The space complexity is determined by the recursion stack during DFS traversal. In the worst case (skewed tree), the recursion stack can go up to O(h), where h is the height of the tree.
- Additionally, we store distances for leaf nodes, which is bounded by the number of leaf nodes. In the worst case, this is O(n).
- Overall, the space complexity is O(n).

Topic: Binary Tree
"""