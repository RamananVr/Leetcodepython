"""
LeetCode Question #815: Bus Routes

Problem Statement:
You are given an array `routes` representing bus routes where `routes[i]` is a bus route that the i-th bus repeats forever.
- For example, if `routes[0] = [1, 2, 7]`, this means that the 0-th bus travels in the sequence 1 -> 2 -> 7 -> 1 -> 2 -> 7 -> 1 -> ... forever.

You will start at the bus stop `source` (initially not on a bus), and you want to go to the bus stop `target`.
You can travel between bus stops by taking buses.

Return the least number of buses you must take to travel from the bus stop `source` to the bus stop `target`. If it is not possible to reach the target bus stop, return -1.

Constraints:
- `1 <= routes.length <= 500`
- `1 <= routes[i].length <= 10^5`
- All the values of `routes[i]` are unique.
- `sum(routes[i].length) <= 10^5`
- `0 <= routes[i][j] < 10^6`
- `0 <= source, target < 10^6`

Example:
Input: routes = [[1, 2, 7], [3, 6, 7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is to take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
"""

from collections import defaultdict, deque

def numBusesToDestination(routes, source, target):
    if source == target:
        return 0

    # Map each bus stop to the list of buses that pass through it
    stop_to_buses = defaultdict(list)
    for bus, stops in enumerate(routes):
        for stop in stops:
            stop_to_buses[stop].append(bus)

    # BFS initialization
    visited_stops = set()  # To track visited stops
    visited_buses = set()  # To track visited buses
    queue = deque([(source, 0)])  # (current stop, number of buses taken)

    while queue:
        current_stop, buses_taken = queue.popleft()

        # Check all buses passing through the current stop
        for bus in stop_to_buses[current_stop]:
            if bus in visited_buses:
                continue
            visited_buses.add(bus)

            # Check all stops on this bus route
            for stop in routes[bus]:
                if stop == target:
                    return buses_taken + 1
                if stop not in visited_stops:
                    visited_stops.add(stop)
                    queue.append((stop, buses_taken + 1))

    return -1  # If we exhaust the queue and don't find the target


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    routes = [[1, 2, 7], [3, 6, 7]]
    source = 1
    target = 6
    print(numBusesToDestination(routes, source, target))  # Output: 2

    # Test Case 2
    routes = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]
    source = 15
    target = 12
    print(numBusesToDestination(routes, source, target))  # Output: -1

    # Test Case 3
    routes = [[1, 2, 3, 4, 5], [5, 6, 7, 8, 9]]
    source = 1
    target = 9
    print(numBusesToDestination(routes, source, target))  # Output: 2

    # Test Case 4
    routes = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
    source = 1
    target = 7
    print(numBusesToDestination(routes, source, target))  # Output: 3


"""
Time Complexity Analysis:
- Let `n` be the total number of bus routes and `m` be the total number of bus stops across all routes.
- Building the `stop_to_buses` map takes O(m) time since we iterate through all stops in all routes.
- In the worst case, BFS visits all stops and buses, which takes O(m + n) time.
- Overall time complexity: O(m + n).

Space Complexity Analysis:
- The `stop_to_buses` dictionary takes O(m) space.
- The `visited_stops` and `visited_buses` sets take O(m) and O(n) space, respectively.
- The BFS queue can hold up to O(m) elements in the worst case.
- Overall space complexity: O(m + n).

Topic: Graph, Breadth-First Search (BFS)
"""