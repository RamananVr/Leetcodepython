"""
LeetCode Problem #1466: Reorder Routes to Make All Paths Lead to the City Zero

Problem Statement:
There are n cities numbered from 0 to n-1 and n-1 roads such that there is only one way to travel between two different cities (this network forms a tree). 
You are given an array roads where roads[i] = [ai, bi] represents a bidirectional road connecting cities ai and bi. 

You need to reorder some of the roads such that each city can visit the city 0. Return the minimum number of edges changed to make this possible.

Example 1:
Input: n = 6, roads = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of roads [1,3], [2,3], and [4,5] to make all paths lead to city 0.

Example 2:
Input: n = 5, roads = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of roads [1,2] and [3,4] to make all paths lead to city 0.

Constraints:
- 2 <= n <= 5 * 10^4
- roads.length == n-1
- roads[i].length == 2
- 0 <= ai, bi <= n-1
- ai != bi
- All the pairs (ai, bi) are distinct.
"""

from collections import defaultdict, deque

def minReorder(n: int, roads: list[list[int]]) -> int:
    # Build the graph
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append((b, 1))  # 1 indicates the road is directed from a to b
        graph[b].append((a, 0))  # 0 indicates the road is directed from b to a

    # BFS to count the number of roads to be reordered
    queue = deque([0])
    visited = set()
    reorder_count = 0

    while queue:
        current = queue.popleft()
        visited.add(current)

        for neighbor, direction in graph[current]:
            if neighbor not in visited:
                reorder_count += direction  # Add 1 if the road needs to be reordered
                queue.append(neighbor)

    return reorder_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 6
    roads1 = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    print(minReorder(n1, roads1))  # Output: 3

    # Test Case 2
    n2 = 5
    roads2 = [[1,0],[1,2],[3,2],[3,4]]
    print(minReorder(n2, roads2))  # Output: 2

    # Test Case 3
    n3 = 3
    roads3 = [[1,0],[2,0]]
    print(minReorder(n3, roads3))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph takes O(n) since there are n-1 roads.
- BFS traversal visits each node and edge once, which takes O(n).
- Overall time complexity is O(n).

Space Complexity:
- The graph uses O(n) space to store the adjacency list.
- The queue and visited set also use O(n) space in the worst case.
- Overall space complexity is O(n).

Topic: Graphs
"""