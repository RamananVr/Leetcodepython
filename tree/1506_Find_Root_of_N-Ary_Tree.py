"""
LeetCode Problem #1506: Find Root of N-Ary Tree

Problem Statement:
You are given all the nodes of an N-ary tree as an array `tree` where each node is represented as a `Node` object with:
- `val`: an integer representing the node's value.
- `children`: a list of child `Node` objects.

Each node is unique and may appear in the `children` list of other nodes. The tree has a single root node, and all nodes are descendants of the root node.

Return the root node of the N-ary tree.

Constraints:
- The total number of nodes is between [1, 5 * 10^4].
- Each node has a unique value.

Follow-up:
Could you solve this problem with O(1) space complexity (excluding the input and output)?

"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def findRoot(tree):
    """
    Finds the root of an N-ary tree.

    Args:
    tree (List[Node]): List of all nodes in the N-ary tree.

    Returns:
    Node: The root node of the N-ary tree.
    """
    # Use the sum of all node values and subtract the sum of all child node values.
    # The remaining value corresponds to the root node's value.
    total_sum = 0
    for node in tree:
        total_sum += node.val
        for child in node.children:
            total_sum -= child.val
    
    # Find the node with the remaining value (root node).
    for node in tree:
        if node.val == total_sum:
            return node

# Example Test Cases
def example_test_cases():
    # Example 1
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    node1.children = [node2, node3, node4]
    node3.children = [node5, node6]

    tree = [node1, node2, node3, node4, node5, node6]
    assert findRoot(tree) == node1

    # Example 2
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)

    node7.children = [node8, node9]
    node8.children = [node10]

    tree = [node7, node8, node9, node10]
    assert findRoot(tree) == node7

    print("All test cases passed!")

# Time and Space Complexity Analysis
"""
Time Complexity:
- Iterating through all nodes in the tree takes O(n), where n is the number of nodes.
- Iterating through the children of each node also takes O(n) in total since each child is processed exactly once.
- Thus, the overall time complexity is O(n).

Space Complexity:
- The algorithm uses O(1) additional space since it only uses a single integer variable (`total_sum`) to store the sum.
- The input and output are excluded from the space complexity analysis.
- Thus, the space complexity is O(1).
"""

# Topic: Tree
if __name__ == "__main__":
    example_test_cases()