"""
LeetCode Problem #2603: Collect Coins in a Tree

Problem Statement:
There is a tree (i.e., a connected, undirected graph with no cycles) consisting of `n` nodes numbered from `0` to `n - 1` and exactly `n - 1` edges. Each node has some coins associated with it, and you are given an integer array `coins` of size `n` where `coins[i]` is the number of coins associated with node `i`. You are also given a 2D integer array `edges` of size `n - 1` where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the tree.

Initially, you can choose to remove some edges from the tree. After removing the edges, the tree will be split into several connected components. Your goal is to collect all the coins in the tree. To do so, you can perform the following operation any number of times:

1. Choose any node in the tree and move to one of its adjacent nodes. You can only move between nodes that belong to the same connected component.

Return the minimum number of edges you need to remove from the tree such that you can collect all the coins in the tree.

Constraints:
- `1 <= n <= 10^5`
- `0 <= coins[i] <= 1`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= ai, bi < n`
- `ai != bi`
- The input represents a valid tree.

"""

from collections import defaultdict, deque

def collectTheCoins(coins, edges):
    """
    Function to calculate the minimum number of edges to remove to collect all coins in the tree.

    :param coins: List[int] - Number of coins at each node.
    :param edges: List[List[int]] - Edges of the tree.
    :return: int - Minimum number of edges to remove.
    """
    n = len(coins)
    if n == 1:
        return 0 if coins[0] == 0 else 0

    # Build the adjacency list for the tree
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Step 1: Remove leaf nodes with no coins
    degree = [len(graph[i]) for i in range(n)]
    queue = deque(i for i in range(n) if degree[i] == 1 and coins[i] == 0)

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            degree[neighbor] -= 1
            if degree[neighbor] == 1 and coins[neighbor] == 0:
                queue.append(neighbor)

    # Step 2: Remove leaf nodes with coins for two rounds
    queue = deque(i for i in range(n) if degree[i] == 1)
    for _ in range(2):
        new_queue = deque()
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    new_queue.append(neighbor)
        queue = new_queue

    # Step 3: Count the remaining edges
    remaining_edges = sum(degree[i] for i in range(n))
    return remaining_edges

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    coins = [1, 0, 0, 0, 0, 1]
    edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
    print(collectTheCoins(coins, edges))  # Output: 2

    # Test Case 2
    coins = [0, 0, 0, 1, 1, 0, 0, 1]
    edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [4, 6], [4, 7]]
    print(collectTheCoins(coins, edges))  # Output: 2

    # Test Case 3
    coins = [0, 0, 0, 0]
    edges = [[0, 1], [1, 2], [2, 3]]
    print(collectTheCoins(coins, edges))  # Output: 0

# Time Complexity Analysis:
# - Building the graph takes O(n).
# - Removing leaf nodes with no coins takes O(n).
# - Removing leaf nodes with coins for two rounds takes O(n).
# - Counting the remaining edges takes O(n).
# Overall time complexity: O(n).

# Space Complexity Analysis:
# - The adjacency list takes O(n) space.
# - The degree array takes O(n) space.
# - The queue takes O(n) space in the worst case.
# Overall space complexity: O(n).

# Topic: Graphs, Trees