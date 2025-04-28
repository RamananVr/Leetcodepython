"""
LeetCode Problem #1490: Clone N-ary Tree

Problem Statement:
Given a root of an N-ary tree, return a deep copy (clone) of the tree.

Each node in the N-ary tree contains a value (int) and a list (List[Node]) of its children.

class Node {
    public int val;
    public List<Node> children;
}

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (see examples).

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]

Constraints:
- The depth of the n-ary tree is less than or equal to 1000.
- The total number of nodes is between [0, 10^4].

Follow up: Can your solution work for the graph problem?

"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        """
        Creates a deep copy of the given N-ary tree.
        """
        if not root:
            return None
        
        # Create a new node with the same value as the root
        cloned_root = Node(root.val)
        
        # Recursively clone each child and add to the cloned root's children
        for child in root.children:
            cloned_root.children.append(self.cloneTree(child))
        
        return cloned_root

# Example Test Cases
def test_clone_tree():
    # Helper function to build an N-ary tree from a level-order list
    def build_tree(data):
        if not data:
            return None
        root = Node(data[0])
        queue = [root]
        i = 2
        while i < len(data):
            parent = queue.pop(0)
            while i < len(data) and data[i] is not None:
                child = Node(data[i])
                parent.children.append(child)
                queue.append(child)
                i += 1
            i += 1
        return root

    # Helper function to serialize an N-ary tree to a level-order list
    def serialize_tree(root):
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.extend(node.children)
            else:
                result.append(None)
        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()
        return result

    # Test Case 1
    root1 = build_tree([1, None, 3, 2, 4, None, 5, 6])
    solution = Solution()
    cloned_root1 = solution.cloneTree(root1)
    assert serialize_tree(cloned_root1) == [1, None, 3, 2, 4, None, 5, 6]

    # Test Case 2
    root2 = build_tree([1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14])
    cloned_root2 = solution.cloneTree(root2)
    assert serialize_tree(cloned_root2) == [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14]

    # Test Case 3: Empty tree
    root3 = build_tree([])
    cloned_root3 = solution.cloneTree(root3)
    assert serialize_tree(cloned_root3) == []

    print("All test cases passed!")

# Run the test cases
test_clone_tree()

"""
Time Complexity:
- Each node in the tree is visited exactly once, and for each node, we process its children.
- Let n be the total number of nodes in the tree. The time complexity is O(n).

Space Complexity:
- The space complexity is determined by the recursion stack. In the worst case, the recursion depth is equal to the height of the tree.
- Let h be the height of the tree. The space complexity is O(h).

Topic: Tree, Recursion
"""