"""
LeetCode Problem #427: Construct Quad Tree

Problem Statement:
We want to use quad-trees to represent a 2D area. Each cell in the grid has a value of either 0 or 1. The root node represents the whole grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same.

Each node has the following attributes:
- `val`: True if the node represents a grid of 1's, False otherwise.
- `isLeaf`: True if the node is a leaf node on the quad tree, False otherwise.
- `topLeft`, `topRight`, `bottomLeft`, `bottomRight`: The four children of the current node.

Write a function to construct a quad tree from a given 2D grid. The function should return the root of the quad tree.

The input grid is guaranteed to be a square grid with a length that is a power of 2 (e.g., 1, 2, 4, 8, ...).

Example:
Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,0],[0,1],[1,0]]
Explanation: The grid is as follows:
    0 1
    1 0
Notice that the topLeft, topRight, bottomLeft, and bottomRight sub-grids all have different values, so the root node is not a leaf. The output represents the structure of the quad tree.

Constraints:
- `n == grid.length == grid[i].length`
- `n` is a power of 2.
- `1 <= n <= 64`
"""

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid):
        """
        Constructs a quad tree from the given grid.
        
        :type grid: List[List[int]]
        :rtype: Node
        """
        def is_uniform(x, y, length):
            """Check if all values in the grid section are the same."""
            val = grid[x][y]
            for i in range(x, x + length):
                for j in range(y, y + length):
                    if grid[i][j] != val:
                        return False, None
            return True, val

        def build(x, y, length):
            """Recursively build the quad tree."""
            uniform, val = is_uniform(x, y, length)
            if uniform:
                return Node(val == 1, True)
            
            half = length // 2
            topLeft = build(x, y, half)
            topRight = build(x, y + half, half)
            bottomLeft = build(x + half, y, half)
            bottomRight = build(x + half, y + half, half)
            
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

        return build(0, 0, len(grid))

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    grid1 = [[0, 1], [1, 0]]
    root1 = solution.construct(grid1)
    print(root1)  # Output: QuadTree structure (not directly printable)

    # Test Case 2
    grid2 = [[1, 1], [1, 1]]
    root2 = solution.construct(grid2)
    print(root2)  # Output: QuadTree structure (not directly printable)

    # Test Case 3
    grid3 = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]
    root3 = solution.construct(grid3)
    print(root3)  # Output: QuadTree structure (not directly printable)

"""
Time Complexity:
- The function `is_uniform` checks all cells in a sub-grid, which takes O(n^2) in the worst case.
- The recursive function `build` divides the grid into four parts at each level, and the depth of recursion is log(n) (base 2).
- Overall, the time complexity is O(n^2 log(n)).

Space Complexity:
- The recursion stack depth is O(log(n)) due to the recursive calls.
- The space required for the quad tree nodes is proportional to the number of nodes, which is O(n^2) in the worst case.
- Overall, the space complexity is O(n^2).

Topic: Binary Tree, Divide and Conquer
"""