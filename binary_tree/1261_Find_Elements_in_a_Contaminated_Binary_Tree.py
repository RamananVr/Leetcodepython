"""
LeetCode Problem #1261: Find Elements in a Contaminated Binary Tree

Problem Statement:
Given a binary tree with the following rules:
1. Every node's value in the binary tree is either -1 or a non-negative integer.
2. Initially, the binary tree is "contaminated," meaning all node values are set to -1.

You are tasked to "recover" the tree by following these rules:
- The root node's value is set to 0.
- If a node's value is `x`, then its left child is assigned the value `2 * x + 1`, and its right child is assigned the value `2 * x + 2`.

Implement the `FindElements` class:
- `FindElements(TreeNode root)`: Initializes the object with the contaminated binary tree and recovers it.
- `bool find(int target)`: Returns `True` if the target value exists in the recovered binary tree, otherwise returns `False`.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- `-1 <= Node.val <= 10^4`
- `target` is in the range [0, 10^6].
- It is guaranteed that the tree is a binary tree.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root: TreeNode):
        """
        Initialize the FindElements object and recover the tree.
        """
        self.recovered_values = set()
        self._recover_tree(root, 0)

    def _recover_tree(self, node: TreeNode, value: int):
        """
        Recursively recover the tree and store all valid node values in a set.
        """
        if not node:
            return
        node.val = value
        self.recovered_values.add(value)
        self._recover_tree(node.left, 2 * value + 1)
        self._recover_tree(node.right, 2 * value + 2)

    def find(self, target: int) -> bool:
        """
        Check if the target value exists in the recovered tree.
        """
        return target in self.recovered_values


# Example Test Cases
if __name__ == "__main__":
    # Example 1
    contaminated_tree = TreeNode(-1)
    contaminated_tree.left = TreeNode(-1)
    contaminated_tree.right = TreeNode(-1)
    contaminated_tree.left.left = TreeNode(-1)
    contaminated_tree.left.right = TreeNode(-1)

    find_elements = FindElements(contaminated_tree)
    print(find_elements.find(1))  # Output: True
    print(find_elements.find(3))  # Output: True
    print(find_elements.find(5))  # Output: False

    # Example 2
    contaminated_tree_2 = TreeNode(-1)
    contaminated_tree_2.right = TreeNode(-1)

    find_elements_2 = FindElements(contaminated_tree_2)
    print(find_elements_2.find(2))  # Output: True
    print(find_elements_2.find(3))  # Output: False


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The `_recover_tree` method visits each node exactly once, so its time complexity is O(n), where n is the number of nodes in the tree.
   - The `find` method checks for the existence of a value in a set, which has an average time complexity of O(1).
   - Overall, the time complexity is O(n) for initialization and O(1) for each `find` operation.

2. Space Complexity:
   - The space complexity is O(n) to store the recovered values in a set.
   - Additionally, the recursion stack in `_recover_tree` can go up to O(h), where h is the height of the tree. In the worst case (skewed tree), h = n.
   - Overall, the space complexity is O(n).

Topic: Binary Tree
"""