"""
LeetCode Problem #1184: Distance Between Bus Stops

Problem Statement:
A bus has `n` stops numbered from `0` to `n - 1` in clockwise order. We know the distance between all pairs of neighboring stops where `distance[i]` is the distance between the stop number `i` and the next stop `(i + 1) % n`. The bus goes in both clockwise and counterclockwise directions.

Given the array `distance` and two integers `start` and `destination`, return the shortest distance between the bus stops `start` and `destination`.

The distance between two stops is defined as the sum of distances between the stops along either the clockwise or the counterclockwise direction. Return the minimum of the two.

Constraints:
- `1 <= n <= 10^4`
- `distance.length == n`
- `0 <= start, destination < n`
- `0 <= distance[i] <= 10^4`

Example:
Input: distance = [1, 2, 3, 4], start = 0, destination = 3
Output: 4
Explanation: The distance from 0 -> 3 in clockwise order is 1 + 2 + 3 = 6, and in counterclockwise order is 4. The minimum is 4.
"""

# Python Solution
def distanceBetweenBusStops(distance, start, destination):
    """
    Calculate the shortest distance between two bus stops.

    :param distance: List[int] - distances between consecutive bus stops
    :param start: int - starting bus stop
    :param destination: int - destination bus stop
    :return: int - shortest distance between start and destination
    """
    if start > destination:
        start, destination = destination, start

    # Calculate clockwise distance
    clockwise_distance = sum(distance[start:destination])

    # Calculate total distance and counterclockwise distance
    total_distance = sum(distance)
    counterclockwise_distance = total_distance - clockwise_distance

    # Return the minimum of the two distances
    return min(clockwise_distance, counterclockwise_distance)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    distance = [1, 2, 3, 4]
    start = 0
    destination = 3
    print(distanceBetweenBusStops(distance, start, destination))  # Output: 4

    # Test Case 2
    distance = [7, 10, 1, 12, 11, 14, 5, 0]
    start = 7
    destination = 2
    print(distanceBetweenBusStops(distance, start, destination))  # Output: 17

    # Test Case 3
    distance = [1, 2, 3, 4]
    start = 3
    destination = 0
    print(distanceBetweenBusStops(distance, start, destination))  # Output: 4

    # Test Case 4
    distance = [1, 2, 3, 4, 5]
    start = 1
    destination = 4
    print(distanceBetweenBusStops(distance, start, destination))  # Output: 9

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the clockwise distance takes O(destination - start) time.
- Calculating the total distance takes O(n) time.
- Overall, the time complexity is O(n), where n is the number of bus stops.

Space Complexity:
- The solution uses O(1) additional space as it only uses a few variables for calculations.
"""

# Topic: Arrays