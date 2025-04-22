"""
LeetCode Question #919: Complete Binary Tree Inserter

Problem Statement:
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, 
and all nodes are as far left as possible. Design a data structure that supports the following operations:

1. `CBTInserter(TreeNode root)`: Initializes the data structure with the root of a complete binary tree.
2. `int insert(int v)`: Inserts a new node with the value `v` into the tree such that it remains a complete binary tree 
   and returns the value of the parent of the inserted node.
3. `TreeNode get_root()`: Returns the root node of the tree.

Constraints:
- The number of nodes in the tree will be in the range [1, 1000].
- 0 <= Node.val <= 5000
- root is a complete binary tree.
- 0 <= v <= 5000
- At most 10^4 calls will be made to `insert`.
- It is guaranteed that every call to `insert` will result in a complete binary tree.

"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:
    def __init__(self, root: TreeNode):
        """
        Initialize the CBTInserter with the root of a complete binary tree.
        """
        self.root = root
        self.deque = deque()
        
        # Perform a level-order traversal to populate the deque with nodes
        # that are missing at least one child.
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, v: int) -> int:
        """
        Insert a new node with value v into the tree and return the value of its parent.
        """
        # The parent node is the first node in the deque.
        parent = self.deque[0]
        new_node = TreeNode(v)
        
        # Attach the new node to the parent.
        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
            # If the parent now has two children, remove it from the deque.
            self.deque.popleft()
        
        # Add the new node to the deque since it may need children in the future.
        self.deque.append(new_node)
        
        return parent.val

    def get_root(self) -> TreeNode:
        """
        Return the root node of the tree.
        """
        return self.root


# Example Test Cases
if __name__ == "__main__":
    # Create a complete binary tree with root [1, 2]
    root = TreeNode(1)
    root.left = TreeNode(2)
    
    # Initialize the CBTInserter
    cbt_inserter = CBTInserter(root)
    
    # Insert new nodes and print the parent values
    print(cbt_inserter.insert(3))  # Output: 1
    print(cbt_inserter.insert(4))  # Output: 2
    
    # Get the root of the tree and print its structure
    root = cbt_inserter.get_root()
    print(root.val)               # Output: 1
    print(root.left.val)          # Output: 2
    print(root.right.val)         # Output: 3
    print(root.left.left.val)     # Output: 4


"""
Time and Space Complexity Analysis:

1. Initialization (`__init__`):
   - Time Complexity: O(n), where n is the number of nodes in the tree. This is because we perform a level-order traversal to populate the deque.
   - Space Complexity: O(n), for storing the deque and the queue used during the traversal.

2. Insertion (`insert`):
   - Time Complexity: O(1), since we only perform constant-time operations to insert a node and update the deque.
   - Space Complexity: O(1), as we only add a single node to the deque.

3. Get Root (`get_root`):
   - Time Complexity: O(1), as we simply return the root node.
   - Space Complexity: O(1), as no additional space is used.

Overall:
- Time Complexity: O(n) for initialization, O(1) for each insertion and get_root operation.
- Space Complexity: O(n).

Topic: Binary Tree
"""