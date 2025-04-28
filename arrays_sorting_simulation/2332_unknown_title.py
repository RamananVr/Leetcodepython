"""
LeetCode Problem #2332: The Latest Time to Catch a Bus

Problem Statement:
You are given a 0-indexed integer array `buses` of length `n`, where `buses[i]` represents the departure time of the ith bus. 
You are also given a 0-indexed integer array `passengers` of length `m`, where `passengers[j]` represents the arrival time of the jth passenger. 
All bus departure times are unique. All passenger arrival times are unique.

Each bus can transport at most `capacity` passengers at once. Passengers will get on the bus in the order of their arrival times, 
and they will wait in line for the next available bus that can transport them.

Return the latest time you may arrive at the bus station to catch a bus without missing it. 
You cannot arrive at the same time as another passenger, and you must catch a bus.

Constraints:
- `n == buses.length`
- `m == passengers.length`
- `1 <= n, m <= 10^5`
- `1 <= capacity <= 10^5`
- `1 <= buses[i], passengers[j] <= 10^9`
- All the values in `buses` are unique.
- All the values in `passengers` are unique.
"""

from typing import List

def latestTimeCatchTheBus(buses: List[int], passengers: List[int], capacity: int) -> int:
    # Sort buses and passengers
    buses.sort()
    passengers.sort()
    
    passenger_index = 0
    latest_time = 0

    for bus in buses:
        # Count how many passengers can board this bus
        count = 0
        while passenger_index < len(passengers) and passengers[passenger_index] <= bus and count < capacity:
            count += 1
            passenger_index += 1
        
        # If the bus is not full, we can arrive at the bus time or earlier
        if count < capacity:
            latest_time = bus
        else:
            # If the bus is full, the latest time is one second before the last passenger who boarded
            latest_time = passengers[passenger_index - 1] - 1
        
        # Ensure the latest time is not the same as any passenger's arrival time
        while latest_time in set(passengers):
            latest_time -= 1

    return latest_time

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    buses = [10, 20]
    passengers = [2, 17, 18, 19]
    capacity = 2
    print(latestTimeCatchTheBus(buses, passengers, capacity))  # Expected Output: 16

    # Test Case 2
    buses = [5, 10]
    passengers = [1, 2, 3, 4, 6, 7, 8, 9]
    capacity = 2
    print(latestTimeCatchTheBus(buses, passengers, capacity))  # Expected Output: 4

    # Test Case 3
    buses = [3]
    passengers = [1, 2, 3]
    capacity = 1
    print(latestTimeCatchTheBus(buses, passengers, capacity))  # Expected Output: 2

"""
Time Complexity Analysis:
- Sorting the `buses` and `passengers` arrays takes O(n log n + m log m), where n is the number of buses and m is the number of passengers.
- The main loop iterates over the buses (O(n)), and the inner loop iterates over the passengers (O(m) in total across all buses).
- Thus, the overall time complexity is O(n log n + m log m + m).

Space Complexity Analysis:
- The space complexity is O(1) additional space, as we are not using any extra data structures apart from a few variables.

Topic: Arrays, Sorting, Simulation
"""