"""
LeetCode Problem #2101: Detonate the Maximum Bombs

Problem Statement:
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. 
This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array `bombs` where:
- `bombs[i] = [xi, yi, ri]` denotes the location of the i-th bomb as (xi, yi) and the radius of its range as ri.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. 
These bombs will further detonate the bombs that lie in their ranges.

Return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb initially.

Constraints:
- 1 <= bombs.length <= 100
- bombs[i].length == 3
- 1 <= xi, yi, ri <= 10^5
"""

from collections import defaultdict, deque
import math

def maximumDetonation(bombs):
    """
    Function to calculate the maximum number of bombs that can be detonated.

    Args:
    bombs (List[List[int]]): A list of bombs where each bomb is represented as [xi, yi, ri].

    Returns:
    int: The maximum number of bombs that can be detonated.
    """
    def in_range(b1, b2):
        """Check if bomb b2 is within the range of bomb b1."""
        x1, y1, r1 = b1
        x2, y2, _ = b2
        return (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r1 ** 2

    # Build the graph
    n = len(bombs)
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i != j and in_range(bombs[i], bombs[j]):
                graph[i].append(j)

    # Perform BFS to find the maximum number of bombs detonated
    def bfs(start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return len(visited)

    # Try detonating each bomb and calculate the maximum
    max_detonated = 0
    for i in range(n):
        max_detonated = max(max_detonated, bfs(i))

    return max_detonated

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    bombs1 = [[2, 1, 3], [6, 1, 4]]
    print(maximumDetonation(bombs1))  # Output: 2

    # Test Case 2
    bombs2 = [[1, 1, 5], [10, 10, 5]]
    print(maximumDetonation(bombs2))  # Output: 1

    # Test Case 3
    bombs3 = [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]
    print(maximumDetonation(bombs3))  # Output: 5

"""
Time Complexity:
- Building the graph: O(n^2), where n is the number of bombs. For each pair of bombs, we check if one is in the range of the other.
- BFS: O(n + e), where e is the number of edges in the graph. In the worst case, e = O(n^2).
- Total: O(n^2) for graph construction + O(n^2) for BFS from each node = O(n^2).

Space Complexity:
- Graph storage: O(n^2) in the worst case.
- BFS visited set and queue: O(n).
- Total: O(n^2).

Topic: Graphs
"""