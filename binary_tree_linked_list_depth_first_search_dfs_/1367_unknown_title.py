"""
LeetCode Problem #1367: Linked List in Binary Tree

Problem Statement:
Given a binary tree root and a linked list with head as the first node. 
Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context, downward path means a path that starts at some node and goes downwards (possibly ending at any node).

Example 1:
Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: True
Explanation: Nodes in blue form a subpath in the binary tree.

Example 2:
Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: True

Example 3:
Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: False

Constraints:
- The number of nodes in the tree will be in the range [1, 2500].
- The number of nodes in the linked list will be in the range [1, 100].
- 1 <= Node.val <= 100 for each node in the linked list and binary tree.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubPath(head: ListNode, root: TreeNode) -> bool:
    def dfs(tree_node, list_node):
        if not list_node:  # If the linked list is fully traversed, return True
            return True
        if not tree_node:  # If the binary tree node is None, return False
            return False
        if tree_node.val != list_node.val:  # If values don't match, return False
            return False
        # Continue matching the linked list with the left or right subtree
        return dfs(tree_node.left, list_node.next) or dfs(tree_node.right, list_node.next)

    if not root:  # If the binary tree is empty, return False
        return False
    # Check if the current tree node matches the linked list or recurse on left/right subtree
    return dfs(root, head) or isSubPath(head, root.left) or isSubPath(head, root.right)

# Example Test Cases
if __name__ == "__main__":
    # Helper function to create a linked list from a list
    def create_linked_list(values):
        dummy = ListNode()
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    # Helper function to create a binary tree from a list (level-order traversal)
    from collections import deque
    def create_binary_tree(values):
        if not values:
            return None
        root = TreeNode(values[0])
        queue = deque([root])
        i = 1
        while i < len(values):
            node = queue.popleft()
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        return root

    # Test Case 1
    head = create_linked_list([4, 2, 8])
    root = create_binary_tree([1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3])
    print(isSubPath(head, root))  # Output: True

    # Test Case 2
    head = create_linked_list([1, 4, 2, 6])
    root = create_binary_tree([1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3])
    print(isSubPath(head, root))  # Output: True

    # Test Case 3
    head = create_linked_list([1, 4, 2, 6, 8])
    root = create_binary_tree([1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3])
    print(isSubPath(head, root))  # Output: False

# Time and Space Complexity Analysis
# Time Complexity: O(N * M), where N is the number of nodes in the binary tree and M is the number of nodes in the linked list.
# Space Complexity: O(M), due to the recursion stack depth being proportional to the length of the linked list.

# Topic: Binary Tree, Linked List, Depth-First Search (DFS)