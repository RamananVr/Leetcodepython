"""
LeetCode Problem #886: Possible Bipartition

Problem Statement:
We want to split a group of `n` people (labeled from 1 to n) into two groups of any size. 
Each person may dislike some other people, and they should not be in the same group.

Given the integer `n` and the array `dislikes` where `dislikes[i] = [a, b]` indicates that 
person `a` and person `b` have a mutual dislike, return `true` if it is possible to split 
everyone into two groups in this way, otherwise return `false`.

Constraints:
- 1 <= n <= 2000
- 0 <= dislikes.length <= 10^4
- dislikes[i].length == 2
- 1 <= dislikes[i][j] <= n
- a != b
- All the pairs in dislikes are unique.

"""

# Solution
from collections import defaultdict, deque

def possibleBipartition(n, dislikes):
    # Build the graph as an adjacency list
    graph = defaultdict(list)
    for a, b in dislikes:
        graph[a].append(b)
        graph[b].append(a)
    
    # Dictionary to store the group assignment (1 or -1)
    group = {}
    
    # BFS function to check bipartition
    def bfs(node):
        queue = deque([node])
        group[node] = 1  # Assign the first group
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if neighbor not in group:
                    # Assign the opposite group to the neighbor
                    group[neighbor] = -group[current]
                    queue.append(neighbor)
                elif group[neighbor] == group[current]:
                    # If the neighbor is in the same group, bipartition is not possible
                    return False
        return True
    
    # Check each node (in case the graph is disconnected)
    for person in range(1, n + 1):
        if person not in group:
            if not bfs(person):
                return False
    
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Possible bipartition
    n1 = 4
    dislikes1 = [[1, 2], [1, 3], [2, 4]]
    print(possibleBipartition(n1, dislikes1))  # Expected output: True

    # Test Case 2: Impossible bipartition
    n2 = 3
    dislikes2 = [[1, 2], [1, 3], [2, 3]]
    print(possibleBipartition(n2, dislikes2))  # Expected output: False

    # Test Case 3: No dislikes
    n3 = 5
    dislikes3 = []
    print(possibleBipartition(n3, dislikes3))  # Expected output: True

    # Test Case 4: Large graph with possible bipartition
    n4 = 6
    dislikes4 = [[1, 2], [3, 4], [5, 6], [1, 3], [2, 4]]
    print(possibleBipartition(n4, dislikes4))  # Expected output: True

    # Test Case 5: Large graph with impossible bipartition
    n5 = 5
    dislikes5 = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]
    print(possibleBipartition(n5, dislikes5))  # Expected output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph takes O(dislikes.length).
- BFS traversal for each node takes O(V + E), where V is the number of nodes (n) and E is the number of edges (dislikes.length).
- In the worst case, we traverse all nodes and edges, so the overall time complexity is O(n + dislikes.length).

Space Complexity:
- The adjacency list representation of the graph takes O(n + dislikes.length).
- The `group` dictionary takes O(n) space.
- The BFS queue can take up to O(n) space in the worst case.
- Overall space complexity is O(n + dislikes.length).

Topic: Graph
"""