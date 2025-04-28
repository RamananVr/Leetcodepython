"""
LeetCode Problem #1443: Minimum Time to Collect All Apples in a Tree

Problem Statement:
Given an undirected tree consisting of `n` vertices numbered from `0` to `n-1`, which has `n-1` edges, 
where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi`. 
Each node has a boolean value `hasApple[i]` that indicates whether or not there is an apple at that node.

You start at node `0` and you have to collect all the apples in the tree. 
You can only move through the edges of the tree and each edge takes 1 second to traverse. 
Return the minimum time in seconds you need to collect all the apples in the tree.

Constraints:
- `1 <= n <= 10^5`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= ai, bi < n`
- `ai != bi`
- `hasApple.length == n`
- `hasApple[i]` is `True` or `False`
- The input represents a valid tree.

Example:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,True,True,False]
Output: 8
Explanation: The figure below represents the given tree. The minimum time to collect all apples is 8 seconds.

         0
       /   \
      1     2
     / \   / \
    4   5 3   6
    (T) (T)    (T)

Note:
- You can visit a node multiple times.
- You can reuse edges multiple times.
"""

from collections import defaultdict
from typing import List

def minTime(n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
    # Build the adjacency list for the tree
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)

    def dfs(node: int, parent: int) -> int:
        # Initialize the time to collect apples from this subtree
        time = 0
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            # Recursively calculate the time for the subtree
            subtree_time = dfs(neighbor, node)
            if subtree_time > 0 or hasApple[neighbor]:
                time += subtree_time + 2  # Add 2 for the round trip to the child
        return time

    # Start DFS from the root node (0) with no parent (-1)
    return dfs(0, -1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 7
    edges1 = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    hasApple1 = [False, False, True, False, True, True, False]
    print(minTime(n1, edges1, hasApple1))  # Output: 8

    # Test Case 2
    n2 = 4
    edges2 = [[0,1],[1,2],[0,3]]
    hasApple2 = [True, True, True, False]
    print(minTime(n2, edges2, hasApple2))  # Output: 6

    # Test Case 3
    n3 = 4
    edges3 = [[0,1],[1,2],[0,3]]
    hasApple3 = [False, False, False, False]
    print(minTime(n3, edges3, hasApple3))  # Output: 0

"""
Time Complexity:
- Building the adjacency list takes O(n) since there are n-1 edges.
- The DFS traversal visits each node and edge once, so it takes O(n) time.
- Overall time complexity: O(n).

Space Complexity:
- The adjacency list uses O(n) space.
- The recursion stack in the worst case can go up to O(n) depth.
- Overall space complexity: O(n).

Topic: Tree, Depth-First Search (DFS)
"""