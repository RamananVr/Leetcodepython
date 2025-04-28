"""
LeetCode Problem #2039: The Time When the Network Becomes Idle

Problem Statement:
You are given a network of n servers, represented as an undirected graph. The graph is given as a 2D integer array edges, 
where edges[i] = [ui, vi] indicates there is a bidirectional edge between servers ui and vi. All servers are connected.

You are also given a 0-indexed integer array patience of length n. All servers are numbered from 0 to n - 1, where server 0 
is the main server.

Every server sends a message to the main server (server 0) at the start of each second, starting from the second 0. 
Messages sent by a server are sent along the shortest path to the main server, and arrive at the main server instantly.

The main server will process the message and send a reply to the server. The reply will be sent back to the server by 
following the same shortest path in reverse. Each server i needs to wait for the reply to arrive before sending another 
message. The time taken for a message to travel from a server to the main server and back is called the round-trip time.

If a server does not receive a reply for a message it sent, it will resend the message starting from the time when it 
last sent the message. You are also given that the network is idle when there are no messages passing between any servers.

Return the earliest time when the network becomes idle.

Constraints:
- 1 <= n <= 10^5
- 0 <= edges.length <= 10^5
- edges[i].length == 2
- 0 <= ui, vi < n
- ui != vi
- 1 <= patience[i] <= 10^5
- There is at least one edge connected to the main server.

"""

from collections import deque, defaultdict

def networkBecomesIdle(edges, patience):
    # Build the graph as an adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Perform BFS to calculate the shortest distance from server 0 to all other servers
    n = len(patience)
    distances = [-1] * n
    distances[0] = 0
    queue = deque([0])
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == -1:  # Not visited
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    
    # Calculate the time when the network becomes idle
    max_time = 0
    for i in range(1, n):  # Skip server 0
        round_trip_time = distances[i] * 2
        if round_trip_time <= patience[i]:
            last_message_time = 0
        else:
            last_message_time = ((round_trip_time - 1) // patience[i]) * patience[i]
        idle_time = last_message_time + round_trip_time
        max_time = max(max_time, idle_time)
    
    return max_time + 1  # Add 1 because the network becomes idle at the next second

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    edges = [[0, 1], [1, 2]]
    patience = [0, 2, 1]
    print(networkBecomesIdle(edges, patience))  # Output: 8

    # Test Case 2
    edges = [[0, 1], [0, 2], [1, 2]]
    patience = [0, 10, 10]
    print(networkBecomesIdle(edges, patience))  # Output: 3

    # Test Case 3
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    patience = [0, 1, 2, 3, 4]
    print(networkBecomesIdle(edges, patience))  # Output: 15

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph takes O(edges.length).
- BFS traversal takes O(n + edges.length), where n is the number of servers and edges.length is the number of edges.
- Calculating the idle time for each server takes O(n).
- Overall time complexity: O(n + edges.length).

Space Complexity:
- The graph representation takes O(n + edges.length).
- The distances array takes O(n).
- The BFS queue takes O(n) in the worst case.
- Overall space complexity: O(n + edges.length).

Topic: Graphs
"""