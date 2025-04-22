"""
LeetCode Problem #871: Minimum Number of Refueling Stops

Problem Statement:
A car travels from a starting position to a destination which is `target` miles east of the starting position. 
There are gas stations along the way. The car starts with an infinite tank of gas, but it can only travel `startFuel` miles on a full tank. 
The car can stop at gas stations to refuel, but it can only refuel at most the amount of gas available at that station.

Given the `target`, `startFuel`, and a list `stations` where `stations[i] = [position, fuel]` represents a gas station at position `position` with `fuel` liters of gas, 
return the minimum number of refueling stops needed to reach the destination. If it is impossible to reach the destination, return -1.

Note:
1. The car starts at position 0 and has `startFuel` liters of gas.
2. If the car reaches a gas station, it can refuel any amount of gas from that station.
3. The car can only stop at gas stations in the order they appear in the input.

Constraints:
- 1 <= target, startFuel <= 10^9
- 0 <= stations.length <= 500
- 0 <= position[i] < position[i+1] < target
- 1 <= fuel[i] < 10^9
"""

import heapq

def minRefuelStops(target: int, startFuel: int, stations: list[list[int]]) -> int:
    """
    Returns the minimum number of refueling stops required to reach the target.
    If it is impossible to reach the target, returns -1.
    """
    max_heap = []  # Max heap to store fuel amounts (negative values for max heap behavior)
    fuel = startFuel
    stops = 0
    prev_position = 0

    for position, station_fuel in stations + [[target, 0]]:
        fuel -= position - prev_position
        while max_heap and fuel < 0:
            fuel += -heapq.heappop(max_heap)
            stops += 1
        if fuel < 0:
            return -1
        heapq.heappush(max_heap, -station_fuel)
        prev_position = position

    return stops

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    target = 100
    startFuel = 10
    stations = [[10, 60], [20, 30], [30, 30], [60, 40]]
    print(minRefuelStops(target, startFuel, stations))  # Output: 2

    # Test Case 2
    target = 1
    startFuel = 1
    stations = []
    print(minRefuelStops(target, startFuel, stations))  # Output: 0

    # Test Case 3
    target = 100
    startFuel = 50
    stations = [[25, 25], [50, 50]]
    print(minRefuelStops(target, startFuel, stations))  # Output: 1

    # Test Case 4
    target = 1000
    startFuel = 1
    stations = [[10, 100], [20, 200], [30, 300], [40, 400]]
    print(minRefuelStops(target, startFuel, stations))  # Output: -1

"""
Time Complexity:
- The loop iterates over all stations and the target, so O(n), where n is the number of stations.
- Each heap operation (push/pop) is O(log n), and in the worst case, we perform a heap operation for every station.
- Overall time complexity: O(n log n).

Space Complexity:
- The heap can store at most n elements, where n is the number of stations.
- Overall space complexity: O(n).

Topic: Greedy, Heap (Priority Queue)
"""