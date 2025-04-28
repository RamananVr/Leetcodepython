"""
LeetCode Question #1094: Car Pooling

Problem Statement:
You are driving a vehicle that has a maximum passenger capacity `capacity`. 
The vehicle only drives along a single road, and you are given a list of 
`trips`, where `trips[i] = [numPassengers, fromLocation, toLocation]` indicates 
that the `i-th` trip has `numPassengers` passengers and the vehicle must pick 
up these passengers at `fromLocation` and drop them off at `toLocation`.

The locations are given as the number of kilometers due east from your vehicle's 
initial position.

Return `true` if and only if it is possible to pick up and drop off all passengers 
for all the given trips without exceeding the vehicle's capacity at any point.

Constraints:
- `1 <= trips.length <= 1000`
- `trips[i].length == 3`
- `1 <= numPassengers <= 100`
- `0 <= fromLocation < toLocation <= 1000`
- `1 <= capacity <= 10^5`
"""

# Solution
def carPooling(trips, capacity):
    """
    Determines if it is possible to pick up and drop off all passengers
    without exceeding the vehicle's capacity at any point.

    :param trips: List[List[int]] - List of trips, where each trip is represented as [numPassengers, fromLocation, toLocation].
    :param capacity: int - Maximum passenger capacity of the vehicle.
    :return: bool - True if all trips can be completed without exceeding capacity, False otherwise.
    """
    # Create an array to track passenger changes at each location
    passenger_changes = [0] * 1001  # Locations range from 0 to 1000

    # Record passenger changes for each trip
    for numPassengers, fromLocation, toLocation in trips:
        passenger_changes[fromLocation] += numPassengers
        passenger_changes[toLocation] -= numPassengers

    # Track the current number of passengers in the vehicle
    current_passengers = 0
    for change in passenger_changes:
        current_passengers += change
        if current_passengers > capacity:
            return False

    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic example
    trips1 = [[2, 1, 5], [3, 3, 7]]
    capacity1 = 4
    print(carPooling(trips1, capacity1))  # Output: False

    # Test Case 2: All trips fit within capacity
    trips2 = [[2, 1, 5], [3, 3, 7]]
    capacity2 = 5
    print(carPooling(trips2, capacity2))  # Output: True

    # Test Case 3: Single trip
    trips3 = [[5, 0, 5]]
    capacity3 = 5
    print(carPooling(trips3, capacity3))  # Output: True

    # Test Case 4: Overlapping trips exceed capacity
    trips4 = [[3, 2, 7], [3, 5, 9], [4, 1, 5]]
    capacity4 = 6
    print(carPooling(trips4, capacity4))  # Output: False

    # Test Case 5: No trips
    trips5 = []
    capacity5 = 10
    print(carPooling(trips5, capacity5))  # Output: True

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the `trips` list once to record passenger changes, which takes O(n), 
  where n is the number of trips.
- Then, it iterates through the `passenger_changes` array (of size 1001) to calculate the current 
  number of passengers at each location, which takes O(1001) = O(1) (constant time).

Overall time complexity: O(n).

Space Complexity:
- The `passenger_changes` array uses O(1001) = O(1) space (constant space).
- No additional data structures are used.

Overall space complexity: O(1).
"""

# Topic: Arrays