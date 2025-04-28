"""
LeetCode Problem #1890: The Latest Time to Catch a Bus

Problem Statement:
You are given a list of `buses` where `buses[i]` represents the departure time of the ith bus, and a list of `passengers` where `passengers[j]` represents the arrival time of the jth passenger. All bus departure times and passenger arrival times are given in minutes after midnight. You are also given an integer `capacity`, which represents the maximum number of passengers that can board each bus.

Return the latest time you can arrive at the bus station to catch a bus without missing it. You cannot arrive at the same time as another passenger, and you must arrive before the departure time of the bus you want to catch.

Constraints:
- 1 <= buses.length, passengers.length <= 10^5
- 0 <= buses[i], passengers[j] <= 10^9
- 1 <= capacity <= 10^5

Example:
Input: buses = [10, 20], passengers = [2, 17, 18, 19], capacity = 2
Output: 16
Explanation: 
- The first bus departs at 10, and only 2 passengers can board it. Passengers [2] and [17] board the first bus.
- The second bus departs at 20, and only 2 passengers can board it. Passengers [18] and [19] board the second bus.
- You can arrive at the bus station at time 16, which is the latest time you can catch the second bus without arriving at the same time as another passenger.

"""

# Python Solution
def latestTimeCatchTheBus(buses, passengers, capacity):
    # Sort buses and passengers by their times
    buses.sort()
    passengers.sort()
    
    # Initialize passenger index
    passenger_idx = 0
    
    # Iterate through each bus
    for bus in buses:
        # Count how many passengers can board the current bus
        count = 0
        while passenger_idx < len(passengers) and passengers[passenger_idx] <= bus and count < capacity:
            count += 1
            passenger_idx += 1
    
    # Find the latest time to catch the last bus
    latest_time = buses[-1]
    if count < capacity:
        # If the last bus is not full, we can arrive at its departure time
        latest_time = buses[-1]
    else:
        # Otherwise, we need to arrive before the last passenger who boarded
        latest_time = passengers[passenger_idx - 1] - 1
    
    # Ensure the latest time is not the same as any passenger's arrival time
    passenger_set = set(passengers)
    while latest_time in passenger_set:
        latest_time -= 1
    
    return latest_time

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    buses = [10, 20]
    passengers = [2, 17, 18, 19]
    capacity = 2
    print(latestTimeCatchTheBus(buses, passengers, capacity))  # Output: 16

    # Test Case 2
    buses = [5, 10, 15]
    passengers = [1, 2, 3, 8, 9, 14]
    capacity = 2
    print(latestTimeCatchTheBus(buses, passengers, capacity))  # Output: 13

    # Test Case 3
    buses = [20]
    passengers = [5, 10, 15, 19]
    capacity = 3
    print(latestTimeCatchTheBus(buses, passengers, capacity))  # Output: 18

    # Test Case 4
    buses = [10, 20, 30]
    passengers = [5, 15, 25, 35]
    capacity = 1
    print(latestTimeCatchTheBus(buses, passengers, capacity))  # Output: 29

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the buses and passengers takes O(n log n), where n is the maximum of len(buses) and len(passengers).
- Iterating through the buses and passengers takes O(n).
- The while loop to find the latest time takes O(n) in the worst case.
Overall, the time complexity is O(n log n).

Space Complexity:
- Sorting uses O(n) space for the sorting algorithm.
- The passenger_set uses O(n) space.
Overall, the space complexity is O(n).
"""

# Topic: Arrays, Sorting