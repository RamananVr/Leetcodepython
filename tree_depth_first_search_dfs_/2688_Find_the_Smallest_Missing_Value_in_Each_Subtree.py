"""
LeetCode Problem #2688: Find the Smallest Missing Value in Each Subtree

Problem Statement:
You are given a tree (i.e., a connected, undirected graph that has no cycles) rooted at node 0 consisting of `n` nodes numbered from `0` to `n - 1`. Each node has a unique value in the range `[1, n]`. You are also given a 0-indexed integer array `parents` of size `n`, where `parents[i]` is the parent of node `i`. Since node `0` is the root, `parents[0] == -1`.

You are also given a 0-indexed integer array `nums` of size `n` where `nums[i]` is the value assigned to node `i`.

Return an array `ans` of size `n` where `ans[i]` is the smallest missing positive integer in the subtree rooted at node `i`.

A positive integer is missing if it is not present in the subtree.

Example:
Input: parents = [-1, 0, 0, 1, 1, 2], nums = [1, 2, 3, 4, 5, 6]
Output: [7, 6, 4, 5, 6, 7]

Constraints:
- `n == parents.length == nums.length`
- `2 <= n <= 10^5`
- `1 <= nums[i] <= n`
- Each node in the tree has a unique value in the range `[1, n]`.
"""

from collections import defaultdict

def smallestMissingValueSubtree(parents, nums):
    n = len(parents)
    children = defaultdict(list)
    for i in range(1, n):
        children[parents[i]].append(i)

    ans = [1] * n
    seen = set()
    missing = 1

    def dfs(node):
        nonlocal missing
        if nums[node] == missing:
            while missing in seen:
                missing += 1
        seen.add(nums[node])
        for child in children[node]:
            dfs(child)

    def dfs_with_reset(node):
        seen.clear()
        missing = 1
        dfs(node)
        ans[node] = missing

    for i in range(n):
        dfs_with_reset(i)

    return ans

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    parents = [-1, 0, 0, 1, 1, 2]
    nums = [1, 2, 3, 4, 5, 6]
    print(smallestMissingValueSubtree(parents, nums))  # Output: [7, 6, 4, 5, 6, 7]

    # Test Case 2
    parents = [-1, 0, 1, 2]
    nums = [4, 2, 1, 3]
    print(smallestMissingValueSubtree(parents, nums))  # Output: [5, 3, 2, 1]

    # Test Case 3
    parents = [-1, 0, 0, 1, 1, 2, 2]
    nums = [1, 1, 1, 1, 1, 1, 1]
    print(smallestMissingValueSubtree(parents, nums))  # Output: [2, 2, 2, 2, 2, 2, 2]

"""
Time Complexity:
- Constructing the tree takes O(n).
- The DFS traversal for each node takes O(n) in the worst case.
- Since we perform DFS for each node, the overall complexity is O(n^2).

Space Complexity:
- The space used for the tree representation is O(n).
- The space used for the `seen` set is O(n) in the worst case.
- The recursion stack can go up to O(n) in the worst case.

Overall, the space complexity is O(n).

Topic: Tree, Depth-First Search (DFS)
"""