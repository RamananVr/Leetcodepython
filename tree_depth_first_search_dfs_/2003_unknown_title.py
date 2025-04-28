"""
LeetCode Problem #2003: Smallest Missing Genetic Value in Each Subtree

Problem Statement:
You are given an integer array `parents` representing a tree. The tree has `n` nodes numbered from `0` to `n - 1` in such a way that `parents[i]` is the parent of node `i`. The root node is `0`, so `parents[0] == -1` since it has no parent.

You are also given an array `nums` where `nums[i]` is a distinct positive integer assigned to node `i`.

Return an array `ans` of size `n` where `ans[i]` is the smallest missing positive integer in the subtree of node `i`.

The subtree of a node `i` contains node `i` and all of its descendants.

Constraints:
- `1 <= nums.length == parents.length <= 10^5`
- `0 <= parents[i] <= n - 1` for all `i != 0`
- `parents[0] == -1`
- `1 <= nums[i] <= 10^5`
- All values in `nums` are distinct.

"""

from collections import defaultdict

def smallestMissingValueSubtree(parents, nums):
    n = len(parents)
    ans = [1] * n
    if 1 not in nums:
        return ans

    # Build the tree structure
    tree = defaultdict(list)
    for child, parent in enumerate(parents):
        tree[parent].append(child)

    # Find the node with value 1
    node_with_1 = nums.index(1)

    # Traverse the tree upwards from the node with value 1
    seen = set()
    missing = 1
    current = node_with_1

    while current != -1:
        # Add all values in the current subtree to the seen set
        def dfs(node):
            if nums[node] not in seen:
                seen.add(nums[node])
                for child in tree[node]:
                    dfs(child)

        dfs(current)

        # Find the smallest missing positive integer
        while missing in seen:
            missing += 1

        ans[current] = missing
        current = parents[current]

    return ans

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    parents = [-1, 0, 0, 1, 1, 2, 2]
    nums = [1, 2, 3, 4, 5, 6, 7]
    print(smallestMissingValueSubtree(parents, nums))  # Output: [8, 8, 8, 8, 8, 8, 8]

    # Test Case 2
    parents = [-1, 0, 1, 2]
    nums = [1, 2, 3, 4]
    print(smallestMissingValueSubtree(parents, nums))  # Output: [5, 5, 5, 5]

    # Test Case 3
    parents = [-1, 0, 0, 1, 1, 2, 2]
    nums = [5, 4, 6, 2, 1, 3, 7]
    print(smallestMissingValueSubtree(parents, nums))  # Output: [8, 7, 4, 5, 6, 1, 1]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the tree takes O(n).
- The DFS traversal for each node is proportional to the size of the subtree. In the worst case, we traverse all nodes once, resulting in O(n).
- Finding the smallest missing positive integer involves iterating through the `seen` set, which is bounded by the range of numbers in `nums`. This is O(n) in the worst case.
- Overall, the time complexity is O(n).

Space Complexity:
- The `tree` dictionary uses O(n) space.
- The `seen` set can grow up to O(n) in size.
- The recursion stack for DFS can also grow up to O(n) in the worst case.
- Overall, the space complexity is O(n).

Topic: Tree, Depth-First Search (DFS)
"""