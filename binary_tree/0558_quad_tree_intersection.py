"""
LeetCode Question #558: Quad Tree Intersection

Problem Statement:
A quad tree is a tree data structure in which each internal node has exactly four children. Quad trees are often used to partition a two-dimensional space by recursively subdividing it into four quadrants or regions.

We want to store a boolean value in each node. The leaf nodes represent a grid of size 1x1. For each node, it is either a leaf node or has four children. If it is a leaf node, the `val` variable represents the value of that leaf node (True for 1, False for 0). If it has four children, then the `val` variable is not used.

You are given two quad trees `quadTree1` and `quadTree2`. Both quad trees represent a `n * n` grid. Return a quad tree that represents the logical OR of the two grids.

A leaf node is True if its value is 1, and False if its value is 0. The logical OR operation is defined as follows:
- A leaf node with value True OR a leaf node with value False results in a leaf node with value True.
- A leaf node with value False OR a leaf node with value False results in a leaf node with value False.
- A non-leaf node OR a leaf node results in a non-leaf node.
- A non-leaf node OR a non-leaf node results in a non-leaf node.

Constraints:
- `quadTree1` and `quadTree2` are both valid quad trees representing a grid of size `n * n`.
- `n == 2^k` where `0 <= k <= 10`.

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

def intersect(quadTree1: Node, quadTree2: Node) -> Node:
    """
    Function to compute the logical OR of two quad trees.
    """
    if quadTree1.isLeaf:
        # If quadTree1 is a leaf node, return quadTree1 if its value is True, otherwise return quadTree2.
        return quadTree1 if quadTree1.val else quadTree2
    if quadTree2.isLeaf:
        # If quadTree2 is a leaf node, return quadTree2 if its value is True, otherwise return quadTree1.
        return quadTree2 if quadTree2.val else quadTree1
    
    # Recursively compute the OR for each quadrant.
    topLeft = intersect(quadTree1.topLeft, quadTree2.topLeft)
    topRight = intersect(quadTree1.topRight, quadTree2.topRight)
    bottomLeft = intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
    bottomRight = intersect(quadTree1.bottomRight, quadTree2.bottomRight)
    
    # If all children are leaf nodes and have the same value, merge them into a single leaf node.
    if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and \
       topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
        return Node(topLeft.val, True)
    
    # Otherwise, return a non-leaf node with the computed children.
    return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)

# Example Test Cases
def test_intersect():
    # Example 1
    quadTree1 = Node(True, True)
    quadTree2 = Node(False, True)
    result = intersect(quadTree1, quadTree2)
    assert result.isLeaf == True and result.val == True, "Test Case 1 Failed"

    # Example 2
    quadTree1 = Node(False, True)
    quadTree2 = Node(False, True)
    result = intersect(quadTree1, quadTree2)
    assert result.isLeaf == True and result.val == False, "Test Case 2 Failed"

    # Example 3
    quadTree1 = Node(False, False, 
                     Node(True, True), Node(False, True), 
                     Node(False, True), Node(False, True))
    quadTree2 = Node(False, False, 
                     Node(False, True), Node(False, True), 
                     Node(False, True), Node(True, True))
    result = intersect(quadTree1, quadTree2)
    assert result.isLeaf == False and result.topLeft.val == True and result.bottomRight.val == True, "Test Case 3 Failed"

    print("All test cases passed!")

# Time and Space Complexity Analysis
"""
Time Complexity:
- Each node in the quad tree is visited once. If the quad tree represents an `n * n` grid, the number of nodes is proportional to `O(n^2)`.
- Therefore, the time complexity is `O(n^2)`.

Space Complexity:
- The space complexity is determined by the recursion stack. In the worst case, the depth of the recursion is proportional to the height of the quad tree, which is `O(log(n))`.
- Therefore, the space complexity is `O(log(n))`.

"""

# Topic: Binary Tree
if __name__ == "__main__":
    test_intersect()