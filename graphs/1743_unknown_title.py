"""
LeetCode Problem #1743: Restore the Array From Adjacent Pairs

Problem Statement:
You are given a 2D integer array `adjacentPairs` of size `n - 1` where each `adjacentPairs[i] = [u, v]` indicates that the elements `u` and `v` are adjacent in the array.

It is guaranteed that the array can be restored from the adjacent pairs and that there is exactly one solution.

Return the restored array.

Constraints:
- `n == adjacentPairs.length + 1`
- `2 <= n <= 10^5`
- `-10^5 <= adjacentPairs[i][j] <= 10^5`

Example:
Input: adjacentPairs = [[2,1],[3,4],[3,2]]
Output: [1,2,3,4]

Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
Output: [-2,4,1,-3]
"""

# Solution
from collections import defaultdict, deque

def restoreArray(adjacentPairs):
    """
    Restore the array from adjacent pairs.

    :param adjacentPairs: List[List[int]] - List of adjacent pairs
    :return: List[int] - Restored array
    """
    # Step 1: Build the adjacency list
    adj = defaultdict(list)
    for u, v in adjacentPairs:
        adj[u].append(v)
        adj[v].append(u)
    
    # Step 2: Find the starting point (an element with only one neighbor)
    start = None
    for key, neighbors in adj.items():
        if len(neighbors) == 1:
            start = key
            break
    
    # Step 3: Restore the array using BFS/DFS
    restored = []
    visited = set()
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        restored.append(current)
        for neighbor in adj[current]:
            if neighbor not in visited:
                queue.append(neighbor)
    
    return restored

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    adjacentPairs1 = [[2, 1], [3, 4], [3, 2]]
    print(restoreArray(adjacentPairs1))  # Output: [1, 2, 3, 4]

    # Test Case 2
    adjacentPairs2 = [[4, -2], [1, 4], [-3, 1]]
    print(restoreArray(adjacentPairs2))  # Output: [-2, 4, 1, -3]

    # Test Case 3
    adjacentPairs3 = [[100000, -100000]]
    print(restoreArray(adjacentPairs3))  # Output: [100000, -100000]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Building the adjacency list takes O(n) time, where n is the number of pairs.
- Restoring the array involves visiting each node once, which takes O(n) time.
- Overall time complexity: O(n).

Space Complexity:
- The adjacency list uses O(n) space.
- The visited set and queue also use O(n) space in the worst case.
- Overall space complexity: O(n).
"""

# Topic: Graphs