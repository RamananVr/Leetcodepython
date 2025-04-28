"""
LeetCode Question #1687: Delivering Boxes from Storage to Ports

Problem Statement:
You have the task of delivering boxes from storage to ports using a truck. The ports are numbered from 1 to n, 
where n is the number of ports. You are given an array `boxes`, where `boxes[i] = [port_i, weight_i]` represents 
the port and weight of the i-th box. You are also given three integers `portsCount`, `maxBoxes`, and `maxWeight`.

- `portsCount` is the number of ports.
- `maxBoxes` is the maximum number of boxes the truck can carry at once.
- `maxWeight` is the maximum total weight the truck can carry at once.

The truck delivers the boxes in the order they appear in the array. The truck starts at storage, goes to the 
ports in the order of the boxes, and comes back to storage. The truck makes multiple trips if necessary.

The cost of a trip is defined as:
1. The number of different ports visited during the trip.
2. 1 for returning to storage.

You want to minimize the total cost of all trips.

Return the minimum total cost to deliver all boxes.

Constraints:
- 1 <= boxes.length <= 10^5
- 1 <= portsCount, maxBoxes <= 10^5
- 1 <= maxWeight <= 10^5
- 1 <= port_i <= portsCount
- 1 <= weight_i <= maxWeight
"""

from collections import deque

def boxDelivering(boxes, portsCount, maxBoxes, maxWeight):
    n = len(boxes)
    dp = [0] * (n + 1)  # dp[i] represents the minimum cost to deliver the first i boxes
    queue = deque([0])  # Monotonic queue to optimize the calculation of dp
    weight = 0  # Current weight of boxes in the truck
    trips = 0  # Number of trips for the current set of boxes

    for i in range(1, n + 1):
        port, w = boxes[i - 1]
        weight += w

        # Remove boxes from the front of the queue if they exceed maxBoxes or maxWeight
        while queue and (i - queue[0] > maxBoxes or weight > maxWeight):
            weight -= boxes[queue.popleft()][1]

        # Calculate trips for the current set of boxes
        trips = dp[queue[0]] + 1  # Start with the cost of the previous set of boxes + 1 trip
        if i > 1 and boxes[i - 1][0] != boxes[i - 2][0]:  # Add 1 for a new port visit
            trips += 1

        dp[i] = trips

        # Maintain monotonicity in the queue
        while queue and dp[queue[-1]] >= dp[i]:
            queue.pop()
        queue.append(i)

    return dp[n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    boxes = [[1, 1], [2, 1], [1, 1]]
    portsCount = 2
    maxBoxes = 3
    maxWeight = 3
    print(boxDelivering(boxes, portsCount, maxBoxes, maxWeight))  # Expected Output: 4

    # Test Case 2
    boxes = [[1, 2], [1, 4], [2, 3], [3, 2], [3, 1], [3, 1]]
    portsCount = 3
    maxBoxes = 3
    maxWeight = 6
    print(boxDelivering(boxes, portsCount, maxBoxes, maxWeight))  # Expected Output: 6

    # Test Case 3
    boxes = [[1, 1], [1, 1], [1, 1], [1, 1]]
    portsCount = 1
    maxBoxes = 4
    maxWeight = 4
    print(boxDelivering(boxes, portsCount, maxBoxes, maxWeight))  # Expected Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the `boxes` array once, making it O(n).
- The monotonic queue operations (append, pop) are amortized O(1) per element.
- Overall time complexity: O(n).

Space Complexity:
- The `dp` array requires O(n) space.
- The monotonic queue requires O(n) space in the worst case.
- Overall space complexity: O(n).

Topic: Dynamic Programming (DP), Monotonic Queue
"""