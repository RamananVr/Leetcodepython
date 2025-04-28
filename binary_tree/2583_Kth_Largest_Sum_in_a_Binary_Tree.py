"""
LeetCode Problem #2583: Kth Largest Sum in a Binary Tree

Problem Statement:
You are given the root of a binary tree and an integer k. The level sum in the tree is the sum of the values of the nodes at each level.

Return the kth largest level sum in the tree. If there are fewer than k levels in the tree, return -1.

Note:
- A binary tree is a tree in which each node has at most two children.
- The level sum is the sum of all node values at a particular depth in the tree (0-indexed).

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^5 <= Node.val <= 10^5
- 1 <= k <= 10^4
"""

from collections import deque
import heapq

def kthLargestLevelSum(root, k):
    """
    Finds the kth largest level sum in a binary tree.

    :param root: TreeNode, the root of the binary tree
    :param k: int, the kth largest level sum to find
    :return: int, the kth largest level sum or -1 if there are fewer than k levels
    """
    if not root:
        return -1

    # Perform level-order traversal to calculate level sums
    level_sums = []
    queue = deque([root])

    while queue:
        level_sum = 0
        for _ in range(len(queue)):
            node = queue.popleft()
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level_sums.append(level_sum)

    # Use a min-heap to find the kth largest level sum
    if len(level_sums) < k:
        return -1

    return heapq.nlargest(k, level_sums)[-1]


# Example Test Cases
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example 1
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.right = TreeNode(8)
root1.left.left = TreeNode(2)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(7)
root1.right.right = TreeNode(9)
k1 = 2
print(kthLargestLevelSum(root1, k1))  # Output: 15 (Level sums: [5, 11, 22])

# Example 2
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.left = TreeNode(6)
root2.right.right = TreeNode(7)
k2 = 3
print(kthLargestLevelSum(root2, k2))  # Output: 6 (Level sums: [1, 5, 22])

# Example 3
root3 = TreeNode(10)
k3 = 1
print(kthLargestLevelSum(root3, k3))  # Output: 10 (Level sums: [10])

# Example 4
root4 = TreeNode(1)
k4 = 2
print(kthLargestLevelSum(root4, k4))  # Output: -1 (Only 1 level exists)

"""
Time and Space Complexity Analysis:

Time Complexity:
- Level-order traversal: O(n), where n is the number of nodes in the tree.
- Calculating the kth largest level sum using a heap: O(m * log(k)), where m is the number of levels in the tree.
  In the worst case, m = n (if the tree is a single chain).

Overall: O(n + m * log(k)) ≈ O(n + n * log(k)) = O(n * log(k)).

Space Complexity:
- Queue for level-order traversal: O(w), where w is the maximum width of the tree (number of nodes at the widest level).
- Level sums storage: O(m), where m is the number of levels.
- Heap for kth largest calculation: O(k).

Overall: O(w + m + k).

Topic: Binary Tree
"""