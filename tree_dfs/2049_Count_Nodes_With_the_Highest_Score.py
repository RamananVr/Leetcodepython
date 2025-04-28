"""
LeetCode Problem #2049: Count Nodes With the Highest Score

Problem Statement:
You are given a binary tree rooted at 0 consisting of `n` nodes. The nodes are numbered from `0` to `n - 1`. 
You are also given a 0-indexed integer array `parents` representing the tree, where `parents[i]` is the parent of node `i`. 
Since node 0 is the root, `parents[0] == -1`.

Each node has a score. To find the score of a node, consider if the node and the edges connected to it were removed. 
The tree would become one or more non-empty subtrees. The size of a subtree is the number of the nodes in it. 
The score of the node is the product of the sizes of all those subtrees.

Return the number of nodes that have the highest score.

Constraints:
- `n == parents.length`
- `2 <= n <= 10^5`
- `parents[0] == -1`
- `0 <= parents[i] <= n - 1` for `i != 0`
- `parents` represents a valid binary tree.
"""

from collections import defaultdict

def countHighestScoreNodes(parents):
    # Step 1: Build the tree as an adjacency list
    tree = defaultdict(list)
    for child, parent in enumerate(parents):
        if parent != -1:
            tree[parent].append(child)
    
    # Step 2: Helper function to calculate subtree sizes and scores
    n = len(parents)
    subtree_sizes = [0] * n
    max_score = 0
    count = 0

    def dfs(node):
        nonlocal max_score, count
        size = 1  # Include the current node
        score = 1  # Start with a score of 1

        # Calculate the size of each subtree
        for child in tree[node]:
            child_size = dfs(child)
            size += child_size
            score *= child_size  # Multiply the sizes of subtrees

        # Calculate the size of the "remaining" tree (excluding the current subtree)
        remaining_size = n - size
        if remaining_size > 0:
            score *= remaining_size

        # Update the maximum score and count
        if score > max_score:
            max_score = score
            count = 1
        elif score == max_score:
            count += 1

        subtree_sizes[node] = size
        return size

    # Step 3: Start DFS from the root node (0)
    dfs(0)

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    parents = [-1, 2, 0, 2, 0]
    print(countHighestScoreNodes(parents))  # Output: 3

    # Test Case 2
    parents = [-1, 0, 0, 1, 1, 2, 2]
    print(countHighestScoreNodes(parents))  # Output: 2

    # Test Case 3
    parents = [-1, 0]
    print(countHighestScoreNodes(parents))  # Output: 1

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Building the tree as an adjacency list takes O(n) time.
   - The DFS traversal visits each node exactly once, so it also takes O(n) time.
   - Overall, the time complexity is O(n).

2. Space Complexity:
   - The adjacency list representation of the tree takes O(n) space.
   - The `subtree_sizes` array takes O(n) space.
   - The recursion stack for DFS can go up to O(n) in the worst case (for a skewed tree).
   - Overall, the space complexity is O(n).

Topic: Tree, DFS
"""