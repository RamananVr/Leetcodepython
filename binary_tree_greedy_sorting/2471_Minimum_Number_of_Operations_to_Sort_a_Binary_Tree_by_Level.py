"""
LeetCode Problem #2471: Minimum Number of Operations to Sort a Binary Tree by Level

Problem Statement:
You are given the root of a binary tree with `n` nodes. Each node in the tree has a distinct value from `1` to `n`.

In one operation, you can choose any two nodes at the same level and swap their values.

Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

Example:
Input: root = [1,3,2,7,6,5,4]
Output: 3
Explanation:
- Swap 3 and 2 -> [1,2,3,7,6,5,4]
- Swap 7 and 4 -> [1,2,3,4,6,5,7]
- Swap 6 and 5 -> [1,2,3,4,5,6,7]
The total number of operations is 3.

Constraints:
- The number of nodes in the tree is `n`.
- `1 <= n <= 10^5`
- `1 <= Node.val <= n`
- All the values in the tree are unique.
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minimumOperations(root: TreeNode) -> int:
    """
    Function to calculate the minimum number of operations to sort a binary tree by level.
    """
    def min_swaps_to_sort(arr):
        """
        Helper function to calculate the minimum number of swaps to sort an array.
        """
        n = len(arr)
        indexed_arr = [(val, idx) for idx, val in enumerate(arr)]
        indexed_arr.sort()  # Sort by value
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or indexed_arr[i][1] == i:
                continue

            # Find the cycle length
            cycle_length = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = indexed_arr[j][1]
                cycle_length += 1

            if cycle_length > 1:
                swaps += cycle_length - 1

        return swaps

    if not root:
        return 0

    queue = deque([root])
    total_swaps = 0

    while queue:
        level_size = len(queue)
        level_values = []

        for _ in range(level_size):
            node = queue.popleft()
            level_values.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Calculate the minimum swaps needed for this level
        total_swaps += min_swaps_to_sort(level_values)

    return total_swaps

# Example Test Cases
if __name__ == "__main__":
    # Helper function to build a binary tree from a list
    def build_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root

    # Test Case 1
    root1 = build_tree([1, 3, 2, 7, 6, 5, 4])
    print(minimumOperations(root1))  # Output: 3

    # Test Case 2
    root2 = build_tree([1, 2, 3, 4, 5, 6, 7])
    print(minimumOperations(root2))  # Output: 0

    # Test Case 3
    root3 = build_tree([1, 3, 4, 2, None, None, None])
    print(minimumOperations(root3))  # Output: 1

"""
Time Complexity:
- Let `n` be the number of nodes in the tree.
- Traversing the tree level by level takes O(n).
- For each level, sorting the array and calculating the minimum swaps takes O(k log k), where `k` is the number of nodes at that level.
- In the worst case, the sum of all levels' sizes is `n`, so the overall complexity is O(n log n).

Space Complexity:
- The space used by the queue for level-order traversal is O(w), where `w` is the maximum width of the tree.
- The space used by the `min_swaps_to_sort` function is O(k) for the visited array and indexed array, where `k` is the size of the current level.
- Overall space complexity is O(n) in the worst case.

Topic: Binary Tree, Greedy, Sorting
"""