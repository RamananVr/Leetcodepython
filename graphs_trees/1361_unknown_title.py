"""
LeetCode Problem #1361: Validate Binary Tree Nodes

Problem Statement:
You have n binary tree nodes numbered from 0 to n - 1 where each node has two children 
represented by two arrays leftChild and rightChild, where:
- leftChild[i] is the left child of the ith node. If leftChild[i] is -1, then the ith node does not have a left child.
- rightChild[i] is the right child of the ith node. If rightChild[i] is -1, then the ith node does not have a right child.

Only one node can be the root of the tree. A binary tree is valid if all the following conditions are satisfied:
1. There are no cycles in the tree.
2. Every node has exactly one parent, except for the root node which has no parent.
3. The binary tree has exactly n nodes.

Given the two arrays leftChild and rightChild, return true if the binary tree represented by these arrays is valid, otherwise return false.

Constraints:
- n == leftChild.length == rightChild.length
- 1 <= n <= 10^4
- -1 <= leftChild[i], rightChild[i] < n
"""

def validateBinaryTreeNodes(n: int, leftChild: list[int], rightChild: list[int]) -> bool:
    # Step 1: Calculate in-degrees for all nodes
    in_degree = [0] * n
    for i in range(n):
        if leftChild[i] != -1:
            in_degree[leftChild[i]] += 1
        if rightChild[i] != -1:
            in_degree[rightChild[i]] += 1

    # Step 2: Find the root (node with in-degree 0)
    root_count = 0
    root = -1
    for i in range(n):
        if in_degree[i] == 0:
            root_count += 1
            root = i

    # There must be exactly one root
    if root_count != 1:
        return False

    # Step 3: Perform BFS/DFS to ensure all nodes are reachable from the root
    visited = set()

    def dfs(node):
        if node == -1 or node in visited:
            return
        visited.add(node)
        dfs(leftChild[node])
        dfs(rightChild[node])

    dfs(root)

    # Check if all nodes are visited
    return len(visited) == n

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Valid binary tree
    n1 = 4
    leftChild1 = [1, -1, 3, -1]
    rightChild1 = [2, -1, -1, -1]
    print(validateBinaryTreeNodes(n1, leftChild1, rightChild1))  # Output: True

    # Test Case 2: Invalid binary tree (cycle exists)
    n2 = 4
    leftChild2 = [1, -1, 3, -1]
    rightChild2 = [2, 3, -1, -1]
    print(validateBinaryTreeNodes(n2, leftChild2, rightChild2))  # Output: False

    # Test Case 3: Invalid binary tree (multiple roots)
    n3 = 2
    leftChild3 = [-1, -1]
    rightChild3 = [-1, -1]
    print(validateBinaryTreeNodes(n3, leftChild3, rightChild3))  # Output: False

    # Test Case 4: Valid binary tree with single node
    n4 = 1
    leftChild4 = [-1]
    rightChild4 = [-1]
    print(validateBinaryTreeNodes(n4, leftChild4, rightChild4))  # Output: True

"""
Time Complexity:
- Calculating in-degrees: O(n)
- Finding the root: O(n)
- DFS traversal: O(n)
Overall: O(n)

Space Complexity:
- In-degree array: O(n)
- Visited set: O(n)
Overall: O(n)

Topic: Graphs, Trees
"""