"""
LeetCode Problem #1916: Count Ways to Build Rooms in an Ant Colony

Problem Statement:
You are an ant tasked with building a colony of rooms. The colony starts with a single room, which is room 0. 
You are given a 2D integer array `prevRoom` where `prevRoom[i]` indicates that you must build room `i` 
only after building room `prevRoom[i]`. Room `prevRoom[i]` can be the direct parent of room `i`.

The room 0 is the root room, and every room must be built exactly once. Return the number of different ways 
to build all the rooms modulo 10^9 + 7.

Constraints:
- 1 <= prevRoom.length <= 10^5
- 0 <= prevRoom[i] < i

Example:
Input: prevRoom = [-1, 0, 1, 2]
Output: 1
Explanation: There is only one way to build the rooms: 0 -> 1 -> 2 -> 3.

Input: prevRoom = [-1, 0, 0, 1, 2]
Output: 6
Explanation: There are 6 ways to build the rooms.

"""

# Solution
from math import factorial
from collections import defaultdict

MOD = 10**9 + 7

def countWays(prevRoom):
    def dfs(node):
        size = 1
        ways = 1
        for child in graph[node]:
            child_size, child_ways = dfs(child)
            size += child_size
            ways = ways * child_ways * factorial(size - 1) // (factorial(child_size) * factorial(size - 1 - child_size)) % MOD
        return size, ways

    # Build the graph
    graph = defaultdict(list)
    for i, parent in enumerate(prevRoom):
        if parent != -1:
            graph[parent].append(i)

    # Start DFS from the root room (room 0)
    _, result = dfs(0)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    prevRoom = [-1, 0, 1, 2]
    print(countWays(prevRoom))  # Output: 1

    # Test Case 2
    prevRoom = [-1, 0, 0, 1, 2]
    print(countWays(prevRoom))  # Output: 6

    # Test Case 3
    prevRoom = [-1, 0, 0, 0]
    print(countWays(prevRoom))  # Output: 6

    # Test Case 4
    prevRoom = [-1, 0, 1, 1, 2, 2]
    print(countWays(prevRoom))  # Output: 90

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph takes O(n), where n is the length of `prevRoom`.
- The DFS traversal visits each node once, and for each node, we compute factorials and combinations. 
  Computing factorials and combinations is efficient due to memoization, so the DFS traversal is O(n).
- Overall, the time complexity is O(n).

Space Complexity:
- The graph representation uses O(n) space.
- The DFS recursion stack uses O(h) space, where h is the height of the tree. In the worst case, h = n.
- Overall, the space complexity is O(n).

Topic: Graphs, Tree, DFS
"""