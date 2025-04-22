"""
LeetCode Question #173: Binary Search Tree Iterator

Problem Statement:
Implement the `BSTIterator` class that represents an iterator over a binary search tree (BST). The iterator should be initialized with the root node of the BST. It should support the following operations:

1. `__init__(self, root: TreeNode)`: Initializes an object of the `BSTIterator` class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
2. `int next()`: Returns the next smallest number in the BST.
3. `bool hasNext()`: Returns `True` if there exists a number in the traversal to the right of the pointer, otherwise returns `False`.

Constraints:
- The number of nodes in the tree is in the range `[1, 10^5]`.
- `0 <= Node.val <= 10^6`
- You may assume that `next()` calls will always be valid (i.e., there will be at least a next number in the BST when `next()` is called).

Follow-up:
- Could you implement the `BSTIterator` using only O(h) memory, where h is the height of the tree?
- Could you implement the `BSTIterator` such that `next()` and `hasNext()` functions run in average O(1) time and use O(h) memory?

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        """
        Initialize the BSTIterator with the root of the BST.
        Use a stack to simulate the in-order traversal iteratively.
        """
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node: TreeNode):
        """
        Helper function to push all the leftmost nodes of the subtree
        rooted at `node` onto the stack.
        """
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        Return the next smallest number in the BST.
        """
        # Pop the topmost node from the stack
        topmost_node = self.stack.pop()
        # If the popped node has a right child, process its leftmost subtree
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        """
        Return True if there exists a next number in the BST traversal.
        """
        return len(self.stack) > 0


# Example Test Cases
if __name__ == "__main__":
    # Example 1: Construct a BST
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    # Initialize the iterator
    iterator = BSTIterator(root)

    # Test next() and hasNext()
    print(iterator.next())    # Output: 3
    print(iterator.next())    # Output: 7
    print(iterator.hasNext()) # Output: True
    print(iterator.next())    # Output: 9
    print(iterator.hasNext()) # Output: True
    print(iterator.next())    # Output: 15
    print(iterator.hasNext()) # Output: True
    print(iterator.next())    # Output: 20
    print(iterator.hasNext()) # Output: False


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - `next()`: Each call to `next()` involves popping a node from the stack and potentially pushing all the leftmost nodes of the right subtree onto the stack. In the worst case, this operation takes O(h) time, where h is the height of the tree. However, across all calls to `next()`, each node is pushed and popped from the stack exactly once, so the amortized time complexity is O(1) per call.
   - `hasNext()`: This operation simply checks if the stack is non-empty, which takes O(1) time.

2. Space Complexity:
   - The space complexity is determined by the stack, which stores at most O(h) nodes at any time, where h is the height of the tree. In the worst case, h = O(log n) for a balanced BST and h = O(n) for a skewed BST.

Topic: Binary Tree
"""