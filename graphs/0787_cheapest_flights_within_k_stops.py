"""
LeetCode Question #787: Cheapest Flights Within K Stops

Problem Statement:
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [from_i, to_i, price_i] 
indicates that there is a flight from city from_i to city to_i with cost price_i.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. 
If there is no such route, return -1.

Constraints:
- 1 <= n <= 100
- 0 <= flights.length <= n * (n - 1) / 2
- flights[i].length == 3
- 0 <= from_i, to_i < n
- from_i != to_i
- 1 <= price_i <= 10^4
- There will not be any duplicate flights.
- src, dst, and k are integers.
- 0 <= src, dst, k < n
"""

from collections import defaultdict, deque
import math

def findCheapestPrice(n, flights, src, dst, k):
    """
    Finds the cheapest price from src to dst with at most k stops.

    :param n: int - Number of cities
    :param flights: List[List[int]] - List of flights [from, to, price]
    :param src: int - Starting city
    :param dst: int - Destination city
    :param k: int - Maximum number of stops
    :return: int - Cheapest price or -1 if no route exists
    """
    # Build adjacency list for the graph
    graph = defaultdict(list)
    for from_i, to_i, price_i in flights:
        graph[from_i].append((to_i, price_i))
    
    # Use BFS with a priority queue to find the cheapest price
    queue = deque([(src, 0, 0)])  # (current_city, current_cost, stops)
    min_cost = {src: 0}
    
    while queue:
        current_city, current_cost, stops = queue.popleft()
        
        # If we exceed the maximum stops, skip this path
        if stops > k:
            continue
        
        # Explore neighbors
        for neighbor, price in graph[current_city]:
            new_cost = current_cost + price
            
            # If the new cost is cheaper, or we haven't visited this neighbor yet
            if neighbor not in min_cost or new_cost < min_cost[neighbor]:
                min_cost[neighbor] = new_cost
                queue.append((neighbor, new_cost, stops + 1))
    
    return min_cost.get(dst, -1)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100], [0, 2, 500]]
    src = 0
    dst = 3
    k = 1
    print(findCheapestPrice(n, flights, src, dst, k))  # Output: -1

    # Test Case 2
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    print(findCheapestPrice(n, flights, src, dst, k))  # Output: 200

    # Test Case 3
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 0
    print(findCheapestPrice(n, flights, src, dst, k))  # Output: 500


"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph takes O(flights.length).
- BFS traversal involves visiting each node and its neighbors. In the worst case, we visit all nodes and edges, resulting in O(n + flights.length).
- Overall time complexity: O(n + flights.length).

Space Complexity:
- The adjacency list requires O(flights.length) space.
- The queue can hold up to O(n) elements in the worst case.
- The min_cost dictionary requires O(n) space.
- Overall space complexity: O(n + flights.length).

Topic: Graphs
"""