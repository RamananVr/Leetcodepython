"""
LeetCode Problem #1396: Design Underground System

Problem Statement:
An underground railway system is being designed to keep track of customer travel times between different stations. 
They want to write a class `UndergroundSystem` to manage the system. The system has three methods:

1. `checkIn(int id, string stationName, int t)`:
   - A customer with a unique ID checks in at the station `stationName` at time `t`.
   - A customer can only be checked into one station at a time.

2. `checkOut(int id, string stationName, int t)`:
   - A customer with a unique ID checks out from the station `stationName` at time `t`.

3. `getAverageTime(string startStation, string endStation)`:
   - Returns the average time it takes for customers to travel between the `startStation` and `endStation`.

You may assume all calls to `checkIn` and `checkOut` are consistent. That is:
   - A customer checking out will have previously checked in at the same station.
   - A customer checking in again will have already checked out from their previous trip.

Constraints:
- There will be at most 10^4 calls to `checkIn`, `checkOut`, and `getAverageTime`.
- All strings consist of uppercase and lowercase English letters and digits.
- `0 <= t <= 10^6`
- `1 <= id <= 10^6`
- The average time will be valid and will not exceed `10^6`.

"""

# Solution
class UndergroundSystem:
    def __init__(self):
        # Dictionary to store check-in information: {id: (stationName, time)}
        self.check_in_data = {}
        # Dictionary to store travel times: {(startStation, endStation): [totalTime, tripCount]}
        self.travel_data = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # Record the check-in information for the customer
        self.check_in_data[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # Retrieve the check-in information for the customer
        startStation, startTime = self.check_in_data.pop(id)
        # Calculate the travel time
        travelTime = t - startTime
        # Update the travel data for the route
        if (startStation, stationName) not in self.travel_data:
            self.travel_data[(startStation, stationName)] = [0, 0]  # [totalTime, tripCount]
        self.travel_data[(startStation, stationName)][0] += travelTime
        self.travel_data[(startStation, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # Retrieve the total time and trip count for the route
        totalTime, tripCount = self.travel_data[(startStation, endStation)]
        # Calculate and return the average time
        return totalTime / tripCount


# Example Test Cases
if __name__ == "__main__":
    # Create an instance of UndergroundSystem
    undergroundSystem = UndergroundSystem()

    # Test Case 1: Basic functionality
    undergroundSystem.checkIn(1, "A", 3)
    undergroundSystem.checkOut(1, "B", 8)
    print(undergroundSystem.getAverageTime("A", "B"))  # Output: 5.0

    # Test Case 2: Multiple trips
    undergroundSystem.checkIn(2, "A", 10)
    undergroundSystem.checkOut(2, "B", 15)
    print(undergroundSystem.getAverageTime("A", "B"))  # Output: 5.0

    undergroundSystem.checkIn(3, "A", 20)
    undergroundSystem.checkOut(3, "B", 30)
    print(undergroundSystem.getAverageTime("A", "B"))  # Output: 7.0

    # Test Case 3: Different routes
    undergroundSystem.checkIn(4, "C", 5)
    undergroundSystem.checkOut(4, "D", 10)
    print(undergroundSystem.getAverageTime("C", "D"))  # Output: 5.0

# Time and Space Complexity Analysis
"""
Time Complexity:
- `checkIn`: O(1) - Inserting data into a dictionary is O(1).
- `checkOut`: O(1) - Retrieving and updating data in a dictionary is O(1).
- `getAverageTime`: O(1) - Retrieving data from a dictionary is O(1).

Space Complexity:
- The space complexity is O(n + m), where:
  - n is the number of active check-ins stored in `check_in_data`.
  - m is the number of unique station pairs stored in `travel_data`.

Overall, the solution is efficient and scales well with the constraints.
"""

# Topic: Design, Hash Table