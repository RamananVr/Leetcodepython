"""
LeetCode Problem #2440: Create Components With Same Value

Problem Statement:
You are given a tree (i.e., a connected, undirected graph with no cycles) consisting of `n` nodes numbered from `0` to `n - 1` and exactly `n - 1` edges. Each node has a value associated with it, given in the integer array `nums`. The sum of all values in `nums` is `sum(nums)`.

You are also given a 2D integer array `edges` of size `(n - 1) x 2` where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the tree.

You want to partition the tree into connected components by removing some edges. Each component should have the same value, which is the sum of the values of its nodes.

Return the maximum number of components you can create.

Constraints:
- `1 <= n <= 2 * 10^4`
- `nums.length == n`
- `1 <= nums[i] <= 50`
- `edges.length == n - 1`
- `0 <= ai, bi < n`
- `ai != bi`
- The input is guaranteed to be a tree.

"""

from collections import defaultdict
from typing import List

def componentValue(nums: List[int], edges: List[List[int]]) -> int:
    def can_partition(target_sum: int) -> bool:
        # Perform a DFS to check if we can partition the tree into components with sum = target_sum
        def dfs(node: int, parent: int) -> int:
            current_sum = nums[node]
            for neighbor in graph[node]:
                if neighbor != parent:
                    child_sum = dfs(neighbor, node)
                    if child_sum == -1:  # If a subtree cannot be partitioned, propagate failure
                        return -1
                    current_sum += child_sum
            if current_sum > target_sum:  # If the sum exceeds target, it's invalid
                return -1
            return 0 if current_sum == target_sum else current_sum

        return dfs(0, -1) == 0

    # Build the graph from the edges
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    total_sum = sum(nums)
    max_components = 1

    # Try all possible target sums (divisors of total_sum)
    for k in range(1, total_sum + 1):
        if total_sum % k == 0:  # k is a valid divisor
            target_sum = total_sum // k
            if can_partition(target_sum):
                max_components = max(max_components, k)

    return max_components

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [1, 2, 1, 1, 1]
    edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
    print(componentValue(nums, edges))  # Output: 4

    # Test Case 2
    nums = [1, 1, 1, 1]
    edges = [[0, 1], [1, 2], [1, 3]]
    print(componentValue(nums, edges))  # Output: 3

    # Test Case 3
    nums = [2, 2, 2, 2, 2]
    edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
    print(componentValue(nums, edges))  # Output: 5

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Building the graph takes O(n) time.
   - The outer loop iterates over all divisors of `sum(nums)`. In the worst case, this is O(sqrt(sum(nums))).
   - For each divisor, we perform a DFS traversal of the tree, which takes O(n) time.
   - Therefore, the overall time complexity is O(n * sqrt(sum(nums))).

2. Space Complexity:
   - The graph representation uses O(n) space.
   - The recursion stack for DFS can go up to O(n) in the worst case.
   - Thus, the overall space complexity is O(n).

Topic: Graphs, Tree, DFS
"""