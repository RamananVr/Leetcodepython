"""
LeetCode Problem #2045: Second Minimum Time to Reach Destination

Problem Statement:
You are given a directed graph of `n` nodes numbered from `1` to `n` where each node has at most one outgoing edge. 
The graph is represented by a 2D integer array `edges` where `edges[i] = [ui, vi]` indicates there is a directed edge 
from node `ui` to node `vi`. You are also given two integers `time` and `change`.

The graph is traversed as follows:
- You start at node `1` and can move to node `2` in `time` seconds.
- If you are at node `i`, you can move to node `j` in `time` seconds if there is an edge from `i` to `j`.

However, the traffic light at each node alternates between green and red every `change` seconds:
- During the green light, you can move to the next node.
- During the red light, you must wait until the light turns green.

Your task is to find the second minimum time it takes to reach node `n` from node `1`.

Constraints:
- `2 <= n <= 1000`
- `1 <= edges.length <= 1000`
- `edges[i].length == 2`
- `1 <= ui, vi <= n`
- `ui != vi`
- There are no duplicate edges.
- The graph is guaranteed to be connected.
- `1 <= time, change <= 10^3`
"""

from collections import defaultdict, deque

def secondMinimum(n, edges, time, change):
    # Build the graph as an adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # BFS to find the first and second shortest times to reach each node
    queue = deque([(1, 0)])  # (current node, current time)
    times = defaultdict(list)  # Store the times to reach each node
    
    while queue:
        node, curr_time = queue.popleft()
        
        # If we already have two times for this node, skip
        if len(times[node]) == 2:
            continue
        
        # Record the current time for this node
        times[node].append(curr_time)
        
        # Explore neighbors
        for neighbor in graph[node]:
            # Calculate the next time considering traffic lights
            next_time = curr_time + time
            if (next_time // change) % 2 == 1:  # If in red light
                next_time = (next_time // change + 1) * change
            
            # Add the neighbor to the queue
            queue.append((neighbor, next_time))
    
    # Return the second minimum time to reach node n
    return times[n][1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 5
    edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5]]
    time = 3
    change = 5
    print(secondMinimum(n, edges, time, change))  # Expected Output: 13

    # Test Case 2
    n = 4
    edges = [[1, 2], [2, 3], [3, 4], [1, 3]]
    time = 2
    change = 6
    print(secondMinimum(n, edges, time, change))  # Expected Output: 14

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph takes O(edges.length).
- BFS traversal explores each node and edge at most twice (since we need two times for each node), so the traversal takes O(n + edges.length).
- Overall time complexity: O(n + edges.length).

Space Complexity:
- The graph representation takes O(n + edges.length).
- The queue and times dictionary take O(n).
- Overall space complexity: O(n + edges.length).

Topic: Graphs, Breadth-First Search (BFS)
"""