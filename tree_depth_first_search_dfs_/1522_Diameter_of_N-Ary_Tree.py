"""
LeetCode Problem #1522: Diameter of N-Ary Tree

Problem Statement:
Given a root of an N-ary tree, you need to compute the diameter of the tree.

The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- The depth of the tree is in the range [1, 1000].
- The node values are unique.

You are given the `Node` class definition:
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

# Clean and Correct Python Solution
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def diameter(self, root: 'Node') -> int:
        self.max_diameter = 0

        def dfs(node):
            if not node:
                return 0

            # Store the heights of the two longest paths from the current node
            max1, max2 = 0, 0
            for child in node.children:
                child_height = dfs(child)
                if child_height > max1:
                    max1, max2 = child_height, max1
                elif child_height > max2:
                    max2 = child_height

            # Update the maximum diameter found so far
            self.max_diameter = max(self.max_diameter, max1 + max2)

            # Return the height of the tree rooted at the current node
            return max1 + 1

        dfs(root)
        return self.max_diameter

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = Node(1, [
        Node(2, [
            Node(4),
            Node(5)
        ]),
        Node(3)
    ])
    print(Solution().diameter(root1))  # Output: 3

    # Example 2
    root2 = Node(1, [
        Node(2),
        Node(3, [
            Node(6),
            Node(7, [
                Node(8)
            ])
        ]),
        Node(4),
        Node(5)
    ])
    print(Solution().diameter(root2))  # Output: 4

    # Example 3
    root3 = Node(1)
    print(Solution().diameter(root3))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each node in the tree is visited exactly once during the DFS traversal.
- If there are N nodes in the tree, the time complexity is O(N).

Space Complexity:
- The space complexity is determined by the recursion stack during the DFS traversal.
- In the worst case, the recursion stack can go as deep as the height of the tree.
- If the height of the tree is H, the space complexity is O(H).
- In the worst case, H = N (e.g., a skewed tree), so the space complexity is O(N).

Topic: Tree, Depth-First Search (DFS)
"""