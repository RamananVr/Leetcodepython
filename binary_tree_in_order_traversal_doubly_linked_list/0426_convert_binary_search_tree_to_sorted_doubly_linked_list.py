"""
LeetCode Question #426: Convert Binary Search Tree to Sorted Doubly Linked List

Problem Statement:
Convert a Binary Search Tree (BST) to a sorted circular doubly-linked list in-place. 
You can think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list. 
For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

Specifically, we want to do the transformation in such a way that the left pointer of each node points to its predecessor, 
and the right pointer points to its successor. We should return the pointer to the smallest element of the linked list.

Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -10^5 <= Node.val <= 10^5
- All the values of the tree are unique.
"""

# Definition for a Node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        # Initialize pointers for the head and the previous node
        self.head = None
        self.prev = None

        # Helper function to perform in-order traversal
        def in_order_traversal(node):
            if not node:
                return
            
            # Traverse the left subtree
            in_order_traversal(node.left)
            
            # Process the current node
            if self.prev:
                # Link the previous node with the current node
                self.prev.right = node
                node.left = self.prev
            else:
                # If this is the first node, set it as the head
                self.head = node
            
            # Update the previous node to the current node
            self.prev = node
            
            # Traverse the right subtree
            in_order_traversal(node.right)
        
        # Perform in-order traversal to build the doubly linked list
        in_order_traversal(root)
        
        # Connect the head and tail to make it circular
        self.head.left = self.prev
        self.prev.right = self.head
        
        return self.head

# Example Test Cases
def print_doubly_linked_list(head: 'Node', count: int):
    """Helper function to print the doubly linked list."""
    result = []
    current = head
    for _ in range(count):
        result.append(current.val)
        current = current.right
    print(" -> ".join(map(str, result)))

if __name__ == "__main__":
    # Example 1
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    solution = Solution()
    head = solution.treeToDoublyList(root)
    print("Example 1:")
    print_doubly_linked_list(head, 5)  # Output: 1 -> 2 -> 3 -> 4 -> 5

    # Example 2
    root = Node(1)
    solution = Solution()
    head = solution.treeToDoublyList(root)
    print("Example 2:")
    print_doubly_linked_list(head, 1)  # Output: 1

    # Example 3
    root = None
    solution = Solution()
    head = solution.treeToDoublyList(root)
    print("Example 3:")
    print(head)  # Output: None

"""
Time Complexity:
- The time complexity is O(n), where n is the number of nodes in the BST. This is because we perform an in-order traversal of the tree, visiting each node exactly once.

Space Complexity:
- The space complexity is O(h), where h is the height of the BST. This is the space used by the recursion stack during the in-order traversal. In the worst case (skewed tree), h = n, and in the best case (balanced tree), h = log(n).

Topic: Binary Tree, In-Order Traversal, Doubly Linked List
"""