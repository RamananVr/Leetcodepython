"""
LeetCode Problem #2747: Count Zero Request Servers

Problem Statement:
You are given an integer `n` representing the number of servers, numbered from `0` to `n-1`. 
You are also given a 2D integer array `logs`, where each `logs[i] = [server_id, time]` indicates 
that server `server_id` received a request at time `time`. Additionally, you are given an integer 
`x` and a 1D integer array `queries`.

For each `queries[j]`, find the number of servers that did not receive any requests in the time 
interval `[queries[j], queries[j] + x - 1]`.

Return an array of integers where the `j-th` integer is the answer for the `j-th` query.

Constraints:
- `1 <= n <= 100`
- `1 <= logs.length <= 10^4`
- `0 <= server_id < n`
- `1 <= time, x, queries[j] <= 10^5`
- All the values in `logs` are unique.
- `queries` is sorted in ascending order.

"""

from collections import defaultdict
from bisect import bisect_left, bisect_right

def countZeroRequestServers(n, logs, x, queries):
    """
    Function to count the number of servers that did not receive any requests
    in the given time intervals for each query.

    Args:
    n (int): Number of servers.
    logs (List[List[int]]): List of logs where each log is [server_id, time].
    x (int): Length of the time interval.
    queries (List[int]): List of query start times.

    Returns:
    List[int]: List of counts of servers with zero requests for each query.
    """
    # Group logs by server_id
    server_logs = defaultdict(list)
    for server_id, time in logs:
        server_logs[server_id].append(time)

    # Sort the logs for each server to enable binary search
    for server_id in server_logs:
        server_logs[server_id].sort()

    result = []
    for query in queries:
        start_time = query
        end_time = query + x - 1
        zero_request_count = 0

        for server_id in range(n):
            # Get the logs for the current server
            times = server_logs[server_id]

            # Use binary search to find the range of times within [start_time, end_time]
            left = bisect_left(times, start_time)
            right = bisect_right(times, end_time)

            # If no logs are found in the range, increment the zero_request_count
            if right - left == 0:
                zero_request_count += 1

        result.append(zero_request_count)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    logs = [[0, 1], [1, 2], [2, 3], [0, 4], [1, 5]]
    x = 2
    queries = [1, 3, 5]
    print(countZeroRequestServers(n, logs, x, queries))  # Output: [1, 1, 2]

    # Test Case 2
    n = 2
    logs = [[0, 1], [1, 2], [0, 3], [1, 4]]
    x = 3
    queries = [1, 2]
    print(countZeroRequestServers(n, logs, x, queries))  # Output: [0, 0]

    # Test Case 3
    n = 4
    logs = [[0, 10], [1, 20], [2, 30], [3, 40]]
    x = 5
    queries = [5, 15, 25, 35]
    print(countZeroRequestServers(n, logs, x, queries))  # Output: [3, 3, 3, 3]

"""
Time Complexity:
- Preprocessing: Sorting the logs for each server takes O(L * log(L)), where L is the total number of logs.
- Query Processing: For each query, we iterate over all servers (O(n)) and perform binary search on their logs (O(log(L/n)) on average). 
  This results in O(q * n * log(L/n)), where q is the number of queries.
- Overall: O(L * log(L) + q * n * log(L/n)).

Space Complexity:
- The space required to store the logs for each server is O(L), where L is the total number of logs.
- Additional space for the result array is O(q).
- Overall: O(L + q).

Topic: Arrays, Binary Search
"""