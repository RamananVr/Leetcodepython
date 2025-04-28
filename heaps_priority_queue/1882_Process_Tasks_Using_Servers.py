"""
LeetCode Problem #1882: Process Tasks Using Servers

Problem Statement:
You are given two 0-indexed integer arrays `servers` and `tasks` of lengths `n` and `m` respectively. 
`servers[i]` is the weight of the i-th server, and `tasks[j]` is the time needed to process the j-th task in seconds.

Tasks are assigned to the servers using the following rules:
1. Each task can only be processed by one server at a time.
2. Each server can only process one task at a time.
3. A server becomes available again after it finishes processing a task.
4. A task j is assigned to a server i such that:
   - The server is available at the time the task is to be assigned.
   - If there are multiple available servers, the one with the smallest weight is chosen.
   - If there is a tie, the server with the smallest index is chosen.
5. If no server is available, the task waits until one becomes available.

Return an array `ans` of length `m`, where `ans[j]` is the index of the server that processes the j-th task.

Constraints:
- `servers.length == n`
- `tasks.length == m`
- `1 <= n, m <= 2 * 10^5`
- `1 <= servers[i], tasks[j] <= 2 * 10^5`
"""

from heapq import heappush, heappop

def assignTasks(servers, tasks):
    """
    Assign tasks to servers based on the given rules.

    :param servers: List[int] - weights of the servers
    :param tasks: List[int] - time required for each task
    :return: List[int] - indices of servers assigned to each task
    """
    n = len(servers)
    m = len(tasks)
    
    # Min-heap for available servers: (weight, index)
    available_servers = [(servers[i], i) for i in range(n)]
    available_servers.sort()
    
    # Min-heap for busy servers: (time when free, weight, index)
    busy_servers = []
    
    # Result array
    result = []
    
    # Current time
    time = 0
    
    for i in range(m):
        # Update current time to the max of current time or task index
        time = max(time, i)
        
        # Free up servers that have completed their tasks
        while busy_servers and busy_servers[0][0] <= time:
            free_time, weight, index = heappop(busy_servers)
            heappush(available_servers, (weight, index))
        
        # If no server is available, fast-forward time to the next available server
        if not available_servers:
            time = busy_servers[0][0]
            while busy_servers and busy_servers[0][0] <= time:
                free_time, weight, index = heappop(busy_servers)
                heappush(available_servers, (weight, index))
        
        # Assign the task to the best available server
        weight, index = heappop(available_servers)
        result.append(index)
        heappush(busy_servers, (time + tasks[i], weight, index))
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    servers = [3, 3, 2]
    tasks = [1, 2, 3, 2, 1, 2]
    print(assignTasks(servers, tasks))  # Output: [2, 2, 0, 2, 1, 2]

    # Test Case 2
    servers = [5, 1, 4, 3, 2]
    tasks = [2, 1, 2, 4, 5, 2, 1]
    print(assignTasks(servers, tasks))  # Output: [1, 4, 1, 4, 1, 3, 1]

    # Test Case 3
    servers = [10, 20, 30]
    tasks = [5, 5, 5, 5, 5]
    print(assignTasks(servers, tasks))  # Output: [0, 1, 2, 0, 1]

"""
Time Complexity:
- Sorting the servers initially takes O(n log n).
- For each task, we may push and pop from the heaps, which takes O(log n) per operation.
- In the worst case, we process all tasks, so the total complexity is O((n + m) log n).

Space Complexity:
- The space used by the heaps is O(n) for the available servers and O(n) for the busy servers.
- The result array takes O(m) space.
- Total space complexity is O(n + m).

Topic: Heaps, Priority Queue
"""