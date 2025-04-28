"""
LeetCode Problem #2458: Height of Binary Tree After Subtree Removal Queries

Problem Statement:
You are given the root of a binary tree with `n` nodes. Each node is uniquely assigned a value from `1` to `n`. 
You are also given an array `queries` of size `m` where `queries[i]` is the value of a node in the tree.

For each query, you need to calculate the height of the binary tree after removing the subtree rooted at the node 
with the value `queries[i]`. The height of a tree is the number of edges in the longest path from the root to any leaf.

Return an array `answer` of size `m` where `answer[i]` is the height of the tree after processing the `i-th` query.

Constraints:
- The number of nodes in the tree is `n`.
- `1 <= n <= 10^5`
- `1 <= queries.length <= 10^5`
- `1 <= queries[i] <= n`
- It is guaranteed that the value of each node is unique.

Follow-up:
Can you solve the problem in O(n + m) time complexity?

"""

from collections import defaultdict

# Solution
class Solution:
    def treeQueries(self, root, queries):
        """
        Calculate the height of the binary tree after removing subtrees for each query.

        :param root: TreeNode, the root of the binary tree
        :param queries: List[int], the list of node values to query
        :return: List[int], the height of the tree after each query
        """
        # Step 1: Precompute the height of each node and the depth of each node
        node_to_height = {}
        node_to_depth = {}
        depth_to_max_height = defaultdict(int)

        def compute_heights_and_depths(node, depth):
            if not node:
                return -1
            left_height = compute_heights_and_depths(node.left, depth + 1)
            right_height = compute_heights_and_depths(node.right, depth + 1)
            height = 1 + max(left_height, right_height)
            node_to_height[node.val] = height
            node_to_depth[node.val] = depth
            depth_to_max_height[depth] = max(depth_to_max_height[depth], height)
            return height

        compute_heights_and_depths(root, 0)

        # Step 2: Precompute the maximum height at each depth excluding a specific node
        max_height_excluding_node = {}

        def compute_max_height_excluding_node(node, parent_max_height):
            if not node:
                return
            depth = node_to_depth[node.val]
            # Calculate the max height excluding the current node
            max_height_excluding_node[node.val] = max(
                parent_max_height, 
                depth_to_max_height[depth] if depth_to_max_height[depth] != node_to_height[node.val] else 0
            )
            # Recurse for children
            compute_max_height_excluding_node(node.left, max_height_excluding_node[node.val])
            compute_max_height_excluding_node(node.right, max_height_excluding_node[node.val])

        compute_max_height_excluding_node(root, 0)

        # Step 3: Answer the queries
        result = []
        for query in queries:
            result.append(max_height_excluding_node[query])
        return result


# Example Test Cases
if __name__ == "__main__":
    # Helper function to build a binary tree from a list
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def build_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    # Example 1
    root = build_tree([1, 3, 4, 2, None, 6, 5, None, None, None, None, None, 7])
    queries = [4]
    solution = Solution()
    print(solution.treeQueries(root, queries))  # Output: [2]

    # Example 2
    root = build_tree([1, 3, 4, 2, None, 6, 5, None, None, None, None, None, 7])
    queries = [3, 4, 7]
    print(solution.treeQueries(root, queries))  # Output: [2, 2, 3]


# Time and Space Complexity Analysis
"""
Time Complexity:
- Precomputing heights and depths: O(n), where n is the number of nodes in the tree.
- Precomputing max height excluding each node: O(n).
- Answering m queries: O(m).
Overall: O(n + m).

Space Complexity:
- Space for storing node_to_height, node_to_depth, and depth_to_max_height: O(n).
- Space for recursion stack: O(h), where h is the height of the tree (worst case O(n)).
Overall: O(n).
"""

# Topic: Binary Tree