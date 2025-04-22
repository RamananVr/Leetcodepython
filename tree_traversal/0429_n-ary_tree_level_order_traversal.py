"""
LeetCode Question #429: N-ary Tree Level Order Traversal

Problem Statement:
Given an n-ary tree, return the level order traversal of its nodes' values.
N-ary tree input is serialized in their level order traversal, each group of children is separated by the null value (see examples).

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

Constraints:
- The height of the n-ary tree is less than or equal to 1000.
- The total number of nodes is between [0, 10^4].

Follow up:
Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

# Solution
from collections import deque

def levelOrder(root: 'Node') -> list[list[int]]:
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            queue.extend(node.children)
        result.append(level)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = Node(1, [
        Node(3, [Node(5), Node(6)]),
        Node(2),
        Node(4)
    ])
    print(levelOrder(root1))  # Output: [[1], [3, 2, 4], [5, 6]]

    # Example 2
    root2 = Node(1, [
        Node(2),
        Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]),
        Node(4, [Node(8, [Node(12)])]),
        Node(5, [Node(9, [Node(13)]), Node(10)])
    ])
    print(levelOrder(root2))  # Output: [[1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13], [14]]

# Time and Space Complexity Analysis
# Time Complexity: O(N), where N is the total number of nodes in the tree. Each node is visited exactly once.
# Space Complexity: O(W), where W is the maximum width of the tree (maximum number of nodes at any level). 
#                   In the worst case, this could be O(N) if the tree is a complete tree.

# Topic: Tree Traversal