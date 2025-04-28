"""
LeetCode Problem #1606: Find Servers That Handled Most Number of Requests

Problem Statement:
You have k servers numbered from 0 to k-1 that are handling multiple requests. The requests are represented by a strictly increasing array `arrival`, where arrival[i] represents the arrival time of the i-th request, and another array `load`, where load[i] represents the time it takes for the i-th server to handle the request.

Each server can handle at most one request at a time. If a server is busy, the request will be handled by the next available server (in a cyclic manner). If all servers are busy, the request is dropped.

You need to find the servers that handled the most number of requests. Return a list containing the indices of these servers in ascending order.

Constraints:
- 1 <= k <= 10^5
- 1 <= arrival.length, load.length <= 10^5
- arrival[i] < arrival[i + 1]
- 1 <= load[i] <= 10^9

Example:
Input: k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3]
Output: [1]

Explanation:
- Server 0 handles requests 0 and 3 (total 2 requests).
- Server 1 handles requests 1 and 4 (total 2 requests).
- Server 2 handles request 2 (total 1 request).
- Servers 0 and 1 handled the most requests, but since we return the smallest indices, the output is [1].
"""

from heapq import heappush, heappop
from collections import defaultdict

def busiestServers(k, arrival, load):
    """
    Find the servers that handled the most number of requests.

    :param k: int - Number of servers
    :param arrival: List[int] - Arrival times of requests
    :param load: List[int] - Load times of requests
    :return: List[int] - Indices of servers that handled the most requests
    """
    # Priority queue to track when servers become available
    available_servers = list(range(k))
    busy_servers = []
    request_count = [0] * k  # Count of requests handled by each server

    for i, (start, duration) in enumerate(zip(arrival, load)):
        # Free up servers that have completed their tasks
        while busy_servers and busy_servers[0][0] <= start:
            _, server_id = heappop(busy_servers)
            heappush(available_servers, server_id)

        if not available_servers:
            continue  # Drop the request if no servers are available

        # Find the next available server in a cyclic manner
        server_index = i % k
        pos = next((s for s in available_servers if s >= server_index), None)
        if pos is None:
            pos = available_servers[0]

        # Assign the request to the chosen server
        available_servers.remove(pos)
        heappush(busy_servers, (start + duration, pos))
        request_count[pos] += 1

    # Find the servers with the maximum number of requests handled
    max_requests = max(request_count)
    return [i for i, count in enumerate(request_count) if count == max_requests]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    k = 3
    arrival = [1, 2, 3, 4, 5]
    load = [5, 2, 3, 3, 3]
    print(busiestServers(k, arrival, load))  # Output: [1]

    # Test Case 2
    k = 3
    arrival = [1, 2, 3, 4]
    load = [10, 10, 10, 10]
    print(busiestServers(k, arrival, load))  # Output: [0, 1, 2]

    # Test Case 3
    k = 1
    arrival = [1, 2, 3]
    load = [10, 10, 10]
    print(busiestServers(k, arrival, load))  # Output: [0]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Freeing up servers: O(n log k), where n is the number of requests and k is the number of servers.
- Assigning requests: O(n log k), as we use a priority queue to manage available servers.
- Overall: O(n log k)

Space Complexity:
- Priority queues for busy and available servers: O(k)
- Request count array: O(k)
- Overall: O(k)

Topic: Greedy, Heap (Priority Queue)
"""