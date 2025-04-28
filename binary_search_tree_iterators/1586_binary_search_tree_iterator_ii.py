"""
LeetCode Question #1586: Binary Search Tree Iterator II

Problem Statement:
Implement the `BSTIterator` class that represents an iterator over a binary search tree (BST). The iterator should be able to iterate forward and backward through the tree's elements in sorted order.

The `BSTIterator` class should have the following methods:
1. `__init__(self, root: TreeNode)`: Initializes an object of the `BSTIterator` class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
2. `hasNext(self) -> bool`: Returns `True` if there exists a number in the traversal to the right of the pointer, otherwise returns `False`.
3. `next(self) -> int`: Moves the pointer to the right, then returns the number at the pointer.
4. `hasPrev(self) -> bool`: Returns `True` if there exists a number in the traversal to the left of the pointer, otherwise returns `False`.
5. `prev(self) -> int`: Moves the pointer to the left, then returns the number at the pointer.

Constraints:
- The number of calls to `next`, `hasNext`, `prev`, and `hasPrev` is at most `10^4`.
- The number of nodes in the tree is in the range `[1, 5000]`.
- `-10^5 <= Node.val <= 10^5`
- All values in the tree are unique.

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
        Initialize the BSTIterator by performing an in-order traversal of the BST
        and storing the values in a list. The pointer is initialized to -1.
        """
        self.inorder_list = []
        self.pointer = -1
        self._inorder_traversal(root)

    def _inorder_traversal(self, node: TreeNode):
        """
        Helper function to perform in-order traversal of the BST and store
        the values in the inorder_list.
        """
        if not node:
            return
        self._inorder_traversal(node.left)
        self.inorder_list.append(node.val)
        self._inorder_traversal(node.right)

    def hasNext(self) -> bool:
        """
        Returns True if there exists a number in the traversal to the right of the pointer.
        """
        return self.pointer + 1 < len(self.inorder_list)

    def next(self) -> int:
        """
        Moves the pointer to the right and returns the number at the pointer.
        """
        if self.hasNext():
            self.pointer += 1
            return self.inorder_list[self.pointer]
        raise Exception("No next element")

    def hasPrev(self) -> bool:
        """
        Returns True if there exists a number in the traversal to the left of the pointer.
        """
        return self.pointer - 1 >= 0

    def prev(self) -> int:
        """
        Moves the pointer to the left and returns the number at the pointer.
        """
        if self.hasPrev():
            self.pointer -= 1
            return self.inorder_list[self.pointer]
        raise Exception("No previous element")


# Example Test Cases
if __name__ == "__main__":
    # Helper function to create a binary tree from a list
    def create_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        for i in range(len(nodes)):
            if nodes[i] is not None:
                if 2 * i + 1 < len(nodes):
                    nodes[i].left = nodes[2 * i + 1]
                if 2 * i + 2 < len(nodes):
                    nodes[i].right = nodes[2 * i + 2]
        return nodes[0]

    # Create a binary search tree
    root = create_tree([7, 3, 15, None, None, 9, 20])

    # Initialize the BSTIterator
    iterator = BSTIterator(root)

    # Test cases
    print(iterator.hasNext())  # Output: True
    print(iterator.next())     # Output: 3
    print(iterator.next())     # Output: 7
    print(iterator.hasPrev())  # Output: True
    print(iterator.prev())     # Output: 3
    print(iterator.hasNext())  # Output: True
    print(iterator.next())     # Output: 7
    print(iterator.next())     # Output: 9
    print(iterator.next())     # Output: 15
    print(iterator.hasNext())  # Output: True
    print(iterator.next())     # Output: 20
    print(iterator.hasNext())  # Output: False

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The `_inorder_traversal` method takes O(n), where n is the number of nodes in the BST, as it visits each node exactly once.
   - The `hasNext`, `next`, `hasPrev`, and `prev` methods each take O(1) time.

2. Space Complexity:
   - The `inorder_list` stores all the values of the BST, which takes O(n) space.
   - The recursion stack for `_inorder_traversal` takes O(h) space, where h is the height of the tree. In the worst case (skewed tree), h = n.

Overall:
- Time Complexity: O(n) for initialization, O(1) for each method call.
- Space Complexity: O(n).

Topic: Binary Search Tree, Iterators
"""