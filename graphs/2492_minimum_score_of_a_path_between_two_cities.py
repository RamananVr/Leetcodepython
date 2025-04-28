"""
LeetCode Question #2492: Minimum Score of a Path Between Two Cities

Problem Statement:
You are given a positive integer n representing n cities numbered from 1 to n. 
You are also given a 2D array roads where roads[i] = [u_i, v_i, distance_i] indicates that 
there is a bidirectional road between cities u_i and v_i with a distance of distance_i.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum score of a path between city 1 and city n.

Note:
- A path is a sequence of roads connecting two cities.
- It is guaranteed that there is at least one path between city 1 and city n.

Constraints:
- 2 <= n <= 10^5
- 1 <= roads.length <= 10^5
- roads[i].length == 3
- 1 <= u_i, v_i <= n
- 1 <= distance_i <= 10^4
- There are no repeated roads.
"""

from collections import defaultdict, deque

def minScore(n: int, roads: list[list[int]]) -> int:
    """
    Finds the minimum score of a path between city 1 and city n.
    """
    # Build the graph as an adjacency list
    graph = defaultdict(list)
    for u, v, distance in roads:
        graph[u].append((v, distance))
        graph[v].append((u, distance))
    
    # Perform BFS to find all reachable nodes from city 1
    visited = set()
    queue = deque([1])
    visited.add(1)
    min_score = float('inf')
    
    while queue:
        current = queue.popleft()
        for neighbor, distance in graph[current]:
            # Update the minimum score
            min_score = min(min_score, distance)
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return min_score

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 4
    roads = [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]
    print(minScore(n, roads))  # Expected Output: 5

    # Test Case 2
    n = 6
    roads = [[1, 2, 4], [2, 3, 3], [3, 4, 2], [4, 5, 1], [5, 6, 10], [1, 6, 8]]
    print(minScore(n, roads))  # Expected Output: 1

    # Test Case 3
    n = 3
    roads = [[1, 2, 2], [2, 3, 3], [1, 3, 1]]
    print(minScore(n, roads))  # Expected Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph takes O(roads.length), which is O(E), where E is the number of edges.
- BFS traversal visits each node and edge once, so it takes O(V + E), where V is the number of nodes.
- Overall time complexity: O(V + E).

Space Complexity:
- The graph representation uses O(V + E) space.
- The visited set and queue use O(V) space.
- Overall space complexity: O(V + E).

Topic: Graphs
"""