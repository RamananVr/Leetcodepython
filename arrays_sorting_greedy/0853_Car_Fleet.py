"""
LeetCode Problem #853: Car Fleet

Problem Statement:
There are `n` cars going to the same destination along a one-lane road. The destination is at position `target`, and each car `i` has a constant speed `speed[i]` (in miles per hour) and initial position `position[i]` (in miles).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the speed of the slower car. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same speed. Note that a single car is also a fleet.

If a car catches up to another car at the destination point, they will still arrive as one fleet.

Return the number of car fleets that will arrive at the destination.

Example 1:
Input: target = 12, position = [10, 8, 0, 5, 3], speed = [2, 4, 1, 1, 3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) arrive together as a fleet, and the car starting at 0 (speed 1) arrives on its own. The car starting at 5 (speed 1) and the car starting at 3 (speed 3) arrive together as a fleet.

Example 2:
Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation: There is only one car and hence only one fleet.

Example 3:
Input: target = 100, position = [0, 2, 4], speed = [4, 2, 1]
Output: 1
Explanation: All cars will arrive at the destination at the same time, forming one fleet.

Constraints:
- `n == position.length == speed.length`
- `1 <= n <= 10^5`
- `0 < target <= 10^6`
- `0 <= position[i] < target`
- All the values of `position` are unique.
- `0 < speed[i] <= 10^6`
"""

# Python Solution
def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    # Pair position and speed, and sort cars by their starting position in descending order
    cars = sorted(zip(position, speed), reverse=True)
    
    fleets = 0
    time_to_reach = 0  # Time for the last fleet to reach the destination
    
    for pos, spd in cars:
        # Calculate the time it takes for the current car to reach the destination
        time = (target - pos) / spd
        
        # If the current car takes more time than the last fleet, it forms a new fleet
        if time > time_to_reach:
            fleets += 1
            time_to_reach = time  # Update the time for the last fleet
    
    return fleets

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    print(carFleet(target, position, speed))  # Output: 3

    # Test Case 2
    target = 10
    position = [3]
    speed = [3]
    print(carFleet(target, position, speed))  # Output: 1

    # Test Case 3
    target = 100
    position = [0, 2, 4]
    speed = [4, 2, 1]
    print(carFleet(target, position, speed))  # Output: 1

    # Test Case 4
    target = 15
    position = [0, 4, 2]
    speed = [4, 2, 1]
    print(carFleet(target, position, speed))  # Output: 3

    # Test Case 5
    target = 20
    position = [6, 8, 10]
    speed = [3, 2, 1]
    print(carFleet(target, position, speed))  # Output: 3

# Time Complexity Analysis:
# Sorting the cars by position takes O(n log n), where n is the number of cars.
# The subsequent loop to calculate fleets runs in O(n).
# Overall time complexity: O(n log n).

# Space Complexity Analysis:
# The space complexity is O(n) due to the storage of the `cars` list.
# Overall space complexity: O(n).

# Topic: Arrays, Sorting, Greedy